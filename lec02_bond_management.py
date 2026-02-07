import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Page configuration (must be first Streamlit call)
st.set_page_config(
    page_title="Managing Bond Portfolios",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1E2761;
        text-align: center;
        padding: 1rem 0;
        font-weight: bold;
    }
    .section-header {
        font-size: 2rem;
        color: #065A82;
        border-bottom: 3px solid #21295C;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .concept-box {
        background-color: #F2F2F2;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #028090;
        margin: 1rem 0;
    }
    .formula-box {
        background-color: #CADCFC;
        padding: 1rem;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        margin: 1rem 0;
        text-align: center;
        font-size: 1.1rem;
    }
    .highlight {
        background-color: #F9E795;
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
        font-weight: bold;
    }
    .success-box {
        background-color: #97BC62;
        padding: 1rem;
        border-radius: 8px;
        color: white;
        font-weight: bold;
    }
    .warning-box {
        background-color: #F96167;
        padding: 1rem;
        border-radius: 8px;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------
def _safe_periods(years: float, frequency: int) -> int:
    """Convert years to integer number of coupon periods robustly."""
    if years is None or years <= 0:
        return 0
    return max(int(round(years * frequency)), 1)

def calculate_bond_price(face_value, coupon_rate, years, ytm, frequency=2):
    """Calculate bond price (PV of cash flows)."""
    if years is None or years <= 0:
        return float(face_value)

    n = _safe_periods(years, frequency)
    c = (face_value * coupon_rate) / frequency
    r = ytm / frequency

    if abs(r) < 1e-12:
        pv_coupons = c * n
        pv_face = face_value
    else:
        pv_coupons = c * (1 - (1 + r) ** (-n)) / r
        pv_face = face_value / ((1 + r) ** n)

    return pv_coupons + pv_face

def calculate_duration(face_value, coupon_rate, years, ytm, frequency=2):
    """Calculate Macaulay Duration (in years)."""
    if years is None or years <= 0:
        return 0.0

    n = _safe_periods(years, frequency)
    c = (face_value * coupon_rate) / frequency
    r = ytm / frequency

    weighted_pv = 0.0
    total_pv = 0.0

    for t in range(1, n + 1):
        cf = c
        if t == n:
            cf += face_value

        if abs(r) < 1e-12:
            pv = cf
        else:
            pv = cf / ((1 + r) ** t)

        time_in_years = t / frequency
        weighted_pv += time_in_years * pv
        total_pv += pv

    return (weighted_pv / total_pv) if total_pv != 0 else np.nan

def calculate_modified_duration(macaulay_duration, ytm, frequency=2):
    """Calculate Modified Duration."""
    return macaulay_duration / (1 + ytm / frequency) if (1 + ytm / frequency) != 0 else np.nan

def calculate_convexity(face_value, coupon_rate, years, ytm, frequency=2):
    """Calculate Convexity (discrete approximation)."""
    if years is None or years <= 0:
        return 0.0

    n = _safe_periods(years, frequency)
    c = (face_value * coupon_rate) / frequency
    r = ytm / frequency

    price = calculate_bond_price(face_value, coupon_rate, years, ytm, frequency)
    if price == 0:
        return np.nan

    convexity_sum = 0.0
    for t in range(1, n + 1):
        cf = c
        if t == n:
            cf += face_value

        if abs(r) < 1e-12:
            pv = cf
        else:
            pv = cf / ((1 + r) ** t)

        convexity_sum += pv * t * (t + 1)

    denom = price * (1 + r) ** 2 * frequency ** 2
    return convexity_sum / denom if denom != 0 else np.nan

def price_change_duration(modified_duration, delta_yield):
    """Estimate price change using duration: ΔP/P ≈ -D* Δy."""
    return -modified_duration * delta_yield

def price_change_duration_convexity(modified_duration, convexity, delta_yield):
    """Estimate price change using duration + convexity."""
    duration_effect = -modified_duration * delta_yield
    convexity_effect = 0.5 * convexity * (delta_yield ** 2)
    return duration_effect + convexity_effect

def _safe_rel_error(estimate: float, actual: float) -> float:
    """Relative error in percent with safe handling for actual≈0."""
    if abs(actual) < 1e-12:
        return 0.0 if abs(estimate) < 1e-12 else np.inf
    return abs(estimate - actual) / abs(actual) * 100.0

# -----------------------------------------------------------------------------
# Main App
# -----------------------------------------------------------------------------
def main():
    # Sidebar Navigation
    st.sidebar.markdown("## 📚 Navigation")
    page = st.sidebar.radio(
        "Choose a topic:",
        [
            "🏠 Home",
            "⏱️ Duration Basics",
            "📐 Duration Calculator",
            "🎯 Interest Rate Risk",
            "🛡️ Immunization",
            "🌊 Convexity",
            "📊 Active Strategies",
            "✅ Quiz",
        ],
    )

    if page == "🏠 Home":
        show_home()
    elif page == "⏱️ Duration Basics":
        show_duration_basics()
    elif page == "📐 Duration Calculator":
        show_duration_calculator()
    elif page == "🎯 Interest Rate Risk":
        show_interest_rate_risk()
    elif page == "🛡️ Immunization":
        show_immunization()
    elif page == "🌊 Convexity":
        show_convexity()
    elif page == "📊 Active Strategies":
        show_active_strategies()
    elif page == "✅ Quiz":
        show_quiz()

def show_home():
    st.markdown('<div class="main-header">📊 Managing Bond Portfolios</div>', unsafe_allow_html=True)
    st.markdown(
        '<p style="text-align: center; font-size: 1.2rem; color: #666;">Duration, Convexity & Portfolio Strategies</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">⏱️ Duration</h3>
        <p>Measure the sensitivity of bond prices to interest rate changes</p>
        <ul>
        <li>Macaulay Duration</li>
        <li>Modified Duration</li>
        <li>Duration Rules</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">🌊 Convexity</h3>
        <p>Capture the curvature in price-yield relationship</p>
        <ul>
        <li>Why Duration Isn't Enough</li>
        <li>Convexity Formula</li>
        <li>Positive Convexity Benefit</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">🛡️ Immunization</h3>
        <p>Shield portfolio value from interest rate movements</p>
        <ul>
        <li>Duration Matching</li>
        <li>Cash Flow Matching</li>
        <li>Rebalancing Strategies</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown('<div class="section-header">📋 Chapter Overview</div>', unsafe_allow_html=True)

    st.markdown("""
    This interactive app covers **Managing Bond Portfolios**.

    ### Topics Covered:

    1. **Interest Rate Risk** - Understanding bond price sensitivity  
    2. **Duration** - The primary measure of interest rate risk  
    3. **Passive Management** - Immunization and cash flow matching  
    4. **Convexity** - Refining duration-based estimates  
    5. **Active Strategies** - Bond swaps and horizon analysis  

    ### 🎯 Learning Objectives:

    By the end of this module, you will be able to:
    - Calculate and interpret Macaulay and Modified Duration
    - Understand the determinants of duration
    - Use duration to immunize bond portfolios
    - Calculate and apply convexity measures
    - Analyze active bond management strategies
    """)

    st.info("💡 **Tip:** Duration is to bonds what Beta is to stocks - a measure of systematic risk!")

def show_duration_basics():
    st.markdown('<div class="section-header">⏱️ Duration Basics</div>', unsafe_allow_html=True)

    st.markdown("""
    ### What is Duration?

    **Duration** is a measure of the weighted average time until a bond's cash flows are received.
    It serves two critical purposes:
    1. **Timing measure**: Average time to recover investment
    2. **Risk measure**: Sensitivity of bond price to interest rate changes
    """)

    st.markdown("---")

    # Macaulay Duration
    st.markdown("### 📏 Macaulay Duration")

    st.markdown("""
    <div class="formula-box">
    <strong>Macaulay Duration Formula:</strong><br><br>
    D = Σ [t × PV(CFₜ)] / Price<br><br>
    Where:<br>
    t = time period<br>
    PV(CFₜ) = present value of cash flow at time t<br>
    Price = current bond price
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="concept-box">
        <h4>Interpretation</h4>
        <p>If a bond has a Macaulay Duration of <strong>5 years</strong>:</p>
        <ul>
        <li>On average, you receive your investment back in 5 years</li>
        <li>The bond's price sensitivity is equivalent to a 5-year zero-coupon bond</li>
        <li>Weighted average maturity of cash flows is 5 years</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="concept-box">
        <h4>Key Properties</h4>
        <ul>
        <li><strong>Zero-coupon bond</strong>: Duration = Maturity</li>
        <li><strong>Coupon bond</strong>: Duration < Maturity</li>
        <li><strong>Higher coupon</strong> → Lower duration</li>
        <li><strong>Longer maturity</strong> → Higher duration</li>
        <li><strong>Higher YTM</strong> → Lower duration</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Modified Duration
    st.markdown("### 🎯 Modified Duration")

    st.markdown("""
    <div class="formula-box">
    <strong>Modified Duration Formula:</strong><br><br>
    D* = D / (1 + y/k)<br><br>
    Where:<br>
    D = Macaulay Duration<br>
    y = Yield to maturity<br>
    k = Number of coupon payments per year
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="concept-box">
    <h4>💡 Why Modified Duration?</h4>
    <p>Modified duration directly measures <strong>percentage price change</strong> for a given yield change:</p>
    <div class="formula-box">
    ΔPrice/Price ≈ -D* × Δy
    </div>
    <p><strong>Example:</strong> If Modified Duration = 7 and yields rise by 1%:</p>
    <p>Price change ≈ -7 × 0.01 = -0.07 = <strong>-7%</strong></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Duration Rules
    st.markdown("### 📋 Duration Rules")

    tab1, tab2, tab3, tab4 = st.tabs(["Rule 1: Zero-Coupon", "Rule 2: Coupon Rate",
                                       "Rule 3: Maturity", "Rule 4: YTM"])

    with tab1:
        st.markdown("""
        #### Rule 1: Zero-Coupon Bonds

        **For zero-coupon bonds, Duration = Time to Maturity**

        Why? All cash flow occurs at maturity, so the weighted average time is simply the maturity.
        """)

        maturities = np.array([1, 5, 10, 15, 20, 25, 30])

        fig = go.Figure()
        fig.add_trace(go.Bar(x=maturities, y=maturities, name='Duration = Maturity'))
        fig.update_layout(
            title="Zero-Coupon Bond: Duration = Maturity",
            xaxis_title="Maturity (years)",
            yaxis_title="Duration (years)",
            height=400,
            xaxis=dict(tickmode='linear', dtick=5)
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.markdown("""
        #### Rule 2: Coupon Rate Effect

        **Higher coupon rate → Lower duration**

        Why? Higher coupons mean more cash received earlier, reducing the weighted average time.
        """)

        coupon_rates = np.array([0, 3, 6, 9, 12])
        durations = []

        for cr in coupon_rates:
            dur = calculate_duration(1000, cr / 100, 10, 0.08, 2)
            durations.append(dur)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=coupon_rates, y=durations, mode='lines+markers'))
        fig.update_layout(
            title="Duration vs Coupon Rate (10-year bond, 8% YTM)",
            xaxis_title="Coupon Rate (%)",
            yaxis_title="Duration (years)",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

        st.info("💡 Notice: As coupon rate increases, duration decreases!")

    with tab3:
        st.markdown("""
        #### Rule 3: Maturity Effect

        **Longer maturity → Higher duration (generally)**

        Note: For bonds selling at or above par, duration always increases with maturity.
        For deep discount bonds, duration may eventually decrease at very long maturities.
        """)

        maturities = np.linspace(1, 30, 30)
        durations_6pct = [calculate_duration(1000, 0.06, m, 0.08, 2) for m in maturities]
        durations_0pct = maturities  # Zero-coupon

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=maturities, y=durations_6pct, mode='lines', name='6% Coupon Bond'))
        fig.add_trace(go.Scatter(x=maturities, y=durations_0pct, mode='lines', name='Zero-Coupon Bond', line=dict(dash='dash')))
        fig.update_layout(
            title="Duration vs Maturity (8% YTM)",
            xaxis_title="Maturity (years)",
            yaxis_title="Duration (years)",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab4:
        st.markdown("""
        #### Rule 4: YTM Effect

        **Higher YTM → Lower duration**

        Why? Higher discount rates reduce the present value weight of distant cash flows.
        """)

        ytms = np.linspace(0.02, 0.15, 30)
        durations_ytm = [calculate_duration(1000, 0.06, 10, y, 2) for y in ytms]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=ytms * 100, y=durations_ytm, mode='lines+markers'))
        fig.update_layout(
            title="Duration vs YTM (10-year bond, 6% coupon)",
            xaxis_title="Yield to Maturity (%)",
            yaxis_title="Duration (years)",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

def show_duration_calculator():
    st.markdown('<div class="section-header">📐 Duration Calculator</div>', unsafe_allow_html=True)

    st.markdown("Calculate Macaulay Duration, Modified Duration, and analyze bond sensitivity.")

    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("### Bond Parameters")

        face_value = st.number_input("Face Value ($)", value=1000, step=100, key="dur_fv")
        coupon_rate = st.number_input("Annual Coupon Rate (%)", value=6.0, step=0.5, key="dur_cr") / 100
        years = st.slider("Years to Maturity", 1, 30, 10, key="dur_years")
        ytm = st.number_input("Yield to Maturity (%)", value=8.0, step=0.5, key="dur_ytm") / 100
        frequency = st.selectbox(
            "Payment Frequency",
            [("Semi-annual", 2), ("Annual", 1)],
            format_func=lambda x: x[0],
            key="dur_freq",
        )[1]

        st.markdown("### Yield Change Scenario")
        delta_yield = st.slider("Change in Yield (basis points)", -300, 300, 100, 10, key="dur_dy") / 10000

    with col2:
        price = calculate_bond_price(face_value, coupon_rate, years, ytm, frequency)
        macaulay_dur = calculate_duration(face_value, coupon_rate, years, ytm, frequency)
        modified_dur = calculate_modified_duration(macaulay_dur, ytm, frequency)
        convexity = calculate_convexity(face_value, coupon_rate, years, ytm, frequency)

        st.markdown("### Results")

        metric_col1, metric_col2, metric_col3 = st.columns(3)
        with metric_col1:
            st.metric("Bond Price", f"${price:.2f}")
        with metric_col2:
            st.metric("Macaulay Duration", f"{macaulay_dur:.3f} years")
        with metric_col3:
            st.metric("Modified Duration", f"{modified_dur:.3f}")

        st.markdown("---")

        st.markdown("### Interest Rate Sensitivity Analysis")

        new_ytm = ytm + delta_yield
        new_price = calculate_bond_price(face_value, coupon_rate, years, new_ytm, frequency)
        actual_change = (new_price - price) / price if price != 0 else np.nan

        duration_pct = price_change_duration(modified_dur, delta_yield)
        convexity_pct = price_change_duration_convexity(modified_dur, convexity, delta_yield)

        comparison_df = pd.DataFrame({
            'Method': ['Actual Change', 'Duration Estimate', 'Duration + Convexity'],
            'Price Change (%)': [actual_change * 100, duration_pct * 100, convexity_pct * 100],
            'New Price ($)': [new_price, price * (1 + duration_pct), price * (1 + convexity_pct)]
        })

        st.dataframe(comparison_df.style.format({
            'Price Change (%)': '{:.4f}%',
            'New Price ($)': '${:.2f}'
        }), use_container_width=True)

        duration_error = _safe_rel_error(duration_pct, actual_change)
        convexity_error = _safe_rel_error(convexity_pct, actual_change)

        if np.isinf(duration_error) or np.isinf(convexity_error):
            improvement_text = "n/a (actual change ~ 0)"
            improvement_val = 0.0
        else:
            improvement_val = duration_error - convexity_error
            improvement_text = f"{improvement_val:.2f} percentage points"

        st.markdown(f"""
        <div class="concept-box">
        <h4>Estimation Accuracy</h4>
        <p><strong>Duration-only error:</strong> {duration_error:.2f}%</p>
        <p><strong>Duration + Convexity error:</strong> {convexity_error:.2f}%</p>
        <p>Convexity improves accuracy by <strong>{improvement_text}</strong></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Cash Flow and Duration Calculation")

    n_periods = _safe_periods(years, frequency)
    coupon_payment = (face_value * coupon_rate) / frequency
    r = ytm / frequency

    cf_data = []
    for t in range(1, min(n_periods + 1, 21)):  # Show first 20 periods
        cf = coupon_payment
        if t == n_periods:
            cf += face_value

        time_years = t / frequency
        if abs(r) < 1e-12:
            pv = cf
        else:
            pv = cf / ((1 + r) ** t)

        weight = (pv / price) if price != 0 else np.nan
        weighted_time = time_years * weight if pd.notna(weight) else np.nan

        cf_data.append({
            'Period': t,
            'Time (years)': f'{time_years:.2f}',
            'Cash Flow': f'${cf:.2f}',
            'Present Value': f'${pv:.2f}',
            'Weight': f'{weight:.4f}' if pd.notna(weight) else 'n/a',
            'Time × Weight': f'{weighted_time:.4f}' if pd.notna(weighted_time) else 'n/a'
        })

    if n_periods > 20:
        cf_data.append({
            'Period': '...',
            'Time (years)': '...',
            'Cash Flow': '...',
            'Present Value': '...',
            'Weight': '...',
            'Time × Weight': '...'
        })

    df = pd.DataFrame(cf_data)
    st.dataframe(df, use_container_width=True, height=400)

    st.info(f"💡 **Macaulay Duration** = Sum of (Time × Weight) = **{macaulay_dur:.3f} years**")

def show_interest_rate_risk():
    st.markdown('<div class="section-header">🎯 Interest Rate Risk</div>', unsafe_allow_html=True)

    st.markdown("""
    ### Understanding Bond Price Sensitivity

    Not all bonds respond equally to interest rate changes. Several factors affect sensitivity:
    """)

    st.markdown("### 📊 Compare Bond Sensitivities")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### Bond A")
        coupon_a = st.number_input("Coupon Rate (%)", value=3.0, step=0.5, key="risk_ca") / 100
        maturity_a = st.slider("Maturity (years)", 1, 30, 5, key="risk_ma")

    with col2:
        st.markdown("#### Bond B")
        coupon_b = st.number_input("Coupon Rate (%)", value=6.0, step=0.5, key="risk_cb") / 100
        maturity_b = st.slider("Maturity (years)", 1, 30, 15, key="risk_mb")

    with col3:
        st.markdown("#### Market Conditions")
        base_ytm = st.number_input("Base YTM (%)", value=5.0, step=0.5, key="risk_ytm") / 100
        yield_shock = st.slider("Yield Change (bp)", -200, 200, 100, 10, key="risk_shock") / 10000

    price_a = calculate_bond_price(1000, coupon_a, maturity_a, base_ytm, 2)
    duration_a = calculate_duration(1000, coupon_a, maturity_a, base_ytm, 2)
    mod_dur_a = calculate_modified_duration(duration_a, base_ytm, 2)

    price_b = calculate_bond_price(1000, coupon_b, maturity_b, base_ytm, 2)
    duration_b = calculate_duration(1000, coupon_b, maturity_b, base_ytm, 2)
    mod_dur_b = calculate_modified_duration(duration_b, base_ytm, 2)

    new_price_a = calculate_bond_price(1000, coupon_a, maturity_a, base_ytm + yield_shock, 2)
    new_price_b = calculate_bond_price(1000, coupon_b, maturity_b, base_ytm + yield_shock, 2)

    change_a = ((new_price_a - price_a) / price_a * 100) if price_a != 0 else np.nan
    change_b = ((new_price_b - price_b) / price_b * 100) if price_b != 0 else np.nan

    st.markdown("---")

    comparison = pd.DataFrame({
        'Metric': ['Initial Price', 'Duration', 'Modified Duration', 'New Price', 'Price Change (%)', 'Dollar Change'],
        'Bond A': [
            f'${price_a:.2f}',
            f'{duration_a:.3f} years',
            f'{mod_dur_a:.3f}',
            f'${new_price_a:.2f}',
            f'{change_a:.2f}%',
            f'${new_price_a - price_a:.2f}'
        ],
        'Bond B': [
            f'${price_b:.2f}',
            f'{duration_b:.3f} years',
            f'{mod_dur_b:.3f}',
            f'${new_price_b:.2f}',
            f'{change_b:.2f}%',
            f'${new_price_b - price_b:.2f}'
        ]
    })

    st.dataframe(comparison, use_container_width=True)

    if abs(change_a) > abs(change_b):
        more_sensitive = "Bond A"
        less_sensitive = "Bond B"
        more_dur, less_dur = duration_a, duration_b
    else:
        more_sensitive = "Bond B"
        less_sensitive = "Bond A"
        more_dur, less_dur = duration_b, duration_a

    st.markdown(f"""
    <div class="concept-box">
    <h4>Analysis</h4>
    <p><strong>{more_sensitive}</strong> is more sensitive to interest rate changes.</p>
    <p>This aligns with duration: the more sensitive bond has higher duration (<strong>{more_dur:.3f}</strong> vs <strong>{less_dur:.3f}</strong> years).</p>
    <p><strong>Key Insight:</strong> Lower coupons and longer maturities typically increase duration and interest rate risk.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Price Sensitivity Across Different Yield Changes")

    yield_changes = np.linspace(-0.03, 0.03, 50)
    prices_a = [calculate_bond_price(1000, coupon_a, maturity_a, base_ytm + dy, 2) for dy in yield_changes]
    prices_b = [calculate_bond_price(1000, coupon_b, maturity_b, base_ytm + dy, 2) for dy in yield_changes]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=yield_changes * 10000, y=prices_a, mode='lines',
        name=f'Bond A ({coupon_a:.1%} coupon, {maturity_a}y)'
    ))
    fig.add_trace(go.Scatter(
        x=yield_changes * 10000, y=prices_b, mode='lines',
        name=f'Bond B ({coupon_b:.1%} coupon, {maturity_b}y)'
    ))

    fig.add_trace(go.Scatter(x=[0], y=[price_a], mode='markers', name='Current Bond A', marker=dict(size=12)))
    fig.add_trace(go.Scatter(x=[0], y=[price_b], mode='markers', name='Current Bond B', marker=dict(size=12)))

    fig.update_layout(
        title="Bond Prices vs Yield Changes",
        xaxis_title="Yield Change (basis points)",
        yaxis_title="Bond Price ($)",
        height=500,
        hovermode='x unified'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.warning("⚠️ **Notice:** The steeper the curve, the higher the interest rate risk!")

def show_immunization():
    st.markdown('<div class="section-header">🛡️ Immunization</div>', unsafe_allow_html=True)

    st.markdown("""
    ### What is Immunization?

    **Immunization** is a strategy to shield a portfolio's value from interest rate movements.

    **Core Principle:** Match the duration of assets to the duration of liabilities.
    """)

    st.markdown("""
    <div class="concept-box">
    <h4>Why Immunization Works</h4>
    <p>When interest rates change, two effects occur:</p>
    <ol>
    <li><strong>Price effect:</strong> Bond prices move inverse to rates</li>
    <li><strong>Reinvestment effect:</strong> Coupon reinvestment rates change</li>
    </ol>
    <p>At the duration point, these effects <strong>approximately offset</strong> each other for small shocks.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 💼 Immunization Example")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Liability")
        liability_amount = st.number_input("Future Obligation ($)", value=10000, step=1000, key="imm_liab")
        liability_years = st.number_input("Years Until Payment", value=5.0, step=0.5, key="imm_years")

        st.markdown(f"""
        <div class="concept-box">
        <p><strong>Liability Duration:</strong> {liability_years:.1f} years</p>
        <p><strong>Required Asset Duration:</strong> {liability_years:.1f} years</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### Bond Portfolio")
        bond_coupon = st.number_input("Bond Coupon Rate (%)", value=6.0, step=0.5, key="imm_coup") / 100
        current_ytm = st.number_input("Current YTM (%)", value=8.0, step=0.5, key="imm_ytm") / 100

    st.markdown("#### Finding the Right Maturity")

    # Search maturities to match duration target
    test_maturities = np.linspace(max(0.5, liability_years), liability_years + 10, 100)
    durations = [calculate_duration(1000, bond_coupon, m, current_ytm, 2) for m in test_maturities]

    target_duration = liability_years
    closest_idx = int(np.nanargmin(np.abs(np.array(durations) - target_duration)))
    optimal_maturity = float(test_maturities[closest_idx])
    optimal_duration = float(durations[closest_idx])

    bond_price = calculate_bond_price(1000, bond_coupon, optimal_maturity, current_ytm, 2)
    pv_liability = liability_amount / ((1 + current_ytm) ** liability_years) if (1 + current_ytm) > 0 else np.nan
    num_bonds = pv_liability / bond_price if bond_price > 0 else np.nan

    st.markdown(f"""
    <div class="success-box">
    <h4>Immunization Strategy</h4>
    <p><strong>Buy bonds with maturity:</strong> {optimal_maturity:.2f} years</p>
    <p><strong>Duration of chosen bonds:</strong> {optimal_duration:.3f} years</p>
    <p><strong>Current bond price:</strong> ${bond_price:.2f}</p>
    <p><strong>Number of bonds needed:</strong> {num_bonds:.2f}</p>
    <p><strong>Total investment:</strong> ${num_bonds * bond_price:.2f}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📊 Immunization Performance Test")
    st.markdown("Let's see how the portfolio performs if interest rates change immediately:")

    rate_change = st.slider("Immediate Yield Change (bp)", -300, 300, 0, 25, key="imm_shock") / 10000
    new_ytm = current_ytm + rate_change

    # Portfolio value today after rate change
    new_bond_price = calculate_bond_price(1000, bond_coupon, optimal_maturity, new_ytm, 2)
    portfolio_value_today = num_bonds * new_bond_price if pd.notna(num_bonds) else np.nan

    # Future value at liability date: coupons reinvested + value of bonds at that date
    periods_per_year = 2
    n_periods = max(int(round(liability_years * periods_per_year)), 1)
    coupon_payment = 1000 * bond_coupon / periods_per_year

    # FV of coupons for ONE bond, reinvested to liability date at new_ytm
    fv_coupons_one = 0.0
    for t in range(1, n_periods + 1):
        time_to_liability_years = liability_years - (t / periods_per_year)
        if time_to_liability_years > 0:
            fv_coupons_one += coupon_payment * ((1 + new_ytm / periods_per_year) ** (time_to_liability_years * periods_per_year))
        else:
            fv_coupons_one += coupon_payment

    fv_coupons_total = (num_bonds * fv_coupons_one) if pd.notna(num_bonds) else np.nan

    remaining_time = optimal_maturity - liability_years
    remaining_time = max(0.0, float(remaining_time))

    bond_value_at_target = calculate_bond_price(1000, bond_coupon, remaining_time, new_ytm, 2)
    total_fv = (num_bonds * bond_value_at_target + fv_coupons_total) if pd.notna(num_bonds) else np.nan

    shortfall = liability_amount - total_fv if pd.notna(total_fv) else np.nan
    shortfall_pct = (shortfall / liability_amount) * 100 if liability_amount != 0 and pd.notna(shortfall) else np.nan

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Portfolio Value Today", f"${portfolio_value_today:.2f}" if pd.notna(portfolio_value_today) else "n/a")
    with col2:
        st.metric("Value at Liability Date", f"${total_fv:.2f}" if pd.notna(total_fv) else "n/a")
    with col3:
        st.metric("Shortfall", f"${shortfall:.2f}" if pd.notna(shortfall) else "n/a",
                  delta=(f"{shortfall_pct:.2f}%" if pd.notna(shortfall_pct) else None))

    if pd.notna(shortfall_pct):
        if abs(shortfall_pct) < 1:
            st.success("✅ Portfolio is well-immunized! Shortfall is minimal.")
        elif abs(shortfall_pct) < 5:
            st.info("ℹ️ Portfolio has some protection, but may need rebalancing.")
        else:
            st.warning("⚠️ Significant shortfall - portfolio needs rebalancing!")

    st.markdown("""
    <div class="concept-box">
    <h4>💡 Key Points About Immunization</h4>
    <ul>
    <li><strong>Duration matching</strong> protects against small, immediate rate changes</li>
    <li><strong>Rebalancing</strong> is needed as time passes and rates change</li>
    <li><strong>Convexity</strong> provides additional protection (positive convexity is desirable)</li>
    <li><strong>Multiple liabilities</strong> require cash flow matching or dedication strategies</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

def show_convexity():
    st.markdown('<div class="section-header">🌊 Convexity</div>', unsafe_allow_html=True)

    st.markdown("""
    ### Why Duration Isn't Enough

    **Duration** provides a linear approximation of the price-yield relationship.
    But the actual relationship is **curved** (convex).

    **Convexity** measures this curvature.
    """)

    st.markdown("""
    <div class="formula-box">
    <strong>Price Change with Convexity:</strong><br><br>
    ΔP/P ≈ -D* × Δy + ½ × C × (Δy)²<br><br>
    Where:<br>
    D* = Modified Duration<br>
    C = Convexity<br>
    Δy = Change in yield
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📊 Visualizing Convexity")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("#### Bond Parameters")
        fv_conv = st.number_input("Face Value ($)", value=1000, step=100, key="conv_fv")
        cr_conv = st.number_input("Coupon Rate (%)", value=6.0, step=0.5, key="conv_cr") / 100
        mat_conv = st.slider("Maturity (years)", 1, 30, 10, key="conv_mat")
        ytm_conv = st.number_input("YTM (%)", value=6.0, step=0.5, key="conv_ytm") / 100

    with col2:
        price_conv = calculate_bond_price(fv_conv, cr_conv, mat_conv, ytm_conv, 2)
        duration_conv = calculate_duration(fv_conv, cr_conv, mat_conv, ytm_conv, 2)
        mod_dur_conv = calculate_modified_duration(duration_conv, ytm_conv, 2)
        convexity_val = calculate_convexity(fv_conv, cr_conv, mat_conv, ytm_conv, 2)

        st.metric("Convexity", f"{convexity_val:.2f}")
        st.metric("Modified Duration", f"{mod_dur_conv:.3f}")
        st.metric("Current Price", f"${price_conv:.2f}")

    y_low = max(0.0001, ytm_conv - 0.04)
    y_high = ytm_conv + 0.04
    yield_range = np.linspace(y_low, y_high, 100)
    actual_prices = [calculate_bond_price(fv_conv, cr_conv, mat_conv, y, 2) for y in yield_range]

    duration_prices = [price_conv * (1 + price_change_duration(mod_dur_conv, y - ytm_conv)) for y in yield_range]
    convexity_prices = [price_conv * (1 + price_change_duration_convexity(mod_dur_conv, convexity_val, y - ytm_conv)) for y in yield_range]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=yield_range * 100, y=actual_prices, mode='lines', name='Actual Price'))
    fig.add_trace(go.Scatter(x=yield_range * 100, y=duration_prices, mode='lines', name='Duration Approximation', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=yield_range * 100, y=convexity_prices, mode='lines', name='Duration + Convexity', line=dict(dash='dot')))

    fig.add_trace(go.Scatter(x=[ytm_conv * 100], y=[price_conv], mode='markers', name='Current Price', marker=dict(size=15)))

    fig.update_layout(
        title="Price-Yield Relationship: Actual vs Approximations",
        xaxis_title="Yield to Maturity (%)",
        yaxis_title="Bond Price ($)",
        height=500,
        hovermode='x unified'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <div class="concept-box">
    <h4>📖 Interpretation</h4>
    <ul>
    <li><strong>Actual:</strong> True price-yield relationship (curved)</li>
    <li><strong>Duration only:</strong> Linear approximation (less accurate for large moves)</li>
    <li><strong>Duration + Convexity:</strong> Better approximation (captures curvature)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🎯 Approximation Accuracy")

    test_yield_change = st.slider("Test Yield Change (bp)", -300, 300, 100, 25, key="conv_test") / 10000

    new_ytm_test = max(0.0001, ytm_conv + test_yield_change)
    actual_new_price = calculate_bond_price(fv_conv, cr_conv, mat_conv, new_ytm_test, 2)
    actual_pct_change = ((actual_new_price - price_conv) / price_conv * 100) if price_conv != 0 else np.nan

    duration_pct_change = price_change_duration(mod_dur_conv, test_yield_change) * 100
    convexity_pct_change = price_change_duration_convexity(mod_dur_conv, convexity_val, test_yield_change) * 100

    duration_error = abs(duration_pct_change - actual_pct_change) if pd.notna(actual_pct_change) else np.nan
    convexity_error = abs(convexity_pct_change - actual_pct_change) if pd.notna(actual_pct_change) else np.nan

    comparison_df = pd.DataFrame({
        'Method': ['Actual Change', 'Duration Only', 'Duration + Convexity'],
        'Price Change (%)': [actual_pct_change, duration_pct_change, convexity_pct_change],
        'Error (%)': [0, duration_error, convexity_error]
    })

    st.dataframe(
        comparison_df.style.format({'Price Change (%)': '{:.4f}%', 'Error (%)': '{:.4f}%'}).background_gradient(
            subset=['Error (%)'], cmap='RdYlGn_r'
        ),
        use_container_width=True
    )

    improvement = ((duration_error - convexity_error) / duration_error * 100) if (pd.notna(duration_error) and duration_error > 0) else 0
    st.success(f"✅ Adding convexity improves accuracy by **{improvement:.1f}%**")

    st.markdown("---")

    st.markdown("### 💎 The Value of Positive Convexity")

    st.markdown("""
    <div class="concept-box">
    <h4>Why Positive Convexity is Desirable</h4>
    <p>Bonds with positive convexity gain more from yield decreases than they lose from yield increases.</p>
    <ul>
    <li><strong>Asymmetric payoff:</strong> Upside > Downside (for equal-magnitude yield moves)</li>
    <li><strong>Portfolio protection:</strong> Better performance under rate volatility</li>
    <li><strong>Callable bonds:</strong> Can exhibit negative convexity</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    symmetric_changes = np.array([-200, -100, 0, 100, 200]) / 10000
    price_changes = []
    for dy in symmetric_changes:
        new_p = calculate_bond_price(fv_conv, cr_conv, mat_conv, max(0.0001, ytm_conv + dy), 2)
        pct_change = ((new_p - price_conv) / price_conv * 100) if price_conv != 0 else np.nan
        price_changes.append(pct_change)

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=[f'{int(dy * 10000):+d} bp' for dy in symmetric_changes], y=price_changes))
    fig2.update_layout(
        title="Asymmetric Price Response (Positive Convexity)",
        xaxis_title="Yield Change",
        yaxis_title="Price Change (%)",
        height=400
    )
    st.plotly_chart(fig2, use_container_width=True)

    if pd.notna(price_changes[0]) and pd.notna(price_changes[-1]):
        st.info(
            f"💡 Notice: The gain from -200bp ({price_changes[0]:.2f}%) often differs from the loss from +200bp ({price_changes[-1]:.2f}%)."
        )

def show_active_strategies():
    st.markdown('<div class="section-header">📊 Active Bond Management Strategies</div>', unsafe_allow_html=True)

    st.markdown("""
    Active bond management seeks to outperform passive strategies through:
    - Interest rate forecasting
    - Sector rotation
    - Security selection
    - Trading strategies
    """)

    st.markdown("### 🔄 Bond Swap Strategies")

    tab1, tab2, tab3, tab4 = st.tabs(["Substitution Swap", "Intermarket Swap",
                                       "Rate Anticipation", "Pure Yield Pickup"])

    with tab1:
        st.markdown("""
        #### Substitution Swap

        **Strategy:** Exchange one bond for another with similar characteristics but better pricing.

        **When to use:**
        - You identify a mispriced bond
        - Two bonds with similar risk/maturity have different yields
        - Temporary market inefficiency
        """)

        st.markdown("""
        <div class="concept-box">
        <h4>Example</h4>
        <p><strong>Current Bond:</strong> 10-year, AA-rated corporate, 5% yield</p>
        <p><strong>Swap into:</strong> 10-year, AA-rated corporate, 5.25% yield</p>
        <p><strong>Rationale:</strong> Same risk/maturity, higher yield = potential mispricing</p>
        <p><strong>Expected gain:</strong> 25 basis points annually (if risks truly equivalent)</p>
        </div>
        """, unsafe_allow_html=True)

        st.warning("⚠️ **Risk:** The yield difference may reflect liquidity differences or hidden credit risk")

    with tab2:
        st.markdown("""
        #### Intermarket Swap

        **Strategy:** Shift between different segments of the bond market.

        **Examples:**
        - Corporate bonds → Government bonds
        - Long-term → Short-term
        - Investment grade → High yield
        """)

        st.markdown("""
        <div class="concept-box">
        <h4>Example Scenario</h4>
        <p><strong>Market View:</strong> Economic slowdown expected</p>
        <p><strong>Action:</strong> Swap corporate bonds for Treasuries</p>
        <p><strong>Rationale:</strong> Credit spreads likely to widen in recession</p>
        <p><strong>Flight to quality:</strong> Treasuries may outperform</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("##### Credit Spread Simulator")

        col1, col2 = st.columns(2)

        with col1:
            treasury_yield = st.number_input("Treasury Yield (%)", value=4.0, step=0.25, key="swap_ty") / 100
            initial_spread = st.number_input("Initial Corporate Spread (bp)", value=150, step=25, key="swap_spread") / 10000

        with col2:
            spread_change = st.slider("Expected Spread Change (bp)", -100, 200, 50, 10, key="swap_change") / 10000
            holding_period = st.number_input("Holding Period (months)", value=6, step=1, key="swap_period")

        corporate_yield = treasury_yield + initial_spread
        new_spread = initial_spread + spread_change
        new_corporate_yield = treasury_yield + new_spread

        corporate_duration = 7.0  # illustrative
        corporate_price_change = -corporate_duration * spread_change
        relative_return = corporate_price_change * 100

        st.metric("Relative Performance", f"{relative_return:.2f}%", delta="Corporate vs Treasury")

        if relative_return < 0:
            st.error("❌ Corporate bonds underperform due to spread widening")
        else:
            st.success("✅ Corporate bonds outperform due to spread tightening")

    with tab3:
        st.markdown("""
        #### Rate Anticipation Swap

        **Strategy:** Adjust portfolio duration based on interest rate forecasts.

        **Rate Expectations:**
        - **Rates falling** → Increase duration (buy long-term bonds)
        - **Rates rising** → Decrease duration (buy short-term bonds)
        """)

        st.markdown("##### Duration Adjustment Calculator")

        col1, col2 = st.columns(2)

        with col1:
            current_duration = st.number_input("Current Portfolio Duration", value=5.0, step=0.5, key="ant_dur")
            portfolio_value = st.number_input("Portfolio Value ($M)", value=10.0, step=1.0, key="ant_val")

        with col2:
            rate_forecast = st.select_slider(
                "Rate Forecast",
                options=["Strong Decline", "Decline", "Stable", "Rise", "Strong Rise"],
                value="Stable",
                key="ant_forecast"
            )
            expected_change = st.number_input("Expected Yield Change (bp)", value=-50, step=25, key="ant_change") / 10000

        if rate_forecast == "Strong Decline":
            target_duration = current_duration * 1.5
            action = "Significantly increase"
        elif rate_forecast == "Decline":
            target_duration = current_duration * 1.25
            action = "Increase"
        elif rate_forecast == "Stable":
            target_duration = current_duration
            action = "Maintain"
        elif rate_forecast == "Rise":
            target_duration = current_duration * 0.75
            action = "Decrease"
        else:
            target_duration = current_duration * 0.5
            action = "Significantly decrease"

        expected_return = -current_duration * expected_change * 100
        optimal_return = -target_duration * expected_change * 100

        st.markdown(f"""
        <div class="concept-box">
        <h4>Recommendation</h4>
        <p><strong>Action:</strong> {action} duration</p>
        <p><strong>Current Duration:</strong> {current_duration:.2f} years</p>
        <p><strong>Target Duration:</strong> {target_duration:.2f} years</p>
        <hr>
        <p><strong>If forecast correct:</strong></p>
        <p>Current portfolio return: {expected_return:.2f}%</p>
        <p>Optimized portfolio return: {optimal_return:.2f}%</p>
        <p><strong>Additional return:</strong> {optimal_return - expected_return:.2f}%</p>
        <p><strong>Dollar gain:</strong> ${(optimal_return - expected_return) * portfolio_value / 100:.2f}M</p>
        </div>
        """, unsafe_allow_html=True)

        st.warning("⚠️ **Risk:** Interest rate forecasting is notoriously difficult!")

    with tab4:
        st.markdown("""
        #### Pure Yield Pickup Swap

        **Strategy:** Swap into higher-yielding bonds to increase income.

        **Common approach:**
        - Sell shorter-maturity bonds
        - Buy longer-maturity bonds
        - Accept higher duration risk for higher yield
        """)

        st.markdown("##### Yield Pickup Calculator")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Current Bond**")
            current_maturity = st.slider("Maturity (years)", 1, 10, 3, key="yp_curr_mat")
            current_yield = st.number_input("Yield (%)", value=3.5, step=0.25, key="yp_curr_yield") / 100

        with col2:
            st.markdown("**Target Bond**")
            target_maturity = st.slider("Maturity (years)", 1, 30, 10, key="yp_targ_mat")
            target_yield = st.number_input("Yield (%)", value=5.0, step=0.25, key="yp_targ_yield") / 100

        yield_pickup_bp = (target_yield - current_yield) * 10000

        current_dur = current_maturity * 0.9
        target_dur = target_maturity * 0.85
        duration_increase = target_dur - current_dur

        if duration_increase > 0:
            breakeven_rate = yield_pickup_bp / (duration_increase * 10000)
        else:
            breakeven_rate = 0.0

        st.markdown(f"""
        <div class="concept-box">
        <h4>Analysis</h4>
        <p><strong>Yield Pickup:</strong> {yield_pickup_bp:.0f} basis points</p>
        <p><strong>Additional Annual Income:</strong> ${yield_pickup_bp * 10:.0f} per $1M invested (rule-of-thumb)</p>
        <hr>
        <p><strong>Trade-off:</strong></p>
        <p>Duration increases by {duration_increase:.2f} years</p>
        <p>Higher interest rate risk</p>
        <hr>
        <p><strong>Breakeven Analysis:</strong></p>
        <p>If rates rise by <strong>{breakeven_rate:.2f}%</strong>, the capital loss may offset the yield pickup</p>
        </div>
        """, unsafe_allow_html=True)

        if breakeven_rate < 0.5:
            st.error("❌ High risk: Small rate increase could eliminate yield benefit")
        elif breakeven_rate < 1.0:
            st.warning("⚠️ Moderate risk: Consider rate outlook")
        else:
            st.success("✅ Reasonable cushion against rate increases")

    st.markdown("---")

    st.markdown("### 🔭 Horizon Analysis")

    st.markdown("""
    **Horizon analysis** forecasts bond returns over a specific investment period based on:
    - Expected yield curve changes
    - Reinvestment rate assumptions
    - Holding period
    """)

    st.markdown("""
    <div class="concept-box">
    <h4>Steps in Horizon Analysis</h4>
    <ol>
    <li>Forecast yield curve at end of horizon</li>
    <li>Calculate expected bond price at horizon</li>
    <li>Add coupon income (with reinvestment)</li>
    <li>Compute total return</li>
    <li>Compare to alternatives</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def show_quiz():
    st.markdown('<div class="section-header">✅ Test Your Knowledge</div>', unsafe_allow_html=True)

    if 'ch11_score' not in st.session_state:
        st.session_state.ch11_score = 0
    if 'ch11_submitted' not in st.session_state:
        st.session_state.ch11_submitted = set()

    st.markdown("### Question 1: Duration Basics")
    st.markdown("A zero-coupon bond with 10 years to maturity has a duration of:")

    q1 = st.radio(
        "",
        ["A) Less than 10 years", "B) Exactly 10 years",
         "C) More than 10 years", "D) Cannot be determined"],
        key="q1",
        label_visibility="collapsed"
    )

    if st.button("Submit Answer", key="q1_btn") and "q1" not in st.session_state.ch11_submitted:
        st.session_state.ch11_submitted.add("q1")
        if q1 == "B) Exactly 10 years":
            st.success("✅ Correct! Zero-coupon bond duration equals its maturity.")
            st.session_state.ch11_score += 1
        else:
            st.error("❌ Incorrect. For zero-coupon bonds, duration = maturity.")

    st.markdown("---")

    st.markdown("### Question 2: Duration and Interest Rates")
    st.markdown("Which bond has the HIGHEST duration?")

    q2 = st.radio(
        "",
        ["A) 10-year, 8% coupon", "B) 10-year, 4% coupon",
         "C) 20-year, 8% coupon", "D) 5-year, 4% coupon"],
        key="q2",
        label_visibility="collapsed"
    )

    if st.button("Submit Answer", key="q2_btn") and "q2" not in st.session_state.ch11_submitted:
        st.session_state.ch11_submitted.add("q2")
        if q2 == "C) 20-year, 8% coupon":
            st.success("✅ Correct! Longer maturity dominates, even with higher coupon.")
            st.session_state.ch11_score += 1
        else:
            st.error("❌ Incorrect. Longer maturity generally means higher duration.")

    st.markdown("---")

    st.markdown("### Question 3: Immunization")
    st.markdown("To immunize a portfolio against a single liability, you should:")

    q3 = st.radio(
        "",
        ["A) Match the maturity of assets and liabilities",
         "B) Match the duration of assets and liabilities",
         "C) Maximize the portfolio's convexity",
         "D) Invest in zero-coupon bonds only"],
        key="q3",
        label_visibility="collapsed"
    )

    if st.button("Submit Answer", key="q3_btn") and "q3" not in st.session_state.ch11_submitted:
        st.session_state.ch11_submitted.add("q3")
        if q3 == "B) Match the duration of assets and liabilities":
            st.success("✅ Correct! Duration matching is the key to immunization.")
            st.session_state.ch11_score += 1
        else:
            st.error("❌ Incorrect. Immunization requires duration matching.")

    st.markdown("---")

    st.markdown("### Question 4: Convexity")
    st.markdown("Positive convexity is desirable because:")

    q4 = st.radio(
        "",
        ["A) It increases duration",
         "B) Bonds gain more from yield decreases than they lose from yield increases",
         "C) It reduces interest rate risk to zero",
         "D) It guarantees positive returns"],
        key="q4",
        label_visibility="collapsed"
    )

    if st.button("Submit Answer", key="q4_btn") and "q4" not in st.session_state.ch11_submitted:
        st.session_state.ch11_submitted.add("q4")
        if q4 == "B) Bonds gain more from yield decreases than they lose from yield increases":
            st.success("✅ Correct! Positive convexity creates asymmetric returns.")
            st.session_state.ch11_score += 1
        else:
            st.error("❌ Incorrect. Positive convexity means asymmetric price response.")

    st.markdown("---")

    st.markdown("### Question 5: Modified Duration")
    st.markdown("A bond has a modified duration of 6. If yields increase by 1%, the bond price will:")

    q5 = st.radio(
        "",
        ["A) Increase by 6%", "B) Decrease by 6%",
         "C) Increase by approximately 6%", "D) Decrease by approximately 6%"],
        key="q5",
        label_visibility="collapsed"
    )

    if st.button("Submit Answer", key="q5_btn") and "q5" not in st.session_state.ch11_submitted:
        st.session_state.ch11_submitted.add("q5")
        if q5 == "D) Decrease by approximately 6%":
            st.success("✅ Correct! ΔP/P ≈ -D* × Δy = -6 × 0.01 = -6%")
            st.session_state.ch11_score += 1
        else:
            st.error("❌ Incorrect. ΔP/P ≈ -Modified Duration × Yield Change")

    st.markdown("---")

    if len(st.session_state.ch11_submitted) > 0:
        score_pct = (st.session_state.ch11_score / len(st.session_state.ch11_submitted)) * 100

        st.markdown(f"""
        <div class="concept-box">
        <h2>Your Score: {st.session_state.ch11_score} / {len(st.session_state.ch11_submitted)}</h2>
        <h3>{score_pct:.0f}%</h3>
        </div>
        """, unsafe_allow_html=True)

        if score_pct >= 80:
            st.success("🎉 Excellent! You have a strong grasp of bond portfolio management.")
        elif score_pct >= 60:
            st.info("👍 Good work! Review the concepts where you missed questions.")
        else:
            st.warning("📚 Keep studying! Review duration, immunization, and convexity.")

    if st.button("Reset Quiz", key="reset_quiz"):
        st.session_state.ch11_score = 0
        st.session_state.ch11_submitted = set()
        st.rerun()

if __name__ == "__main__":
    main()
