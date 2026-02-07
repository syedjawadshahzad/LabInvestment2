import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Equity Valuation",
    page_icon="💼",
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
    .valuation-box {
        background-color: #97BC62;
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #F96167;
        padding: 1rem;
        border-radius: 8px;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Main App
def main():
    # Sidebar Navigation
    st.sidebar.markdown("## 📚 Navigation")
    page = st.sidebar.radio(
        "Choose a topic:",
        ["🏠 Home",
         "📚 Valuation Basics",
         "📈 Dividend Discount Model",
         "💹 Two-Stage DDM",
         "📊 P/E Ratio Analysis",
         "💰 Free Cash Flow",
         "🔍 Model Comparison",
         "✅ Quiz"]
    )
    
    if page == "🏠 Home":
        show_home()
    elif page == "📚 Valuation Basics":
        show_valuation_basics()
    elif page == "📈 Dividend Discount Model":
        show_ddm()
    elif page == "💹 Two-Stage DDM":
        show_two_stage_ddm()
    elif page == "📊 P/E Ratio Analysis":
        show_pe_analysis()
    elif page == "💰 Free Cash Flow":
        show_fcf()
    elif page == "🔍 Model Comparison":
        show_model_comparison()
    elif page == "✅ Quiz":
        show_quiz()

def show_home():
    st.markdown('<div class="main-header">💼 Equity Valuation</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Intrinsic Value & Valuation Models</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">📈 DDM Models</h3>
        <p>Dividend-based valuation</p>
        <ul>
        <li>Constant growth (Gordon model)</li>
        <li>Two-stage growth</li>
        <li>Multi-stage models</li>
        <li>Growth rate determinants</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">📊 P/E Analysis</h3>
        <p>Relative valuation</p>
        <ul>
        <li>P/E ratio fundamentals</li>
        <li>Growth opportunities</li>
        <li>ROE & plowback effects</li>
        <li>Comparative ratios</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">💰 FCF Valuation</h3>
        <p>Cash flow-based models</p>
        <ul>
        <li>Free Cash Flow to Firm (FCFF)</li>
        <li>Free Cash Flow to Equity (FCFE)</li>
        <li>WACC calculations</li>
        <li>Terminal value</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown('<div class="section-header">📋 Chapter Overview</div>', unsafe_allow_html=True)
    
    st.markdown("""
    This interactive app covers **Equity Valuation**.
    
    ### Valuation Approaches:
    
    1. **Book Value** → Balance sheet measure (limited usefulness)
    2. **Dividend Discount Models** → Value based on expected dividends
    3. **P/E Ratio Analysis** → Relative valuation using multiples
    4. **Free Cash Flow Models** → Value based on cash generation
    
    ### 🎯 Learning Objectives:
    
    By the end of this module, you will be able to:
    - Calculate intrinsic value using dividend discount models
    - Apply constant growth and multi-stage growth models
    - Analyze P/E ratios and understand their determinants
    - Value companies using free cash flow approaches
    - Compare different valuation methods and understand their limitations
    """)
    
    st.info("💡 **Key Insight:** Intrinsic value is what the stock is *really* worth. Market price is what people *pay* for it. Smart investors buy when price < intrinsic value!")

def show_valuation_basics():
    st.markdown('<div class="section-header">📚 Valuation Basics</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Book Value vs. Intrinsic Value vs. Market Price
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="concept-box">
        <h4>📖 Book Value</h4>
        <p><strong>Definition:</strong> Net worth according to balance sheet</p>
        <p><strong>Formula:</strong> Assets - Liabilities</p>
        <hr>
        <p><strong>Limitations:</strong></p>
        <ul>
        <li>Historical cost accounting</li>
        <li>Doesn't reflect market values</li>
        <li>Ignores intangibles</li>
        <li>Ignores growth opportunities</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="concept-box">
        <h4>💎 Intrinsic Value</h4>
        <p><strong>Definition:</strong> Present value of expected future cash flows</p>
        <p><strong>Formula:</strong> PV of dividends/FCF</p>
        <hr>
        <p><strong>Characteristics:</strong></p>
        <ul>
        <li>Based on fundamentals</li>
        <li>Requires forecasts</li>
        <li>Subjective estimates</li>
        <li>"True" economic value</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="concept-box">
        <h4>💵 Market Price</h4>
        <p><strong>Definition:</strong> What investors actually pay</p>
        <p><strong>Determined by:</strong> Supply & demand</p>
        <hr>
        <p><strong>Characteristics:</strong></p>
        <ul>
        <li>Observable, objective</li>
        <li>Changes constantly</li>
        <li>May deviate from intrinsic value</li>
        <li>Consensus valuation</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Holding Period Return
    st.markdown("### 📈 Holding Period Return (HPR)")
    
    st.markdown("""
    <div class="formula-box">
    <strong>HPR = (Dividend + Price Change) / Initial Price</strong><br><br>
    HPR = (D₁ + P₁ - P₀) / P₀
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### Interactive HPR Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        p0 = st.number_input("Purchase Price (P₀)", value=40.0, step=1.0, key="hpr_p0")
        div = st.number_input("Expected Dividend (D₁)", value=2.42, step=0.1, key="hpr_div")
        p1 = st.number_input("Expected Ending Price (P₁)", value=42.0, step=1.0, key="hpr_p1")
    
    with col2:
        capital_gain = p1 - p0
        dividend_yield = div / p0
        capital_gain_yield = capital_gain / p0
        total_hpr = (div + capital_gain) / p0
        
        st.markdown(f"""
        <div class="valuation-box">
        <h3>Expected HPR: {total_hpr:.2%}</h3>
        <hr style="border-color: white;">
        <p><strong>Breakdown:</strong></p>
        <p>Dividend Yield: {dividend_yield:.2%}</p>
        <p>Capital Gain Yield: {capital_gain_yield:.2%}</p>
        <p>Total Return: {total_hpr:.2%}</p>
        </div>
        """, unsafe_allow_html=True)
        
        dollar_return = div + capital_gain
        st.markdown(f"""
        <div class="concept-box">
        <p><strong>Dollar Return:</strong> ${dollar_return:.2f}</p>
        <p>On investment of ${p0:.2f}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Market Capitalization Rate
    st.markdown("### 🎯 Market Capitalization Rate")
    
    st.markdown("""
    <div class="concept-box">
    <h4>Market Capitalization Rate (k)</h4>
    <p>The <strong>required rate of return</strong> that investors demand for holding the stock.</p>
    <p>Also called the <strong>discount rate</strong> or <strong>cost of equity</strong>.</p>
    <hr>
    <p><strong>Determined by:</strong></p>
    <ul>
    <li>Risk-free rate</li>
    <li>Market risk premium</li>
    <li>Stock's beta (systematic risk)</li>
    </ul>
    <p><strong>CAPM Formula:</strong> k = Rₓ + β × (Rₘ - Rₓ)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # CAPM Calculator
    st.markdown("#### CAPM Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        rf = st.slider("Risk-Free Rate (%)", 0.0, 10.0, 3.0, 0.5, key="capm_rf") / 100
        rm = st.slider("Expected Market Return (%)", 0.0, 20.0, 10.0, 0.5, key="capm_rm") / 100
        beta = st.slider("Stock Beta", 0.0, 2.5, 1.2, 0.1, key="capm_beta")
    
    with col2:
        market_premium = rm - rf
        required_return = rf + beta * market_premium
        
        st.markdown(f"""
        <div class="valuation-box">
        <h3>Required Return (k): {required_return:.2%}</h3>
        <hr style="border-color: white;">
        <p>Risk-Free Rate: {rf:.2%}</p>
        <p>Market Premium: {market_premium:.2%}</p>
        <p>Beta: {beta:.2f}</p>
        <p>Risk Premium: {beta * market_premium:.2%}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if beta > 1:
            st.info(f"📈 This stock is **more volatile** than the market (β={beta:.2f} > 1)")
        elif beta < 1:
            st.info(f"📉 This stock is **less volatile** than the market (β={beta:.2f} < 1)")
        else:
            st.info(f"📊 This stock has **average volatility** (β={beta:.2f} = 1)")

def show_ddm():
    st.markdown('<div class="section-header">📈 Dividend Discount Model</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### The Foundation of Equity Valuation
    
    The **Dividend Discount Model (DDM)** values a stock as the present value of all future dividends.
    """)
    
    st.markdown("""
    <div class="formula-box">
    <strong>General DDM Formula:</strong><br><br>
    V₀ = Σ [Dₜ / (1 + k)ᵗ]<br><br>
    Where:<br>
    V₀ = Intrinsic value today<br>
    Dₜ = Expected dividend in period t<br>
    k = Required rate of return
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Constant Growth DDM (Gordon Model)
    st.markdown("### 🌱 Constant Growth DDM (Gordon Model)")
    
    st.markdown("""
    <div class="concept-box">
    <h4>Assumptions:</h4>
    <ul>
    <li>Dividends grow at a <strong>constant rate (g)</strong> forever</li>
    <li>Growth rate g < Required return k</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="formula-box">
    <strong>Gordon Growth Model:</strong><br><br>
    V₀ = D₁ / (k - g)<br><br>
    Where:<br>
    D₁ = Expected dividend next year<br>
    k = Required return<br>
    g = Constant growth rate
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Gordon Model
    st.markdown("#### 🧮 Gordon Model Calculator")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("**Inputs**")
        d0 = st.number_input("Current Dividend (D₀)", value=2.00, step=0.1, key="gordon_d0")
        g = st.slider("Dividend Growth Rate (%)", 0.0, 15.0, 5.0, 0.5, key="gordon_g") / 100
        k_gordon = st.slider("Required Return (%)", 5.0, 20.0, 10.0, 0.5, key="gordon_k") / 100
        
        if g >= k_gordon:
            st.error("⚠️ Growth rate must be less than required return!")
    
    with col2:
        if g < k_gordon:
            d1 = d0 * (1 + g)
            intrinsic_value = d1 / (k_gordon - g)
            
            st.markdown(f"""
            <div class="valuation-box">
            <h2>Intrinsic Value: ${intrinsic_value:.2f}</h2>
            <hr style="border-color: white;">
            <p><strong>D₁ (Next year's dividend):</strong> ${d1:.2f}</p>
            <p><strong>Growth Rate:</strong> {g:.1%}</p>
            <p><strong>Required Return:</strong> {k_gordon:.1%}</p>
            <p><strong>Spread (k - g):</strong> {(k_gordon - g):.1%}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Investment decision
            current_price = st.number_input("Current Market Price", value=35.0, step=1.0, key="gordon_price")
            
            if current_price < intrinsic_value:
                diff = intrinsic_value - current_price
                diff_pct = (diff / current_price) * 100
                st.success(f"✅ **BUY**: Stock is undervalued by ${diff:.2f} ({diff_pct:.1f}%)")
            elif current_price > intrinsic_value:
                diff = current_price - intrinsic_value
                diff_pct = (diff / current_price) * 100
                st.error(f"❌ **SELL**: Stock is overvalued by ${diff:.2f} ({diff_pct:.1f}%)")
            else:
                st.info("➡️ **HOLD**: Stock is fairly valued")
    
    st.markdown("---")
    
    # Sensitivity Analysis
    st.markdown("### 📊 Sensitivity Analysis")
    
    st.markdown("See how intrinsic value changes with different growth rates and required returns:")
    
    # Create sensitivity table
    growth_rates = np.array([0.02, 0.04, 0.06, 0.08, 0.10])
    required_returns = np.array([0.08, 0.10, 0.12, 0.14, 0.16])
    
    sensitivity_data = []
    for k_val in required_returns:
        row = []
        for g_val in growth_rates:
            if g_val < k_val:
                d1_val = d0 * (1 + g_val)
                value = d1_val / (k_val - g_val)
                row.append(value)
            else:
                row.append(np.nan)
        sensitivity_data.append(row)
    
    sensitivity_df = pd.DataFrame(
        sensitivity_data,
        index=[f'{r:.0%}' for r in required_returns],
        columns=[f'{g:.0%}' for g in growth_rates]
    )
    sensitivity_df.index.name = 'k (Required Return)'
    sensitivity_df.columns.name = 'g (Growth Rate)'
    
    st.dataframe(sensitivity_df.style.format('${:.2f}').background_gradient(cmap='RdYlGn', axis=None),
                use_container_width=True)
    
    st.info("💡 **Key Insights:**\n- Higher growth → Higher value\n- Higher required return → Lower value\n- Small changes in g or k can dramatically affect value!")
    
    st.markdown("---")
    
    # Determinants of Growth Rate
    st.markdown("### 🔍 What Determines Growth Rate?")
    
    st.markdown("""
    <div class="formula-box">
    <strong>Sustainable Growth Rate:</strong><br><br>
    g = ROE × Plowback Ratio<br>
    g = ROE × (1 - Payout Ratio)
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        roe = st.slider("Return on Equity (%)", 0.0, 30.0, 15.0, 1.0, key="growth_roe") / 100
        plowback = st.slider("Plowback Ratio (%)", 0.0, 100.0, 60.0, 5.0, key="growth_pb") / 100
    
    with col2:
        sustainable_g = roe * plowback
        payout_ratio = 1 - plowback
        
        st.markdown(f"""
        <div class="valuation-box">
        <h3>Sustainable Growth: {sustainable_g:.2%}</h3>
        <hr style="border-color: white;">
        <p><strong>ROE:</strong> {roe:.2%}</p>
        <p><strong>Plowback Ratio:</strong> {plowback:.2%}</p>
        <p><strong>Payout Ratio:</strong> {payout_ratio:.2%}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="concept-box">
        <p><strong>Interpretation:</strong></p>
        <p>The company earns {:.1%} on equity and reinvests {:.0%} of earnings.</p>
        <p>This generates {:.2%} annual growth in dividends and earnings.</p>
        </div>
        """.format(roe, plowback * 100, sustainable_g), unsafe_allow_html=True)

def show_two_stage_ddm():
    st.markdown('<div class="section-header">💹 Two-Stage Dividend Discount Model</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Multi-Stage Growth Models
    
    Most companies don't grow at a constant rate forever. **Two-stage models** allow for:
    1. **High growth phase**: Rapid growth for several years
    2. **Stable growth phase**: Constant growth thereafter
    """)
    
    st.markdown("""
    <div class="formula-box">
    <strong>Two-Stage DDM Formula:</strong><br><br>
    V₀ = PV(High Growth Dividends) + PV(Terminal Value)<br><br>
    V₀ = Σ[Dₜ/(1+k)ᵗ] + [Pₙ/(1+k)ᴺ]<br><br>
    Where Pₙ = Dₙ₊₁/(k - g₂)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive Two-Stage Model
    st.markdown("### 🧮 Two-Stage DDM Calculator")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("#### Stage 1: High Growth")
        d0_ts = st.number_input("Current Dividend (D₀)", value=1.00, step=0.1, key="ts_d0")
        g1_ts = st.slider("High Growth Rate (%)", 5.0, 50.0, 20.0, 1.0, key="ts_g1") / 100
        n_years = st.slider("Years of High Growth", 1, 10, 3, key="ts_years")
        
        st.markdown("#### Stage 2: Stable Growth")
        g2_ts = st.slider("Stable Growth Rate (%)", 0.0, 10.0, 5.0, 0.5, key="ts_g2") / 100
        
        st.markdown("#### Discount Rate")
        k_ts = st.slider("Required Return (%)", 5.0, 20.0, 12.0, 0.5, key="ts_k") / 100
        
        if g2_ts >= k_ts:
            st.error("⚠️ Stable growth must be less than required return!")
    
    with col2:
        if g2_ts < k_ts:
            # Calculate high growth dividends
            high_growth_divs = []
            pv_high_growth = 0
            
            for t in range(1, n_years + 1):
                div_t = d0_ts * ((1 + g1_ts) ** t)
                pv_div = div_t / ((1 + k_ts) ** t)
                pv_high_growth += pv_div
                high_growth_divs.append({
                    'Year': t,
                    'Dividend': div_t,
                    'PV': pv_div
                })
            
            # Calculate terminal value
            d_terminal = d0_ts * ((1 + g1_ts) ** n_years) * (1 + g2_ts)
            p_terminal = d_terminal / (k_ts - g2_ts)
            pv_terminal = p_terminal / ((1 + k_ts) ** n_years)
            
            # Total value
            intrinsic_value_ts = pv_high_growth + pv_terminal
            
            st.markdown(f"""
            <div class="valuation-box">
            <h2>Intrinsic Value: ${intrinsic_value_ts:.2f}</h2>
            <hr style="border-color: white;">
            <p><strong>PV of High Growth Dividends:</strong> ${pv_high_growth:.2f}</p>
            <p><strong>PV of Terminal Value:</strong> ${pv_terminal:.2f}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Breakdown
            st.markdown("#### Value Breakdown")
            
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=['High Growth\nDividends', 'Terminal\nValue'],
                y=[pv_high_growth, pv_terminal],
                marker_color=['#028090', '#97BC62'],
                text=[f'${pv_high_growth:.2f}', f'${pv_terminal:.2f}'],
                textposition='auto'
            ))
            fig.update_layout(
                title="Sources of Value",
                yaxis_title="Present Value ($)",
                height=400,
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
            
            pct_terminal = (pv_terminal / intrinsic_value_ts) * 100
            st.info(f"💡 **Terminal value represents {pct_terminal:.1f}% of total value**")
    
    st.markdown("---")
    
    # Dividend Schedule
    if g2_ts < k_ts:
        st.markdown("### 📅 Projected Dividend Schedule")
        
        # Create full dividend schedule
        schedule_data = []
        for t in range(1, n_years + 6):  # Show 5 years into stable phase
            if t <= n_years:
                div = d0_ts * ((1 + g1_ts) ** t)
                growth = g1_ts
                phase = "High Growth"
            else:
                div = d0_ts * ((1 + g1_ts) ** n_years) * ((1 + g2_ts) ** (t - n_years))
                growth = g2_ts
                phase = "Stable Growth"
            
            pv = div / ((1 + k_ts) ** t)
            
            schedule_data.append({
                'Year': t,
                'Phase': phase,
                'Growth Rate': f'{growth:.1%}',
                'Dividend': f'${div:.2f}',
                'PV of Dividend': f'${pv:.2f}'
            })
        
        schedule_df = pd.DataFrame(schedule_data)
        st.dataframe(schedule_df, use_container_width=True, hide_index=True)
        
        # Visualization
        dividends_over_time = [d0_ts * ((1 + g1_ts) ** t) if t <= n_years 
                              else d0_ts * ((1 + g1_ts) ** n_years) * ((1 + g2_ts) ** (t - n_years))
                              for t in range(1, 21)]
        
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=list(range(1, 21)),
            y=dividends_over_time,
            mode='lines+markers',
            line=dict(color='#028090', width=3),
            marker=dict(size=8)
        ))
        
        # Add vertical line at transition
        fig2.add_vline(x=n_years, line_dash="dash", line_color="red",
                      annotation_text="Growth Transition")
        
        fig2.update_layout(
            title="Dividend Growth Over Time",
            xaxis_title="Year",
            yaxis_title="Dividend ($)",
            height=400
        )
        st.plotly_chart(fig2, use_container_width=True)

def show_pe_analysis():
    st.markdown('<div class="section-header">📊 Price-Earnings Ratio Analysis</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### P/E Ratio: The Most Popular Valuation Multiple
    
    The **P/E ratio** compares a stock's price to its earnings per share.
    """)
    
    st.markdown("""
    <div class="formula-box">
    <strong>P/E Ratio = Price per Share / Earnings per Share</strong>
    </div>
    """, unsafe_allow_html=True)
    
    # P/E from DDM
    st.markdown("### 🔗 Linking P/E to the DDM")
    
    st.markdown("""
    <div class="concept-box">
    <h4>P/E Ratio from Gordon Model:</h4>
    <p>Starting with: P₀ = D₁ / (k - g)</p>
    <p>Divide both sides by E₁ (earnings):</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="formula-box">
    <strong>P/E = (D₁/E₁) / (k - g)</strong><br>
    <strong>P/E = Payout Ratio / (k - g)</strong><br><br>
    Or equivalently:<br>
    <strong>P/E = (1 - b) / (k - ROE × b)</strong><br><br>
    Where:<br>
    b = Plowback ratio<br>
    (1 - b) = Payout ratio
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive P/E Calculator
    st.markdown("### 🧮 P/E Ratio Calculator")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("#### Company Fundamentals")
        roe_pe = st.slider("Return on Equity (%)", 5.0, 30.0, 15.0, 1.0, key="pe_roe") / 100
        plowback_pe = st.slider("Plowback Ratio (%)", 0.0, 100.0, 40.0, 5.0, key="pe_pb") / 100
        k_pe = st.slider("Required Return (%)", 8.0, 20.0, 12.0, 0.5, key="pe_k") / 100
    
    with col2:
        payout_ratio = 1 - plowback_pe
        growth_rate_pe = roe_pe * plowback_pe
        
        if growth_rate_pe < k_pe:
            pe_ratio = payout_ratio / (k_pe - growth_rate_pe)
            
            st.markdown(f"""
            <div class="valuation-box">
            <h2>P/E Ratio: {pe_ratio:.2f}</h2>
            <hr style="border-color: white;">
            <p><strong>Payout Ratio:</strong> {payout_ratio:.1%}</p>
            <p><strong>Growth Rate (g = ROE × b):</strong> {growth_rate_pe:.2%}</p>
            <p><strong>Required Return:</strong> {k_pe:.2%}</p>
            <p><strong>k - g:</strong> {(k_pe - growth_rate_pe):.2%}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Market valuation
            eps = st.number_input("Earnings Per Share (EPS)", value=5.00, step=0.5, key="pe_eps")
            implied_price = pe_ratio * eps
            
            st.markdown(f"""
            <div class="concept-box">
            <h4>Implied Stock Price</h4>
            <p><strong>EPS:</strong> ${eps:.2f}</p>
            <p><strong>P/E Ratio:</strong> {pe_ratio:.2f}</p>
            <p><strong>Implied Price:</strong> ${implied_price:.2f}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("⚠️ Growth rate exceeds required return!")
    
    st.markdown("---")
    
    # P/E Sensitivity to ROE and Plowback
    st.markdown("### 📈 How ROE and Plowback Affect P/E")
    
    # Create sensitivity matrix
    roe_values = np.linspace(0.08, 0.25, 10)
    plowback_values = np.linspace(0, 0.8, 10)
    
    pe_matrix = np.zeros((len(roe_values), len(plowback_values)))
    
    for i, roe_val in enumerate(roe_values):
        for j, pb_val in enumerate(plowback_values):
            payout = 1 - pb_val
            g_val = roe_val * pb_val
            if g_val < k_pe:
                pe_matrix[i, j] = payout / (k_pe - g_val)
            else:
                pe_matrix[i, j] = np.nan
    
    fig = go.Figure(data=go.Heatmap(
        z=pe_matrix,
        x=[f'{pb:.0%}' for pb in plowback_values],
        y=[f'{roe:.0%}' for roe in roe_values],
        colorscale='RdYlGn',
        colorbar=dict(title="P/E Ratio")
    ))
    
    fig.update_layout(
        title=f"P/E Ratio Heatmap (k = {k_pe:.1%})",
        xaxis_title="Plowback Ratio",
        yaxis_title="ROE",
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 **Key Insights:**\n- Higher ROE → Higher P/E (if ROE > k)\n- Optimal plowback depends on ROE\n- If ROE < k, plowback reduces P/E (bad investments)\n- If ROE > k, plowback increases P/E (good investments)")
    
    st.markdown("---")
    
    # Other Valuation Ratios
    st.markdown("### 📊 Other Comparative Valuation Ratios")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="concept-box">
        <h4>Price-to-Book (P/B)</h4>
        <p><strong>Formula:</strong> Market Price / Book Value per Share</p>
        <p><strong>Use:</strong> Indicates how aggressively market values firm</p>
        <p><strong>Typical:</strong> P/B > 1 for profitable firms</p>
        <hr>
        <h4>Price-to-Sales (P/S)</h4>
        <p><strong>Formula:</strong> Market Price / Sales per Share</p>
        <p><strong>Use:</strong> For startups with no earnings</p>
        <p><strong>Advantage:</strong> Sales harder to manipulate than earnings</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="concept-box">
        <h4>Price-to-Cash Flow (P/CF)</h4>
        <p><strong>Formula:</strong> Market Price / Cash Flow per Share</p>
        <p><strong>Use:</strong> Cash flow less affected by accounting</p>
        <p><strong>Advantage:</strong> More reliable than earnings</p>
        <hr>
        <h4>PEG Ratio</h4>
        <p><strong>Formula:</strong> P/E Ratio / Growth Rate</p>
        <p><strong>Use:</strong> Adjusts P/E for growth</p>
        <p><strong>Rule of thumb:</strong> PEG < 1 may indicate undervaluation</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Comparative ratios calculator
    st.markdown("#### Comparative Ratios Calculator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        price_comp = st.number_input("Stock Price", value=50.0, step=1.0, key="comp_price")
        eps_comp = st.number_input("EPS", value=4.0, step=0.5, key="comp_eps")
    
    with col2:
        bvps = st.number_input("Book Value per Share", value=25.0, step=1.0, key="comp_bv")
        sales_ps = st.number_input("Sales per Share", value=100.0, step=5.0, key="comp_sales")
    
    with col3:
        cf_ps = st.number_input("Cash Flow per Share", value=6.0, step=0.5, key="comp_cf")
        growth_comp = st.number_input("Growth Rate (%)", value=15.0, step=1.0, key="comp_g")
    
    # Calculate ratios
    pe_comp = price_comp / eps_comp if eps_comp > 0 else 0
    pb_comp = price_comp / bvps if bvps > 0 else 0
    ps_comp = price_comp / sales_ps if sales_ps > 0 else 0
    pcf_comp = price_comp / cf_ps if cf_ps > 0 else 0
    peg_comp = (pe_comp / growth_comp) * 100 if growth_comp > 0 else 0
    
    ratios_df = pd.DataFrame({
        'Ratio': ['P/E', 'P/B', 'P/S', 'P/CF', 'PEG'],
        'Value': [f'{pe_comp:.2f}', f'{pb_comp:.2f}', f'{ps_comp:.2f}', f'{pcf_comp:.2f}', f'{peg_comp:.2f}']
    })
    
    st.dataframe(ratios_df, use_container_width=True, hide_index=True)

def show_fcf():
    st.markdown('<div class="section-header">💰 Free Cash Flow Valuation</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Free Cash Flow Models
    
    **Free Cash Flow (FCF)** represents cash available to investors after all necessary investments.
    
    Two main approaches:
    1. **FCFF**: Free Cash Flow to the Firm (all investors)
    2. **FCFE**: Free Cash Flow to Equity (only equity holders)
    """)
    
    # FCFF vs FCFE
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="concept-box">
        <h4>FCFF: Free Cash Flow to Firm</h4>
        <div class="formula-box" style="font-size: 0.95rem;">
        FCFF = EBIT × (1 - Tax Rate)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ Depreciation<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Capital Expenditures<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Increase in NWC
        </div>
        <p><strong>Discount Rate:</strong> WACC</p>
        <p><strong>Result:</strong> Enterprise Value</p>
        <p><strong>Then:</strong> Subtract debt to get equity value</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="concept-box">
        <h4>FCFE: Free Cash Flow to Equity</h4>
        <div class="formula-box" style="font-size: 0.95rem;">
        FCFE = FCFF<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Interest × (1 - Tax Rate)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ Net Borrowing
        </div>
        <p><strong>Discount Rate:</strong> Cost of Equity (k)</p>
        <p><strong>Result:</strong> Equity Value directly</p>
        <p><strong>Simpler:</strong> No need to subtract debt</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # FCFF Calculator
    st.markdown("### 🧮 FCFF Valuation Calculator")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("#### Operating Data")
        ebit = st.number_input("EBIT ($M)", value=500.0, step=10.0, key="fcff_ebit")
        tax_rate = st.slider("Tax Rate (%)", 0.0, 50.0, 25.0, 1.0, key="fcff_tax") / 100
        depreciation = st.number_input("Depreciation ($M)", value=100.0, step=10.0, key="fcff_dep")
        capex = st.number_input("Capital Expenditures ($M)", value=150.0, step=10.0, key="fcff_capex")
        nwc_increase = st.number_input("Increase in NWC ($M)", value=20.0, step=5.0, key="fcff_nwc")
        
        st.markdown("#### Growth & Discount Rate")
        fcf_growth = st.slider("FCF Growth Rate (%)", 0.0, 15.0, 5.0, 0.5, key="fcff_g") / 100
        wacc = st.slider("WACC (%)", 5.0, 15.0, 9.0, 0.5, key="fcff_wacc") / 100
        
        st.markdown("#### Capital Structure")
        total_debt = st.number_input("Total Debt ($M)", value=1000.0, step=50.0, key="fcff_debt")
        shares_outstanding = st.number_input("Shares Outstanding (M)", value=100.0, step=5.0, key="fcff_shares")
    
    with col2:
        # Calculate FCFF
        ebit_after_tax = ebit * (1 - tax_rate)
        fcff = ebit_after_tax + depreciation - capex - nwc_increase
        
        st.markdown(f"""
        <div class="concept-box">
        <h4>FCFF Calculation</h4>
        <p>EBIT × (1 - Tax): ${ebit_after_tax:.2f}M</p>
        <p>+ Depreciation: ${depreciation:.2f}M</p>
        <p>- CapEx: ${capex:.2f}M</p>
        <p>- Δ NWC: ${nwc_increase:.2f}M</p>
        <hr>
        <p><strong>FCFF: ${fcff:.2f}M</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        if fcf_growth < wacc:
            # Enterprise value
            enterprise_value = fcff * (1 + fcf_growth) / (wacc - fcf_growth)
            
            # Equity value
            equity_value = enterprise_value - total_debt
            
            # Price per share
            price_per_share = equity_value / shares_outstanding
            
            st.markdown(f"""
            <div class="valuation-box">
            <h3>Valuation Results</h3>
            <hr style="border-color: white;">
            <p><strong>Enterprise Value:</strong> ${enterprise_value:.2f}M</p>
            <p><strong>Less: Total Debt:</strong> ${total_debt:.2f}M</p>
            <p><strong>Equity Value:</strong> ${equity_value:.2f}M</p>
            <hr style="border-color: white;">
            <h2>Price per Share: ${price_per_share:.2f}</h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Market comparison
            current_market_price = st.number_input("Current Market Price", value=45.0, step=1.0, key="fcff_market")
            
            if current_market_price < price_per_share:
                diff = price_per_share - current_market_price
                diff_pct = (diff / current_market_price) * 100
                st.success(f"✅ **UNDERVALUED**: Intrinsic value ${diff:.2f} higher ({diff_pct:.1f}%)")
            elif current_market_price > price_per_share:
                diff = current_market_price - price_per_share
                diff_pct = (diff / current_market_price) * 100
                st.error(f"❌ **OVERVALUED**: Market price ${diff:.2f} higher ({diff_pct:.1f}%)")
            else:
                st.info("➡️ **FAIRLY VALUED**")
        else:
            st.error("⚠️ Growth rate must be less than WACC!")
    
    st.markdown("---")
    
    # WACC Calculator
    st.markdown("### 📊 WACC Calculator")
    
    st.markdown("""
    <div class="formula-box">
    WACC = (E/V) × Cost of Equity + (D/V) × Cost of Debt × (1 - Tax Rate)<br><br>
    Where:<br>
    E = Market value of equity<br>
    D = Market value of debt<br>
    V = E + D (Total firm value)
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        mv_equity = st.number_input("Market Value of Equity ($M)", value=2000.0, step=100.0, key="wacc_e")
        mv_debt = st.number_input("Market Value of Debt ($M)", value=1000.0, step=100.0, key="wacc_d")
        cost_equity = st.slider("Cost of Equity (%)", 5.0, 20.0, 12.0, 0.5, key="wacc_ke") / 100
        cost_debt = st.slider("Cost of Debt (%)", 2.0, 10.0, 5.0, 0.5, key="wacc_kd") / 100
        tax_rate_wacc = st.slider("Tax Rate (%)", 0.0, 50.0, 25.0, 1.0, key="wacc_tax") / 100
    
    with col2:
        total_value = mv_equity + mv_debt
        weight_equity = mv_equity / total_value
        weight_debt = mv_debt / total_value
        
        wacc_calc = (weight_equity * cost_equity) + (weight_debt * cost_debt * (1 - tax_rate_wacc))
        
        st.markdown(f"""
        <div class="valuation-box">
        <h2>WACC: {wacc_calc:.2%}</h2>
        <hr style="border-color: white;">
        <p><strong>Weights:</strong></p>
        <p>Equity: {weight_equity:.1%} × {cost_equity:.2%} = {weight_equity * cost_equity:.2%}</p>
        <p>Debt: {weight_debt:.1%} × {cost_debt:.2%} × {1 - tax_rate_wacc:.2f} = {weight_debt * cost_debt * (1 - tax_rate_wacc):.2%}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Pie chart of capital structure
        fig = go.Figure(data=[go.Pie(
            labels=['Equity', 'Debt'],
            values=[mv_equity, mv_debt],
            marker=dict(colors=['#028090', '#F96167']),
            textinfo='label+percent',
            hovertemplate='<b>%{label}</b><br>Value: $%{value:.0f}M<br>Weight: %{percent}<extra></extra>'
        )])
        fig.update_layout(title="Capital Structure", height=400)
        st.plotly_chart(fig, use_container_width=True)

def show_model_comparison():
    st.markdown('<div class="section-header">🔍 Valuation Model Comparison</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Comparing Valuation Approaches
    
    Different valuation models can yield different results. Understanding when to use each is crucial.
    """)
    
    # Model comparison table
    comparison_data = {
        'Model': ['Dividend Discount Model (DDM)', 'P/E Ratio Analysis', 
                 'Free Cash Flow to Firm', 'Free Cash Flow to Equity'],
        'Best For': [
            'Mature, dividend-paying stocks',
            'Quick comparisons, peer analysis',
            'All companies, especially non-dividend payers',
            'Leveraged companies'
        ],
        'Key Advantage': [
            'Theoretically sound, based on cash to shareholders',
            'Simple, easy to understand',
            'Captures total firm value',
            'Direct equity valuation'
        ],
        'Main Limitation': [
            'Not applicable to non-dividend stocks',
            'Ignores growth differences',
            'Requires detailed financial data',
            'Sensitive to leverage assumptions'
        ],
        'Discount Rate': [
            'Cost of Equity (k)',
            'Implied from comparables',
            'WACC',
            'Cost of Equity (k)'
        ]
    }
    
    comparison_df = pd.DataFrame(comparison_data)
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Side-by-side comparison
    st.markdown("### 🔬 Multi-Model Valuation")
    
    st.markdown("Let's value the same company using different methods:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Company Data")
        current_div = st.number_input("Current Dividend", value=2.50, step=0.1, key="comp_div")
        eps_multi = st.number_input("Earnings Per Share", value=5.00, step=0.5, key="comp_eps")
        fcfe_per_share = st.number_input("FCFE per Share", value=6.00, step=0.5, key="comp_fcfe")
        growth_multi = st.slider("Growth Rate (%)", 2.0, 15.0, 6.0, 0.5, key="comp_g") / 100
        required_return = st.slider("Required Return (%)", 8.0, 15.0, 10.0, 0.5, key="comp_k") / 100
        
        st.markdown("#### Comparables (for P/E)")
        industry_pe = st.number_input("Industry Average P/E", value=18.0, step=1.0, key="comp_pe")
    
    with col2:
        st.markdown("#### Valuation Results")
        
        # DDM
        if growth_multi < required_return:
            d1 = current_div * (1 + growth_multi)
            ddm_value = d1 / (required_return - growth_multi)
        else:
            ddm_value = 0
        
        # P/E Method
        pe_value = eps_multi * industry_pe
        
        # FCFE Method
        if growth_multi < required_return:
            fcfe_next = fcfe_per_share * (1 + growth_multi)
            fcfe_value = fcfe_next / (required_return - growth_multi)
        else:
            fcfe_value = 0
        
        valuation_results = pd.DataFrame({
            'Model': ['DDM (Gordon)', 'P/E Comparable', 'FCFE'],
            'Value per Share': [f'${ddm_value:.2f}', f'${pe_value:.2f}', f'${fcfe_value:.2f}']
        })
        
        st.dataframe(valuation_results, use_container_width=True, hide_index=True)
        
        # Average
        values = [ddm_value, pe_value, fcfe_value]
        avg_value = np.mean([v for v in values if v > 0])
        min_value = min([v for v in values if v > 0])
        max_value = max([v for v in values if v > 0])
        
        st.markdown(f"""
        <div class="concept-box">
        <h4>Valuation Range</h4>
        <p><strong>Low:</strong> ${min_value:.2f}</p>
        <p><strong>Average:</strong> ${avg_value:.2f}</p>
        <p><strong>High:</strong> ${max_value:.2f}</p>
        <p><strong>Range:</strong> ${max_value - min_value:.2f}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Visualization
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['DDM', 'P/E', 'FCFE', 'Average'],
            y=[ddm_value, pe_value, fcfe_value, avg_value],
            marker_color=['#028090', '#97BC62', '#F96167', '#1E2761'],
            text=[f'${v:.2f}' for v in [ddm_value, pe_value, fcfe_value, avg_value]],
            textposition='auto'
        ))
        fig.update_layout(
            title="Valuation Comparison",
            yaxis_title="Value per Share ($)",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Best practices
    st.markdown("### 💡 Best Practices in Equity Valuation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="concept-box">
        <h4>✅ Do:</h4>
        <ul>
        <li>Use multiple valuation methods</li>
        <li>Triangulate to a reasonable range</li>
        <li>Consider company lifecycle stage</li>
        <li>Perform sensitivity analysis</li>
        <li>Check assumptions carefully</li>
        <li>Use realistic growth rates</li>
        <li>Compare to peers</li>
        <li>Update valuations regularly</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="concept-box">
        <h4>❌ Don't:</h4>
        <ul>
        <li>Rely on a single model</li>
        <li>Use unrealistic assumptions</li>
        <li>Ignore terminal value sensitivity</li>
        <li>Apply DDM to non-dividend stocks</li>
        <li>Ignore quality of earnings</li>
        <li>Use historical P/E blindly</li>
        <li>Forget about risk differences</li>
        <li>Ignore industry dynamics</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.warning("⚠️ **Remember:** All models are wrong, but some are useful. Valuation is an art as much as a science!")

def show_quiz():
    st.markdown('<div class="section-header">✅ Test Your Knowledge</div>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'ch13_score' not in st.session_state:
        st.session_state.ch13_score = 0
    if 'ch13_submitted' not in st.session_state:
        st.session_state.ch13_submitted = set()
    
    # Question 1
    st.markdown("### Question 1: Gordon Growth Model")
    st.markdown("In the Gordon Growth Model, if the required return increases, the stock price will:")
    
    q1 = st.radio("",
                 ["A) Increase", "B) Decrease", "C) Stay the same", "D) It depends on the dividend"],
                 key="q1", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q1_btn") and "q1" not in st.session_state.ch13_submitted:
        st.session_state.ch13_submitted.add("q1")
        if q1 == "B) Decrease":
            st.success("✅ Correct! Higher k (denominator) → Lower value")
            st.session_state.ch13_score += 1
        else:
            st.error("❌ Incorrect. V₀ = D₁/(k-g). Higher k means lower value.")
    
    st.markdown("---")
    
    # Question 2
    st.markdown("### Question 2: Growth Rate")
    st.markdown("Sustainable growth rate equals:")
    
    q2 = st.radio("",
                 ["A) ROE × Payout Ratio", "B) ROE × Plowback Ratio",
                  "C) Dividend / Price", "D) Earnings / Assets"],
                 key="q2", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q2_btn") and "q2" not in st.session_state.ch13_submitted:
        st.session_state.ch13_submitted.add("q2")
        if q2 == "B) ROE × Plowback Ratio":
            st.success("✅ Correct! g = ROE × b, where b is the retention/plowback ratio")
            st.session_state.ch13_score += 1
        else:
            st.error("❌ Incorrect. g = ROE × Plowback Ratio")
    
    st.markdown("---")
    
    # Question 3
    st.markdown("### Question 3: P/E Ratio")
    st.markdown("According to the DDM, higher growth rates lead to:")
    
    q3 = st.radio("",
                 ["A) Lower P/E ratios", "B) Higher P/E ratios",
                  "C) No change in P/E", "D) Lower stock prices"],
                 key="q3", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q3_btn") and "q3" not in st.session_state.ch13_submitted:
        st.session_state.ch13_submitted.add("q3")
        if q3 == "B) Higher P/E ratios":
            st.success("✅ Correct! P/E = (1-b)/(k-g). Higher g → Higher P/E")
            st.session_state.ch13_score += 1
        else:
            st.error("❌ Incorrect. Higher growth increases P/E ratios.")
    
    st.markdown("---")
    
    # Question 4
    st.markdown("### Question 4: Free Cash Flow")
    st.markdown("FCFF is discounted using:")
    
    q4 = st.radio("",
                 ["A) Cost of Equity", "B) Cost of Debt",
                  "C) WACC", "D) Risk-free rate"],
                 key="q4", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q4_btn") and "q4" not in st.session_state.ch13_submitted:
        st.session_state.ch13_submitted.add("q4")
        if q4 == "C) WACC":
            st.success("✅ Correct! FCFF goes to all investors, so use WACC")
            st.session_state.ch13_score += 1
        else:
            st.error("❌ Incorrect. FCFF is discounted at WACC; FCFE at cost of equity.")
    
    st.markdown("---")
    
    # Question 5
    st.markdown("### Question 5: Intrinsic Value")
    st.markdown("If intrinsic value > market price, you should:")
    
    q5 = st.radio("",
                 ["A) Sell the stock", "B) Buy the stock",
                  "C) Short the stock", "D) Do nothing"],
                 key="q5", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q5_btn") and "q5" not in st.session_state.ch13_submitted:
        st.session_state.ch13_submitted.add("q5")
        if q5 == "B) Buy the stock":
            st.success("✅ Correct! Stock is undervalued, so buy it!")
            st.session_state.ch13_score += 1
        else:
            st.error("❌ Incorrect. Buy when intrinsic value exceeds market price.")
    
    st.markdown("---")
    
    # Score Display
    if len(st.session_state.ch13_submitted) > 0:
        score_pct = (st.session_state.ch13_score / len(st.session_state.ch13_submitted)) * 100
        
        st.markdown(f"""
        <div class="concept-box">
        <h2>Your Score: {st.session_state.ch13_score} / {len(st.session_state.ch13_submitted)}</h2>
        <h3>{score_pct:.0f}%</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if score_pct >= 80:
            st.success("🎉 Excellent! You understand equity valuation very well.")
        elif score_pct >= 60:
            st.info("👍 Good work! Review DDM, P/E, and FCF models.")
        else:
            st.warning("📚 Keep studying! Review valuation formulas and practice calculations.")
    
    if st.button("Reset Quiz", key="reset_quiz"):
        st.session_state.ch13_score = 0
        st.session_state.ch13_submitted = set()
        st.rerun()

if __name__ == "__main__":
    main()