import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

# -----------------------------------------------------------------------------
# Page configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Bond Pricing & Yields",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# Custom CSS (kept generic; no copyrighted assets)
# -----------------------------------------------------------------------------
st.markdown(
    """
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
    .quiz-correct {
        background-color: #97BC62;
        padding: 1rem;
        border-radius: 8px;
        color: white;
        font-weight: bold;
    }
    .quiz-incorrect {
        background-color: #F96167;
        padding: 1rem;
        border-radius: 8px;
        color: white;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# Disclaimers (copyright-safe framing)
# -----------------------------------------------------------------------------
def render_disclaimer():
    st.sidebar.caption(
        "Unofficial educational tool for learning bond pricing, yields, and credit risk. "
        "Not affiliated with or endorsed by any authors or publishers. "
        "No publisher figures/slides/tables are reproduced."
    )

def render_footer():
    st.markdown("---")
    st.caption(
        "Unofficial educational tool for bond pricing and yield concepts. "
        "Not affiliated with or endorsed by any authors/publishers."
    )

# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------
def calculate_bond_price(face_value, coupon_rate, years_to_maturity, ytm, frequency=2):
    """Calculate bond price using PV of cash flows."""
    if years_to_maturity <= 0:
        return face_value

    n_periods = int(round(years_to_maturity * frequency))
    n_periods = max(n_periods, 1)

    coupon_payment = (face_value * coupon_rate) / frequency
    discount_rate = ytm / frequency

    if abs(discount_rate) < 1e-12:
        pv_coupons = coupon_payment * n_periods
    else:
        pv_coupons = coupon_payment * (1 - (1 + discount_rate) ** (-n_periods)) / discount_rate

    pv_face = face_value / ((1 + discount_rate) ** n_periods)
    return pv_coupons + pv_face

def calculate_current_yield(coupon_rate, face_value, price):
    """Current yield = annual coupon / price."""
    annual_coupon = coupon_rate * face_value
    return annual_coupon / price if price != 0 else np.nan

def ytm_approximation(price, face_value, coupon_rate, years_to_maturity):
    """
    Approximate YTM:
    (C + (F - P)/n) / ((F + P)/2)
    """
    if years_to_maturity <= 0:
        return np.nan
    annual_coupon = coupon_rate * face_value
    return (annual_coupon + (face_value - price) / years_to_maturity) / ((face_value + price) / 2)

def calculate_duration(face_value, coupon_rate, years, ytm, frequency=2):
    """Macaulay duration (years) for fixed-rate bond."""
    n = int(round(years * frequency))
    n = max(n, 1)
    c = (face_value * coupon_rate) / frequency
    r = ytm / frequency

    weighted_pv = 0.0
    total_pv = 0.0

    for t in range(1, n + 1):
        cf = c
        if t == n:
            cf += face_value
        pv = cf / ((1 + r) ** t) if abs(r) > 1e-12 else cf
        time_years = t / frequency
        weighted_pv += time_years * pv
        total_pv += pv

    return weighted_pv / total_pv if total_pv != 0 else np.nan

def calculate_modified_duration(macaulay_duration, ytm, frequency=2):
    """Modified duration."""
    return macaulay_duration / (1 + ytm / frequency)

def calculate_convexity(face_value, coupon_rate, years, ytm, frequency=2):
    """Convexity (standard discrete approximation)."""
    n = int(round(years * frequency))
    n = max(n, 1)
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
        pv = cf / ((1 + r) ** t) if abs(r) > 1e-12 else cf
        convexity_sum += pv * t * (t + 1)

    return convexity_sum / (price * (1 + r) ** 2 * frequency ** 2)

def price_change_duration(modified_duration, delta_yield):
    """ΔP/P ≈ -D* Δy"""
    return -modified_duration * delta_yield

def price_change_duration_convexity(modified_duration, convexity, delta_yield):
    """ΔP/P ≈ -D* Δy + 0.5 C (Δy)^2"""
    return (-modified_duration * delta_yield) + 0.5 * convexity * (delta_yield ** 2)

# -----------------------------------------------------------------------------
# Pages
# -----------------------------------------------------------------------------
def show_home():
    st.markdown('<div class="main-header">💰 Bond Pricing & Yields</div>', unsafe_allow_html=True)
    st.markdown(
        '<p style="text-align:center; font-size:1.15rem; color:#666;">Interactive practice: pricing, yield measures, yield curves, and credit spreads</p>',
        unsafe_allow_html=True,
    )
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class="concept-box">
            <h3 style="color:#028090;">📚 Learn Concepts</h3>
            <p>Bond cash flows, pricing intuition, and yield measures with clear definitions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="concept-box">
            <h3 style="color:#028090;">📊 Visualize</h3>
            <p>See price–yield curves, maturity effects, and term structure shapes.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class="concept-box">
            <h3 style="color:#028090;">🧮 Practice</h3>
            <p>Use calculators and quizzes to build speed and accuracy.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-header">📋 Overview</div>', unsafe_allow_html=True)
    st.markdown(
        """
This app is an **independent educational tool** for learning bond pricing and yield concepts.
It is **not affiliated with or endorsed** by any textbook authors or publishers.

### Topics in this app
- Bond cash flows and present value pricing  
- Yield measures: current yield, (approx.) YTM, (approx.) YTC  
- Price–yield relationship and interest-rate sensitivity  
- Default risk, ratings intuition, and credit spreads  
- Yield curve interpretation and expectations logic  

### 🎯 Learning objectives
By the end, you should be able to:
- Price fixed-rate bonds using PV methods  
- Explain why prices and yields move inversely  
- Compute and interpret key yield measures  
- Compare bonds across maturity/coupon structures  
- Interpret common yield curve shapes and the intuition behind them  
        """
    )
    st.info("💡 Tip: Use the Calculator page to verify your homework computations quickly, then use the charts to build intuition.")

def show_bond_basics():
    st.markdown('<div class="section-header">📖 Bond Basics</div>', unsafe_allow_html=True)

    st.markdown(
        """
### What is a bond?
A **bond** is a contract where the issuer promises to pay:
- periodic **coupon** payments (for coupon bonds), and
- **principal** (face value) at **maturity**.

You can think of it as a loan you make to the issuer.
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="concept-box">
            <h4>Key terms</h4>
            <ul>
              <li><span class="highlight">Face value (par)</span>: principal repaid at maturity (often $1,000)</li>
              <li><span class="highlight">Coupon rate</span>: annual coupon / face value</li>
              <li><span class="highlight">Coupon payment</span>: coupon rate × face value ÷ payments per year</li>
              <li><span class="highlight">Maturity</span>: date principal is repaid</li>
              <li><span class="highlight">Zero-coupon bond</span>: no coupons; issued at discount</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="concept-box">
            <h4>Example</h4>
            <p>Face value = $1,000, coupon rate = 6%, maturity = 10 years, semiannual coupons.</p>
            <ul>
              <li>Coupon per half-year = $1,000 × 0.06 ÷ 2 = $30</li>
              <li>Final payment includes principal: $1,000</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 🧾 Accrued interest (simple practice)")

    st.markdown(
        """
When a bond trades between coupon dates, the buyer typically compensates the seller for **accrued interest**
since the last coupon date. This is a simplified day-count practice tool.
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        face_value = st.number_input("Face Value ($)", value=1000, step=100, key="ai_fv")
        coupon_rate = st.number_input("Annual Coupon Rate (%)", value=6.0, step=0.5, key="ai_cr") / 100
        days_since_payment = st.number_input("Days Since Last Coupon", value=45, step=1, key="ai_days")
        days_in_period = st.number_input("Days in Coupon Period", value=182, step=1, key="ai_period")
    with col2:
        semi_annual_coupon = (face_value * coupon_rate) / 2
        accrued_interest = semi_annual_coupon * (days_since_payment / days_in_period) if days_in_period > 0 else np.nan

        st.markdown(
            f"""
            <div class="formula-box">
            <p><strong>Semi-annual coupon:</strong> ${semi_annual_coupon:.2f}</p>
            <p><strong>Accrued interest:</strong> ${accrued_interest:.2f}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("Note: Real markets use specific day-count conventions. This is for intuition and practice.")

def show_bond_pricing():
    st.markdown('<div class="section-header">💵 Bond Pricing</div>', unsafe_allow_html=True)
    st.markdown(
        """
### Pricing principle
A bond’s price is the **present value** of its future cash flows, discounted at the market-required yield.
        """
    )

    st.markdown(
        """
        <div class="formula-box">
        <strong>Bond price (discrete compounding):</strong><br><br>
        Price = Σ [C / (1 + r)ᵗ] + [F / (1 + r)ᴺ]
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### 📊 Interactive bond price calculator")

    col1, col2 = st.columns([1, 2])
    with col1:
        face_value = st.number_input("Face Value ($)", value=1000, step=100, key="bp_fv")
        coupon_rate = st.number_input("Coupon Rate (%)", value=5.0, step=0.5, key="bp_cr") / 100
        maturity = st.slider("Years to Maturity", 1, 30, 10, key="bp_mat")
        ytm = st.number_input("Yield to Maturity (%)", value=8.0, step=0.5, key="bp_ytm") / 100
        frequency = st.selectbox(
            "Payment Frequency",
            [1, 2, 4],
            format_func=lambda x: {1: "Annual", 2: "Semi-annual", 4: "Quarterly"}[x],
            key="bp_freq",
        )

    with col2:
        price = calculate_bond_price(face_value, coupon_rate, maturity, ytm, frequency)
        status = "Premium" if price > face_value else "Discount" if price < face_value else "Par"
        cy = calculate_current_yield(coupon_rate, face_value, price)

        st.markdown(
            f"""
            <div class="concept-box">
            <h3>Bond Price: ${price:.2f}</h3>
            <p style="font-size:1.15rem;">Trading at: <strong>{status}</strong></p>
            <hr>
            <p><strong>Annual coupon:</strong> ${face_value * coupon_rate:.2f}</p>
            <p><strong>Current yield:</strong> {cy:.2%}</p>
            <p><strong>YTM (input):</strong> {ytm:.2%}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        n_periods = int(maturity * frequency)
        coupon_payment = (face_value * coupon_rate) / frequency
        st.markdown("#### Cash-flow summary")
        st.markdown(f"- {n_periods} coupon payments of ${coupon_payment:.2f}")
        st.markdown(f"- Final principal repayment of ${face_value:.2f}")

    st.markdown("---")
    st.markdown("### 📈 Price–yield relationship (inverse)")
    st.markdown("Bond prices generally **fall when yields rise**, and **rise when yields fall** (holding other features fixed).")

    yields = np.linspace(0.01, 0.15, 60)
    curve_prices = [calculate_bond_price(1000, 0.05, 10, y, 2) for y in yields]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=yields * 100, y=curve_prices, mode="lines", name="Example bond price"))
    fig.add_trace(go.Scatter(x=[ytm * 100], y=[price], mode="markers", name="Your bond", marker=dict(size=12)))
    fig.update_layout(
        title="Bond Price vs Yield",
        xaxis_title="Yield to Maturity (%)",
        yaxis_title="Bond Price ($)",
        hovermode="x unified",
        height=450,
    )
    st.plotly_chart(fig, use_container_width=True)
    st.info("💡 Intuition: higher discount rates reduce PV of future cash flows.")

    st.markdown("---")
    st.markdown("### ⏰ Maturity and sensitivity (intuition)")
    st.markdown("Longer maturities typically imply larger price moves for the same yield shock.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Shorter maturity (4 years)")
        short_price = calculate_bond_price(1000, 0.05, 4, ytm, 2)
        short_5 = calculate_bond_price(1000, 0.05, 4, 0.05, 2)
        short_11 = calculate_bond_price(1000, 0.05, 4, 0.11, 2)
        st.metric("Price at your YTM", f"${short_price:.2f}")
        st.markdown(f"- At 5%: ${short_5:.2f}\n- At 11%: ${short_11:.2f}\n- Range: ${short_5 - short_11:.2f}")
    with col2:
        st.markdown("#### Longer maturity (30 years)")
        long_price = calculate_bond_price(1000, 0.05, 30, ytm, 2)
        long_5 = calculate_bond_price(1000, 0.05, 30, 0.05, 2)
        long_11 = calculate_bond_price(1000, 0.05, 30, 0.11, 2)
        st.metric("Price at your YTM", f"${long_price:.2f}")
        st.markdown(f"- At 5%: ${long_5:.2f}\n- At 11%: ${long_11:.2f}\n- Range: ${long_5 - long_11:.2f}")

    st.warning("⚠️ Longer maturity generally increases interest-rate risk (larger price swings).")

def show_yield_calculations():
    st.markdown('<div class="section-header">📊 Yield Calculations</div>', unsafe_allow_html=True)
    st.markdown("Different yield measures answer different questions about return and pricing.")

    tab1, tab2, tab3, tab4 = st.tabs(["Current Yield", "YTM (Approx.)", "YTC (Approx.)", "Realized Return"])

    with tab1:
        st.markdown("### Current yield")
        st.markdown(
            """
            <div class="formula-box">
            Current Yield = Annual Coupon / Price
            </div>
            """,
            unsafe_allow_html=True,
        )
        col1, col2 = st.columns(2)
        with col1:
            coupon = st.number_input("Annual Coupon ($)", value=80.0, step=5.0, key="cy_coupon")
            price = st.number_input("Bond Price ($)", value=950.0, step=10.0, key="cy_price")
        with col2:
            cy = coupon / price if price != 0 else np.nan
            st.markdown(
                f"""
                <div class="concept-box">
                <h3>Current Yield: {cy:.2%}</h3>
                <p>${coupon:.2f} / ${price:.2f} = {cy:.2%}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.info("💡 Current yield ignores capital gain/loss and time value; useful for quick comparisons only.")

    with tab2:
        st.markdown("### Yield to maturity (approximation)")
        st.caption("Exact YTM typically requires numerical solving; this uses a common approximation formula.")

        col1, col2 = st.columns(2)
        with col1:
            p = st.number_input("Price ($)", value=1100.0, step=10.0, key="ytm_p")
            f = st.number_input("Face Value ($)", value=1000.0, step=100.0, key="ytm_f")
            cr = st.number_input("Coupon Rate (%)", value=8.0, step=0.5, key="ytm_cr") / 100
            n = st.number_input("Years to Maturity", value=10, step=1, key="ytm_n")
        with col2:
            ytm_a = ytm_approximation(p, f, cr, n)
            cy = (cr * f) / p if p != 0 else np.nan
            status = "Premium" if p > f else "Discount" if p < f else "Par"
            st.markdown(
                f"""
                <div class="concept-box">
                <h3>Approx. YTM: {ytm_a:.2%}</h3>
                <p><strong>Current yield:</strong> {cy:.2%}</p>
                <p><strong>Status:</strong> {status}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown(
            """
**Common relationships (intuition):**
- Premium: YTM < Current Yield < Coupon Rate  
- Discount: YTM > Current Yield > Coupon Rate  
- Par: YTM = Current Yield = Coupon Rate  
            """
        )

    with tab3:
        st.markdown("### Yield to call (approximation)")
        st.caption("Callable bonds can be redeemed early by the issuer. YTC uses call date/price instead of maturity/face.")

        col1, col2 = st.columns(2)
        with col1:
            p = st.number_input("Price ($)", value=1150.0, step=10.0, key="ytc_p")
            call_price = st.number_input("Call Price ($)", value=1050.0, step=10.0, key="ytc_cp")
            annual_coupon = st.number_input("Annual Coupon ($)", value=90.0, step=5.0, key="ytc_c")
            years_to_call = st.number_input("Years to Call", value=5, step=1, key="ytc_n")
        with col2:
            if years_to_call <= 0:
                ytc = np.nan
            else:
                ytc = (annual_coupon + (call_price - p) / years_to_call) / ((call_price + p) / 2)

            st.markdown(
                f"""
                <div class="concept-box">
                <h3>Approx. YTC: {ytc:.2%}</h3>
                <p>Interpretation: yield if called in {years_to_call} years at ${call_price:.2f}.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.warning("⚠️ Premium callable bonds may be called when rates fall, creating reinvestment risk.")

    with tab4:
        st.markdown("### Realized compound return (with reinvestment assumption)")
        st.markdown(
            """
Realized return depends on:
- the holding period,
- the reinvestment rate on coupons, and
- the bond’s sale price at the end of the holding period.
            """
        )

        col1, col2 = st.columns(2)
        with col1:
            initial = st.number_input("Initial Investment ($)", value=1000.0, step=100.0, key="rr_init")
            coupon = st.number_input("Annual Coupon ($)", value=80.0, step=5.0, key="rr_coupon")
            reinvest = st.number_input("Reinvestment Rate (%)", value=6.0, step=0.5, key="rr_r") / 100
            years = st.number_input("Holding Period (years)", value=10, step=1, key="rr_years")
            ending_price = st.number_input("Ending Bond Price ($)", value=1100.0, step=10.0, key="rr_end")
        with col2:
            if years <= 0:
                st.error("Holding period must be positive.")
            else:
                if abs(reinvest) < 1e-12:
                    fv_coupons = coupon * years
                else:
                    fv_coupons = coupon * (((1 + reinvest) ** years - 1) / reinvest)

                total_value = fv_coupons + ending_price
                realized = (total_value / initial) ** (1 / years) - 1 if initial > 0 else np.nan

                st.markdown(
                    f"""
                    <div class="concept-box">
                    <h4>Realized return analysis</h4>
                    <p><strong>FV of reinvested coupons:</strong> ${fv_coupons:.2f}</p>
                    <p><strong>Ending bond price:</strong> ${ending_price:.2f}</p>
                    <p><strong>Total value:</strong> ${total_value:.2f}</p>
                    <hr>
                    <h3>Realized annual return: {realized:.2%}</h3>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

def show_yield_curve():
    st.markdown('<div class="section-header">📈 Yield Curve</div>', unsafe_allow_html=True)
    st.markdown(
        """
The **yield curve** plots yields against maturities for bonds of similar credit risk.
It summarizes the **term structure** of interest rates.
        """
    )

    st.markdown("### Shapes (intuition)")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="concept-box">
            <h4>📈 Normal</h4>
            <p>Long-term yields > short-term yields</p>
            <ul><li>often associated with growth expectations</li><li>term premium for long horizons</li></ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="concept-box">
            <h4>📉 Inverted</h4>
            <p>Long-term yields < short-term yields</p>
            <ul><li>can indicate expectations of falling short rates</li><li>often seen around downturn fears</li></ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="concept-box">
            <h4>➡️ Flat</h4>
            <p>Yields similar across maturities</p>
            <ul><li>uncertainty / transition periods</li></ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="concept-box">
            <h4>🎭 Humped</h4>
            <p>Mid maturities highest</p>
            <ul><li>mixed expectations about near-term vs long-term rates</li></ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 🎨 Interactive yield curve builder")

    col1, col2 = st.columns([1, 2])
    with col1:
        curve_type = st.selectbox("Curve type", ["Normal", "Inverted", "Flat", "Humped", "Custom"], key="yc_type")
        if curve_type == "Custom":
            y1 = st.slider("1-Year Yield (%)", 0.0, 10.0, 2.0, 0.25, key="yc_1") / 100
            y2 = st.slider("2-Year Yield (%)", 0.0, 10.0, 2.5, 0.25, key="yc_2") / 100
            y5 = st.slider("5-Year Yield (%)", 0.0, 10.0, 3.0, 0.25, key="yc_5") / 100
            y10 = st.slider("10-Year Yield (%)", 0.0, 10.0, 3.5, 0.25, key="yc_10") / 100
            y30 = st.slider("30-Year Yield (%)", 0.0, 10.0, 4.0, 0.25, key="yc_30") / 100
            maturities = [1, 2, 5, 10, 30]
            yields = [y1, y2, y5, y10, y30]
        else:
            maturities = [0.25, 0.5, 1, 2, 5, 7, 10, 20, 30]
            if curve_type == "Normal":
                yields = [0.02, 0.025, 0.03, 0.035, 0.04, 0.042, 0.045, 0.048, 0.05]
            elif curve_type == "Inverted":
                yields = [0.05, 0.048, 0.045, 0.04, 0.035, 0.033, 0.03, 0.028, 0.027]
            elif curve_type == "Flat":
                yields = [0.035, 0.035, 0.035, 0.036, 0.035, 0.035, 0.035, 0.035, 0.035]
            else:  # Humped
                yields = [0.02, 0.03, 0.04, 0.045, 0.048, 0.047, 0.045, 0.042, 0.04]

    with col2:
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=maturities,
                y=[y * 100 for y in yields],
                mode="lines+markers",
                name="Yield curve",
                marker=dict(size=9),
            )
        )
        fig.update_layout(
            title=f"{curve_type} yield curve",
            xaxis_title="Maturity (years)",
            yaxis_title="Yield (%)",
            height=450,
            hovermode="x unified",
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.markdown("### 💭 Expectations-style intuition (simple forward-rate idea)")
    st.markdown(
        """
A simplified idea: longer yields can be related to expected future short rates (plus any term premium).
Here’s a basic two-period relationship under simplifying assumptions:
        """
    )
    st.markdown(
        """
        <div class="formula-box">
        (1 + y₂)² = (1 + y₁) × (1 + E[r₁])
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        y1 = st.number_input("Current 1-year rate (%)", value=3.0, step=0.25, key="ex_y1") / 100
        y2 = st.number_input("Current 2-year rate (%)", value=3.5, step=0.25, key="ex_y2") / 100
    with col2:
        expected_r1 = ((1 + y2) ** 2 / (1 + y1)) - 1 if (1 + y1) != 0 else np.nan
        st.markdown(
            f"""
            <div class="concept-box">
            <h4>Implied expected 1-year rate, one year from now</h4>
            <h3>{expected_r1:.2%}</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.info("💡 If y₂ > y₁, the implied future short rate is higher (under the simplifying model).")

def show_default_risk():
    st.markdown('<div class="section-header">⚠️ Default Risk</div>', unsafe_allow_html=True)
    st.markdown(
        """
**Default risk** is the possibility that an issuer fails to meet promised payments.
Credit ratings and credit spreads are market tools used to summarize this risk.
        """
    )

    st.markdown("### Ratings (simplified reference table)")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="concept-box">
            <h4>Investment grade (example mapping)</h4>
            <p>Often interpreted as BBB/Baa and above.</p>
            <table>
              <tr><th>Label</th><th>Intuition</th></tr>
              <tr><td>AAA</td><td>Very strong capacity</td></tr>
              <tr><td>AA</td><td>Strong capacity</td></tr>
              <tr><td>A</td><td>Adequate/strong</td></tr>
              <tr><td>BBB</td><td>Adequate; more sensitivity</td></tr>
            </table>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="concept-box" style="border-left-color:#F96167;">
            <h4>Speculative grade (example mapping)</h4>
            <p>Often interpreted as BB/Ba and below.</p>
            <table>
              <tr><th>Label</th><th>Intuition</th></tr>
              <tr><td>BB</td><td>Elevated risk</td></tr>
              <tr><td>B</td><td>High risk</td></tr>
              <tr><td>CCC</td><td>Substantial risk</td></tr>
              <tr><td>D</td><td>Default</td></tr>
            </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### Credit spread intuition")
    st.markdown(
        """
A **credit spread** is often summarized as the extra yield demanded over a similar-maturity government benchmark.
        """
    )
    st.markdown(
        """
        <div class="formula-box">
        Spread = Corporate Yield − Government Benchmark Yield
        </div>
        """,
        unsafe_allow_html=True,
    )

    ratings = ["AAA", "AA", "A", "BBB", "BB", "B", "CCC"]
    benchmark = st.number_input("Benchmark yield (%)", value=3.5, step=0.25, key="bench_y")  # percent
    spreads = [0.5, 0.8, 1.2, 2.0, 3.5, 5.0, 8.0]  # percent spreads (illustrative)
    corp = [benchmark + s for s in spreads]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=ratings, y=corp, name="Illustrative corporate yields"))
    fig.add_trace(go.Scatter(x=ratings, y=[benchmark] * len(ratings), mode="lines", name="Benchmark"))
    fig.update_layout(
        title="Illustrative yields by rating (benchmark + spread)",
        xaxis_title="Rating (illustrative)",
        yaxis_title="Yield (%)",
        height=450,
        hovermode="x unified",
    )
    st.plotly_chart(fig, use_container_width=True)
    st.warning("⚠️ Spreads tend to widen in stress periods and narrow when risk appetite improves.")

def show_calculator():
    st.markdown('<div class="section-header">🧮 Calculator</div>', unsafe_allow_html=True)
    st.markdown("Use this calculator for common bond computations.")

    calc_type = st.selectbox(
        "Calculation type",
        ["Bond Price", "YTM (Approx.)", "Duration & Convexity", "Compare Bonds"],
        key="calc_type",
    )

    if calc_type == "Bond Price":
        st.markdown("### Bond price")
        col1, col2, col3 = st.columns(3)
        with col1:
            fv = st.number_input("Face Value ($)", value=1000, step=100, key="c_fv")
            cr = st.number_input("Coupon Rate (%)", value=6.0, step=0.5, key="c_cr") / 100
        with col2:
            mat = st.number_input("Years to Maturity", value=10, step=1, key="c_mat")
            ytm = st.number_input("YTM (%)", value=8.0, step=0.5, key="c_ytm") / 100
        with col3:
            freq = st.selectbox(
                "Payment Frequency",
                [1, 2, 4],
                format_func=lambda x: {1: "Annual", 2: "Semi-annual", 4: "Quarterly"}[x],
                key="c_freq",
            )

        if st.button("Calculate", key="c_price_btn"):
            price = calculate_bond_price(fv, cr, mat, ytm, freq)
            cy = calculate_current_yield(cr, fv, price)
            st.markdown(
                f"""
                <div class="concept-box">
                <h2>Price: ${price:.2f}</h2>
                <p><strong>Current yield:</strong> {cy:.2%}</p>
                <p><strong>Status:</strong> {'Premium' if price > fv else 'Discount' if price < fv else 'Par'}</p>
                <p><strong>Dollar premium/discount:</strong> ${price - fv:.2f}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("#### Cash flow schedule (PV by period)")
            periods = int(round(mat * freq))
            periods = max(periods, 1)
            coupon_pmt = (fv * cr) / freq
            rows = []
            for i in range(1, periods + 1):
                cf = coupon_pmt + (fv if i == periods else 0)
                pv = cf / ((1 + ytm / freq) ** i) if abs(ytm) > 1e-12 else cf
                rows.append({"Period": i, "Years": i / freq, "Cash Flow": cf, "PV": pv})
            df = pd.DataFrame(rows)
            st.dataframe(df.style.format({"Cash Flow": "${:,.2f}", "PV": "${:,.2f}", "Years": "{:.2f}"}), use_container_width=True)

    elif calc_type == "YTM (Approx.)":
        st.markdown("### Approximate YTM")
        st.caption("Exact YTM generally requires numerical solving. This uses a common approximation.")
        col1, col2 = st.columns(2)
        with col1:
            p = st.number_input("Price ($)", value=950.0, step=10.0, key="cytm_p")
            fv = st.number_input("Face Value ($)", value=1000.0, step=100.0, key="cytm_fv")
            cr = st.number_input("Coupon Rate (%)", value=6.0, step=0.5, key="cytm_cr") / 100
            n = st.number_input("Years to Maturity", value=10, step=1, key="cytm_n")
        with col2:
            if st.button("Calculate", key="cytm_btn"):
                y = ytm_approximation(p, fv, cr, n)
                cy = calculate_current_yield(cr, fv, p)
                st.markdown(
                    f"""
                    <div class="concept-box">
                    <h2>Approx. YTM: {y:.2%}</h2>
                    <p><strong>Current yield:</strong> {cy:.2%}</p>
                    <p><strong>Coupon rate:</strong> {cr:.2%}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    elif calc_type == "Duration & Convexity":
        st.markdown("### Duration & convexity (interest-rate sensitivity)")
        col1, col2 = st.columns([1, 1.6])
        with col1:
            fv = st.number_input("Face Value ($)", value=1000, step=100, key="dc_fv")
            cr = st.number_input("Coupon Rate (%)", value=6.0, step=0.5, key="dc_cr") / 100
            years = st.slider("Years to Maturity", 1, 30, 10, key="dc_years")
            ytm = st.number_input("YTM (%)", value=8.0, step=0.5, key="dc_ytm") / 100
            freq = st.selectbox("Payments per year", [1, 2], format_func=lambda x: "Annual" if x == 1 else "Semi-annual", key="dc_freq")
            delta_bp = st.slider("Yield change (bp)", -300, 300, 100, 25, key="dc_bp")
            dy = delta_bp / 10000

        with col2:
            price = calculate_bond_price(fv, cr, years, ytm, freq)
            D = calculate_duration(fv, cr, years, ytm, freq)
            Dm = calculate_modified_duration(D, ytm, freq)
            C = calculate_convexity(fv, cr, years, ytm, freq)

            st.markdown("#### Metrics")
            c1, c2, c3 = st.columns(3)
            c1.metric("Price", f"${price:.2f}")
            c2.metric("Macaulay (yrs)", f"{D:.3f}")
            c3.metric("Modified", f"{Dm:.3f}")
            st.metric("Convexity", f"{C:.2f}")

            new_price = calculate_bond_price(fv, cr, years, ytm + dy, freq)
            actual = (new_price - price) / price

            est_d = price_change_duration(Dm, dy)
            est_dc = price_change_duration_convexity(Dm, C, dy)

            df = pd.DataFrame(
                {
                    "Method": ["Actual (reprice)", "Duration approx", "Duration+Convexity approx"],
                    "ΔP/P (%)": [actual * 100, est_d * 100, est_dc * 100],
                    "Implied Price": [new_price, price * (1 + est_d), price * (1 + est_dc)],
                }
            )
            st.dataframe(df.style.format({"ΔP/P (%)": "{:.4f}%", "Implied Price": "${:,.2f}"}), use_container_width=True)

            if abs(actual) > 1e-12:
                err_d = abs(est_d - actual) / abs(actual) * 100
                err_dc = abs(est_dc - actual) / abs(actual) * 100
                st.markdown(
                    f"""
                    <div class="concept-box">
                    <h4>Approximation error</h4>
                    <p><strong>Duration-only:</strong> {err_d:.2f}%</p>
                    <p><strong>Duration+convexity:</strong> {err_dc:.2f}%</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    else:  # Compare Bonds
        st.markdown("### Compare two bonds")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Bond A")
            fv_a = st.number_input("Face Value ($)", value=1000, key="cb_fv_a")
            cr_a = st.number_input("Coupon Rate (%)", value=5.0, key="cb_cr_a") / 100
            mat_a = st.number_input("Years to Maturity", value=10, key="cb_mat_a")
            ytm_a = st.number_input("YTM (%)", value=6.0, key="cb_ytm_a") / 100
        with col2:
            st.markdown("#### Bond B")
            fv_b = st.number_input("Face Value ($)", value=1000, key="cb_fv_b")
            cr_b = st.number_input("Coupon Rate (%)", value=7.0, key="cb_cr_b") / 100
            mat_b = st.number_input("Years to Maturity", value=20, key="cb_mat_b")
            ytm_b = st.number_input("YTM (%)", value=6.0, key="cb_ytm_b") / 100

        if st.button("Compare", key="cb_btn"):
            price_a = calculate_bond_price(fv_a, cr_a, mat_a, ytm_a, 2)
            price_b = calculate_bond_price(fv_b, cr_b, mat_b, ytm_b, 2)
            cy_a = calculate_current_yield(cr_a, fv_a, price_a)
            cy_b = calculate_current_yield(cr_b, fv_b, price_b)

            comparison = pd.DataFrame(
                {
                    "Metric": ["Price", "Coupon rate", "Current yield", "YTM", "Maturity", "Status"],
                    "Bond A": [
                        f"${price_a:.2f}",
                        f"{cr_a:.1%}",
                        f"{cy_a:.2%}",
                        f"{ytm_a:.2%}",
                        f"{mat_a}y",
                        "Premium" if price_a > fv_a else "Discount" if price_a < fv_a else "Par",
                    ],
                    "Bond B": [
                        f"${price_b:.2f}",
                        f"{cr_b:.1%}",
                        f"{cy_b:.2%}",
                        f"{ytm_b:.2%}",
                        f"{mat_b}y",
                        "Premium" if price_b > fv_b else "Discount" if price_b < fv_b else "Par",
                    ],
                }
            )
            st.dataframe(comparison, use_container_width=True)

            rates = np.linspace(0.02, 0.12, 40)
            prices_a = [calculate_bond_price(fv_a, cr_a, mat_a, r, 2) for r in rates]
            prices_b = [calculate_bond_price(fv_b, cr_b, mat_b, r, 2) for r in rates]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=rates * 100, y=prices_a, mode="lines", name="Bond A"))
            fig.add_trace(go.Scatter(x=rates * 100, y=prices_b, mode="lines", name="Bond B"))
            fig.update_layout(
                title="Price sensitivity comparison",
                xaxis_title="Yield (%)",
                yaxis_title="Price ($)",
                height=450,
                hovermode="x unified",
            )
            st.plotly_chart(fig, use_container_width=True)

def show_quiz():
    st.markdown('<div class="section-header">✅ Quiz</div>', unsafe_allow_html=True)
    st.markdown("Quick knowledge check. Submit each question once (reset anytime).")

    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0
    if "quiz_attempted" not in st.session_state:
        st.session_state.quiz_attempted = set()

    def submit(qkey, correct_choice, selected):
        if qkey in st.session_state.quiz_attempted:
            return
        st.session_state.quiz_attempted.add(qkey)
        if selected == correct_choice:
            st.session_state.quiz_score += 1
            st.markdown('<div class="quiz-correct">✅ Correct!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="quiz-incorrect">❌ Incorrect.</div>', unsafe_allow_html=True)

    st.markdown("### Q1: Price–yield relationship")
    q1 = st.radio("When market yields rise, bond prices:", ["Rise", "Fall", "Stay the same", "Depends"], key="qz1")
    if st.button("Submit Q1", key="qz1_btn"):
        submit("q1", "Fall", q1)

    st.markdown("---")
    st.markdown("### Q2: Premium vs discount")
    q2 = st.radio("A bond trading above face value is a:", ["Discount", "Premium", "Par", "Zero-coupon"], key="qz2")
    if st.button("Submit Q2", key="qz2_btn"):
        submit("q2", "Premium", q2)

    st.markdown("---")
    st.markdown("### Q3: Maturity and sensitivity")
    q3 = st.radio("Which is typically more rate-sensitive?", ["2-year bond", "30-year bond", "Equal", "Need more info"], key="qz3")
    if st.button("Submit Q3", key="qz3_btn"):
        submit("q3", "30-year bond", q3)

    st.markdown("---")
    st.markdown("### Q4: Discount bond yields")
    q4 = st.radio(
        "For a discount bond, which ordering is most typical?",
        ["YTM > Current Yield > Coupon Rate", "Coupon Rate > Current Yield > YTM", "Current Yield > YTM > Coupon Rate", "All equal"],
        key="qz4",
    )
    if st.button("Submit Q4", key="qz4_btn"):
        submit("q4", "YTM > Current Yield > Coupon Rate", q4)

    st.markdown("---")
    st.markdown("### Q5: Investment grade boundary (simplified)")
    q5 = st.radio("Which is commonly considered investment grade (simplified)?", ["BB", "BBB", "B", "CCC"], key="qz5")
    if st.button("Submit Q5", key="qz5_btn"):
        submit("q5", "BBB", q5)

    st.markdown("---")
    attempted = len(st.session_state.quiz_attempted)
    if attempted > 0:
        score = st.session_state.quiz_score
        pct = (score / attempted) * 100
        st.markdown(
            f"""
            <div class="concept-box">
            <h2>Your Score: {score} / {attempted}</h2>
            <h3>{pct:.0f}%</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if pct >= 80:
            st.success("🎉 Strong performance.")
        elif pct >= 60:
            st.info("👍 Solid—review the misses.")
        else:
            st.warning("📚 Keep going—revisit the concepts and try again.")

    if st.button("Reset Quiz", key="qz_reset"):
        st.session_state.quiz_score = 0
        st.session_state.quiz_attempted = set()
        st.rerun()

# -----------------------------------------------------------------------------
# Main app router
# -----------------------------------------------------------------------------
def main():
    st.sidebar.markdown("## 📚 Navigation")
    #render_disclaimer()

    page = st.sidebar.radio(
        "Choose a topic:",
        ["🏠 Home", "📖 Bond Basics", "💵 Bond Pricing", "📊 Yield Calculations", "📈 Yield Curve", "⚠️ Default Risk", "🧮 Calculator", "✅ Quiz"],
        key="nav",
    )

    if page == "🏠 Home":
        show_home()
    elif page == "📖 Bond Basics":
        show_bond_basics()
    elif page == "💵 Bond Pricing":
        show_bond_pricing()
    elif page == "📊 Yield Calculations":
        show_yield_calculations()
    elif page == "📈 Yield Curve":
        show_yield_curve()
    elif page == "⚠️ Default Risk":
        show_default_risk()
    elif page == "🧮 Calculator":
        show_calculator()
    else:
        show_quiz()

    render_footer()

if __name__ == "__main__":
    main()
