import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Macroeconomic & Industry Analysis",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
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
    .indicator-box {
        background-color: #CADCFC;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .cyclical-box {
        background-color: #F96167;
        padding: 1rem;
        border-radius: 8px;
        color: white;
        font-weight: bold;
    }
    .defensive-box {
        background-color: #97BC62;
        padding: 1rem;
        border-radius: 8px;
        color: white;
        font-weight: bold;
    }
    .highlight {
        background-color: #F9E795;
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Deterministic RNG for any simulated visuals
RNG = np.random.default_rng(42)


# Main App
def main():
    # Sidebar Navigation
    st.sidebar.markdown("## 📚 Navigation")
    page = st.sidebar.radio(
        "Choose a topic:",
        [
            "🏠 Home",
            "🌍 Global Economy",
            "📊 Macro Indicators",
            "📈 Business Cycles",
            "🏭 Industry Analysis",
            "🔄 Sector Rotation",
            "🔧 Industry Structure",
            "✅ Quiz",
        ],
    )

    if page == "🏠 Home":
        show_home()
    elif page == "🌍 Global Economy":
        show_global_economy()
    elif page == "📊 Macro Indicators":
        show_macro_indicators()
    elif page == "📈 Business Cycles":
        show_business_cycles()
    elif page == "🏭 Industry Analysis":
        show_industry_analysis()
    elif page == "🔄 Sector Rotation":
        show_sector_rotation()
    elif page == "🔧 Industry Structure":
        show_industry_structure()
    elif page == "✅ Quiz":
        show_quiz()


def show_home():
    st.markdown(
        '<div class="main-header">🌍 Macroeconomic & Industry Analysis</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p style="text-align: center; font-size: 1.2rem; color: #666;">From Global Economy to Industry Structure</p>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
        <div class="concept-box">
        <h3 style="color: #028090;">🌍 Macro Analysis</h3>
        <p>Understand the big picture</p>
        <ul>
        <li>Global economy & exchange rates</li>
        <li>GDP, inflation, unemployment</li>
        <li>Interest rates & fiscal policy</li>
        <li>Supply & demand shocks</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="concept-box">
        <h3 style="color: #028090;">📈 Business Cycles</h3>
        <p>Timing the economy</p>
        <ul>
        <li>Peak, trough, expansion</li>
        <li>Leading indicators</li>
        <li>Coincident indicators</li>
        <li>Cyclical vs defensive industries</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class="concept-box">
        <h3 style="color: #028090;">🏭 Industry Analysis</h3>
        <p>Sector-level insights</p>
        <ul>
        <li>Industry classification (NAICS)</li>
        <li>Sector rotation strategies</li>
        <li>Industry life cycles</li>
        <li>Porter's Five Forces</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    st.markdown('<div class="section-header">📋 Chapter Overview</div>', unsafe_allow_html=True)

    st.markdown(
        """
    This interactive app covers **Macroeconomic and Industry Analysis**.

    ### Top-Down Analysis Framework:

    1. **Global Economy** → Exchange rates, international markets
    2. **Domestic Macroeconomy** → GDP, inflation, unemployment, interest rates
    3. **Industry Analysis** → Sector performance, cyclicality, structure
    4. **Individual Firm Analysis** 

    ### 🎯 Learning Objectives:

    By the end of this module, you will be able to:
    - Analyze key macroeconomic indicators and their impact on markets
    - Identify phases of business cycles using leading indicators
    - Distinguish between cyclical and defensive industries
    - Apply sector rotation strategies
    - Evaluate industry structure using Porter's Five Forces
    """
    )

    st.info("💡 **Key Insight:** Top-down analysis starts with the big picture (macro) and narrows down to industries and firms.")


def show_global_economy():
    st.markdown('<div class="section-header">🌍 Global Economy</div>', unsafe_allow_html=True)

    st.markdown(
        """
    ### Why the Global Economy Matters

    The **national economic environment** is a crucial determinant of industry and firm performance.
    Global factors affect:
    - Currency values (exchange rates)
    - International trade
    - Capital flows
    - Competitive positioning
    """
    )

    st.markdown("---")

    # Exchange Rates
    st.markdown("### 💱 Exchange Rates")

    st.markdown(
        """
    <div class="concept-box">
    <h4>Exchange Rate</h4>
    <p>The rate at which domestic currency can be converted into foreign currency.</p>
    <p><strong>Impact on stocks:</strong></p>
    <ul>
    <li><strong>Strong domestic currency:</strong> Exports more expensive, imports cheaper → Bad for exporters, good for importers</li>
    <li><strong>Weak domestic currency:</strong> Exports cheaper, imports expensive → Good for exporters, bad for importers</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Interactive Exchange Rate Impact Calculator
    st.markdown("### 📊 Exchange Rate Impact Calculator")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Company Profile")
        company_type = st.selectbox(
            "Company Type",
            ["Exporter (sells abroad)", "Importer (buys abroad)", "Domestic only"],
            key="fx_type",
        )
        export_pct = (
            st.slider("% Revenue from Exports", 0, 100, 50, 5, key="fx_exp")
            if company_type == "Exporter (sells abroad)"
            else 0
        )
        import_pct = (
            st.slider("% Costs from Imports", 0, 100, 30, 5, key="fx_imp")
            if company_type == "Importer (buys abroad)"
            else 0
        )

    with col2:
        st.markdown("#### Currency Scenario")
        fx_change = st.slider("Change in Domestic Currency (%)", -30, 30, 10, 5, key="fx_change")

        if fx_change > 0:
            fx_direction = "Appreciation (Stronger)"
            fx_color = "#028090"
        elif fx_change < 0:
            fx_direction = "Depreciation (Weaker)"
            fx_color = "#F96167"
        else:
            fx_direction = "Unchanged"
            fx_color = "#97BC62"

        st.markdown(
            f"""
        <div class="concept-box" style="background-color: {fx_color}; color: white;">
        <h4>Currency Movement</h4>
        <p><strong>{fx_change:+.0f}%</strong> - {fx_direction}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # Calculate impact
    if company_type == "Exporter (sells abroad)":
        revenue_impact = -(fx_change / 100) * (export_pct / 100)
        explanation = (
            f"Export revenue decreases by {abs(revenue_impact)*100:.1f}% when converted to domestic currency"
            if fx_change > 0
            else f"Export revenue increases by {abs(revenue_impact)*100:.1f}% when converted to domestic currency"
        )
    elif company_type == "Importer (buys abroad)":
        cost_impact = -(fx_change / 100) * (import_pct / 100)
        revenue_impact = -cost_impact  # Lower costs = higher profit
        explanation = (
            f"Import costs decrease by {abs(cost_impact)*100:.1f}%, improving profit margin"
            if fx_change > 0
            else f"Import costs increase by {abs(cost_impact)*100:.1f}%, squeezing profit margin"
        )
    else:
        revenue_impact = 0
        explanation = "Domestic-only company is not directly affected by exchange rates"

    st.markdown(
        f"""
    <div class="concept-box">
    <h4>Impact Analysis</h4>
    <p><strong>Expected profit impact:</strong> {revenue_impact*100:+.2f}%</p>
    <p>{explanation}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # International Market Performance
    st.markdown("### 🌐 International Market Performance")

    st.markdown(
        """
    Different countries' stock markets can have vastly different returns due to:
    - Local economic conditions
    - Political stability
    - Currency movements
    - Sector composition
    """
    )

    # Sample international returns (illustrative)
    countries = ["India", "Brazil", "Canada", "Japan", "UK", "Germany", "China", "USA"]
    returns_2016 = [2.9, 38.9, 21.1, 0.4, 14.4, 6.9, -11.4, 12.0]

    fig = go.Figure()
    colors = ["#97BC62" if r > 0 else "#F96167" for r in returns_2016]
    fig.add_trace(go.Bar(x=countries, y=returns_2016, marker_color=colors))
    fig.update_layout(
        title="Sample International Stock Market Returns (%)",
        xaxis_title="Country",
        yaxis_title="Return (%)",
        height=400,
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)

    st.warning("⚠️ **Key Takeaway:** International diversification can reduce portfolio risk but adds currency risk.")


def show_macro_indicators():
    st.markdown('<div class="section-header">📊 Macroeconomic Indicators</div>', unsafe_allow_html=True)

    st.markdown("Key macroeconomic variables that affect stock market performance:")

    tab1, tab2, tab3, tab4 = st.tabs(["GDP & Growth", "Unemployment & Inflation", "Interest Rates", "Fiscal Policy"])

    with tab1:
        st.markdown("### 📈 Gross Domestic Product (GDP)")

        st.markdown(
            """
        <div class="concept-box">
        <h4>GDP Definition</h4>
        <p><strong>Gross Domestic Product (GDP)</strong>: Market value of all goods and services produced over a period of time.</p>
        <p><strong>Relationship with stocks:</strong></p>
        <ul>
        <li>Higher GDP growth → Higher corporate earnings → Higher stock prices</li>
        <li>GDP growth is correlated with stock market returns</li>
        <li>Stock market often leads GDP (stocks are a leading indicator)</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("#### GDP Growth Impact Simulator")

        col1, col2 = st.columns(2)

        with col1:
            gdp_growth = st.slider("GDP Growth Rate (%)", -5.0, 8.0, 2.5, 0.5, key="gdp_growth")
            earnings_sensitivity = st.slider("Earnings Sensitivity to GDP", 0.5, 2.0, 1.5, 0.1, key="gdp_sens")

        with col2:
            expected_earnings_growth = gdp_growth * earnings_sensitivity

            if gdp_growth > 3:
                scenario = "Strong Expansion"
                color = "#97BC62"
                text_color = "black"
            elif gdp_growth > 0:
                scenario = "Modest Growth"
                color = "#028090"
                text_color = "white"
            elif gdp_growth > -2:
                scenario = "Mild Recession"
                color = "#F9E795"
                text_color = "black"
            else:
                scenario = "Severe Recession"
                color = "#F96167"
                text_color = "white"

            st.markdown(
                f"""
            <div class="concept-box" style="background-color: {color}; color: {text_color};">
            <h4>Economic Scenario: {scenario}</h4>
            <p><strong>GDP Growth:</strong> {gdp_growth:.1f}%</p>
            <p><strong>Expected Earnings Growth:</strong> {expected_earnings_growth:.1f}%</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with tab2:
        st.markdown("### 💼 Unemployment & Inflation")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                """
            <div class="indicator-box">
            <h4>📉 Unemployment Rate</h4>
            <p><strong>Definition:</strong> Ratio of unemployed to total labor force</p>
            <p><strong>Impact:</strong></p>
            <ul>
            <li>Low unemployment → Strong consumer spending</li>
            <li>High unemployment → Weak consumer demand</li>
            <li>Natural rate: ~4-5%</li>
            </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                """
            <div class="indicator-box">
            <h4>📊 Inflation Rate</h4>
            <p><strong>Definition:</strong> Rate at which general price level rises</p>
            <p><strong>Impact:</strong></p>
            <ul>
            <li>Moderate inflation (2-3%): Healthy</li>
            <li>High inflation: Erodes real returns</li>
            <li>Deflation: Signals weak demand</li>
            </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

        st.markdown("---")

        st.markdown("#### The Phillips Curve Trade-off")

        unemployment = np.linspace(2, 10, 50)
        inflation = 8 - 0.6 * unemployment + RNG.normal(0, 0.3, 50)

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=unemployment,
                y=inflation,
                mode="markers",
                marker=dict(size=8, color="#028090"),
            )
        )
        fig.update_layout(
            title="Phillips Curve: Inflation vs Unemployment",
            xaxis_title="Unemployment Rate (%)",
            yaxis_title="Inflation Rate (%)",
            height=400,
        )
        st.plotly_chart(fig, use_container_width=True)

        st.info(
            "💡 **Traditional view:** Inverse relationship between unemployment and inflation (though this relationship has weakened in recent decades)"
        )

    with tab3:
        st.markdown("### 💰 Interest Rates")

        st.markdown(
            """
        <div class="concept-box">
        <h4>Why Interest Rates Matter</h4>
        <p><strong>Impact on stocks:</strong></p>
        <ol>
        <li><strong>Discount rate effect:</strong> Higher rates reduce present value of future cash flows</li>
        <li><strong>Competition for capital:</strong> Bonds become more attractive relative to stocks</li>
        <li><strong>Economic activity:</strong> Higher rates slow borrowing and spending</li>
        <li><strong>Corporate costs:</strong> Higher rates increase debt service costs</li>
        </ol>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("#### Interest Rate Factors")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                """
            **Supply-side:**
            - Household savings
            - Business retained earnings
            - Government budget surplus/deficit
            - Foreign investment
            """
            )

        with col2:
            st.markdown(
                """
            **Demand-side:**
            - Business investment needs
            - Consumer borrowing
            - Government borrowing
            - Expected inflation
            """
            )

        st.markdown("#### Interest Rate Impact Calculator")

        col1, col2 = st.columns(2)

        with col1:
            current_rate = st.slider("Current Interest Rate (%)", 0.0, 10.0, 5.0, 0.5, key="int_curr")
            new_rate = st.slider("New Interest Rate (%)", 0.0, 10.0, 6.0, 0.5, key="int_new")
            stock_pe = st.number_input("Stock P/E Ratio", value=20.0, step=1.0, key="int_pe")

        with col2:
            rate_change = new_rate - current_rate

            earnings_yield = (1 / stock_pe) * 100 if stock_pe > 0 else 0.0

            equity_risk_premium = earnings_yield - current_rate
            new_equity_risk_premium = earnings_yield - new_rate

            # Rough estimate of price impact (guard against divide-by-zero)
            price_impact = -(rate_change / current_rate) * 0.5 if current_rate > 0 else 0

            st.markdown(
                f"""
            <div class="concept-box">
            <h4>Analysis</h4>
            <p><strong>Rate Change:</strong> {rate_change:+.1f}%</p>
            <p><strong>Equity Risk Premium:</strong></p>
            <p>Before: {equity_risk_premium:.2f}%</p>
            <p>After: {new_equity_risk_premium:.2f}%</p>
            <hr>
            <p><strong>Est. Stock Price Impact:</strong> {price_impact*100:.1f}%</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

            if rate_change > 0:
                st.error("❌ Rising rates typically pressure stock valuations")
            elif rate_change < 0:
                st.success("✅ Falling rates typically support stock valuations")
            else:
                st.info("ℹ️ No rate change in this scenario")

    with tab4:
        st.markdown("### 🏛️ Fiscal & Monetary Policy")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                """
            <div class="indicator-box">
            <h4>Fiscal Policy</h4>
            <p><strong>Tools:</strong></p>
            <ul>
            <li>Government spending</li>
            <li>Taxation</li>
            </ul>
            <p><strong>Expansionary (Stimulus):</strong></p>
            <ul>
            <li>↑ Spending or ↓ Taxes</li>
            <li>Stimulates economy</li>
            <li>May increase deficit</li>
            </ul>
            <p><strong>Contractionary:</strong></p>
            <ul>
            <li>↓ Spending or ↑ Taxes</li>
            <li>Cools overheated economy</li>
            <li>Reduces deficit</li>
            </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                """
            <div class="indicator-box">
            <h4>Monetary Policy</h4>
            <p><strong>Tools:</strong></p>
            <ul>
            <li>Interest rates (Policy Rate)</li>
            <li>Open market operations</li>
            <li>Reserve requirements</li>
            </ul>
            <p><strong>Expansionary (Easing):</strong></p>
            <ul>
            <li>↓ Interest rates</li>
            <li>↑ Money supply</li>
            <li>Stimulates borrowing</li>
            </ul>
            <p><strong>Contractionary (Tightening):</strong></p>
            <ul>
            <li>↑ Interest rates</li>
            <li>↓ Money supply</li>
            <li>Reduces inflation</li>
            </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

        st.markdown("---")

        st.markdown("#### Policy Mix Analyzer")

        fiscal = st.select_slider(
            "Fiscal Policy Stance",
            options=["Very Contractionary", "Contractionary", "Neutral", "Expansionary", "Very Expansionary"],
            value="Neutral",
            key="policy_fiscal",
        )
        monetary = st.select_slider(
            "Monetary Policy Stance",
            options=["Very Tight", "Tight", "Neutral", "Easy", "Very Easy"],
            value="Neutral",
            key="policy_mon",
        )

        fiscal_score = ["Very Contractionary", "Contractionary", "Neutral", "Expansionary", "Very Expansionary"].index(
            fiscal
        ) - 2
        monetary_score = ["Very Tight", "Tight", "Neutral", "Easy", "Very Easy"].index(monetary) - 2
        overall_score = fiscal_score + monetary_score

        if overall_score >= 3:
            overall = "Highly Stimulative"
            color = "#97BC62"
            impact = "Strong positive for stocks"
        elif overall_score >= 1:
            overall = "Moderately Stimulative"
            color = "#028090"
            impact = "Positive for stocks"
        elif overall_score <= -3:
            overall = "Highly Restrictive"
            color = "#F96167"
            impact = "Negative for stocks"
        elif overall_score <= -1:
            overall = "Moderately Restrictive"
            color = "#F9E795"
            impact = "Slightly negative for stocks"
        else:
            overall = "Neutral"
            color = "#CADCFC"
            impact = "Mixed for stocks"

        st.markdown(
            f"""
        <div class="concept-box" style="background-color: {color};">
        <h4>Overall Policy Stance: {overall}</h4>
        <p><strong>Expected Market Impact:</strong> {impact}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )


def show_business_cycles():
    st.markdown('<div class="section-header">📈 Business Cycles</div>', unsafe_allow_html=True)

    st.markdown(
        """
    ### Understanding Business Cycles

    **Business cycles** are recurring patterns of economic expansion and contraction.
    """
    )

    st.markdown(
        """
    <div class="concept-box">
    <h4>Four Phases of the Business Cycle</h4>
    <ol>
    <li><strong>Peak:</strong> Economy at maximum output, unemployment low, inflation risk</li>
    <li><strong>Contraction (Recession):</strong> Economic activity declines, unemployment rises</li>
    <li><strong>Trough:</strong> Economy bottoms out, transition point to recovery</li>
    <li><strong>Expansion (Recovery):</strong> Economic activity increases, employment rises</li>
    </ol>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📊 Stylized Business Cycle")

    time = np.linspace(0, 10, 200)
    gdp_trend = 2 + 0.3 * time
    gdp_cycle = gdp_trend + 2 * np.sin(time * 1.5)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=time, y=gdp_trend, mode="lines", name="Long-term Trend", line=dict(color="#028090", dash="dash", width=2))
    )
    fig.add_trace(go.Scatter(x=time, y=gdp_cycle, mode="lines", name="Actual GDP", line=dict(color="#1E2761", width=3)))

    fig.add_annotation(x=1.0, y=3.8, text="Peak", showarrow=True, arrowhead=2)
    fig.add_annotation(x=3.1, y=2.0, text="Trough", showarrow=True, arrowhead=2)
    fig.add_annotation(x=5.2, y=5.8, text="Peak", showarrow=True, arrowhead=2)
    fig.add_annotation(x=7.3, y=3.5, text="Trough", showarrow=True, arrowhead=2)

    fig.update_layout(
        title="Business Cycle: GDP Over Time",
        xaxis_title="Time",
        yaxis_title="GDP Level",
        height=500,
        showlegend=True,
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.markdown("### 🎯 Economic Indicators")

    tab1, tab2, tab3 = st.tabs(["Leading Indicators", "Coincident Indicators", "Lagging Indicators"])

    with tab1:
        st.markdown("#### Leading Indicators")
        st.markdown("Economic series that tend to **rise or fall in advance** of the rest of the economy.")

        leading_indicators = [
            ("📊 Stock Prices (S&P 500)", "Market anticipates future earnings"),
            ("🏗️ Building Permits", "New housing construction leads economic activity"),
            ("📦 Manufacturers' New Orders", "Future production activity"),
            ("⏰ Average Weekly Hours", "Employers adjust hours before hiring/firing"),
            ("📉 Initial Unemployment Claims", "Early sign of job market weakness"),
            ("📈 Yield Curve Spread", "10-year minus policy rate"),
            ("💰 Money Supply (M2)", "Liquidity in the economy"),
            ("🎭 Consumer Expectations", "Consumer confidence about future"),
            ("🏭 ISM New Orders Index", "Manufacturing demand"),
        ]

        for indicator, description in leading_indicators:
            st.markdown(
                f"""
            <div class="indicator-box">
            <p><strong>{indicator}</strong></p>
            <p style="font-size: 0.9rem;">{description}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        st.success("✅ **Use leading indicators** to anticipate turning points in the business cycle")

    with tab2:
        st.markdown("#### Coincident Indicators")
        st.markdown("Economic series that tend to **move in tandem** with the overall economy.")

        coincident_indicators = [
            ("👥 Nonfarm Employment", "Current job market"),
            ("💵 Personal Income", "Current earning power"),
            ("🏭 Industrial Production", "Current manufacturing output"),
            ("🛒 Manufacturing & Trade Sales", "Current business activity"),
        ]

        for indicator, description in coincident_indicators:
            st.markdown(
                f"""
            <div class="indicator-box">
            <p><strong>{indicator}</strong></p>
            <p style="font-size: 0.9rem;">{description}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        st.info("ℹ️ **Use coincident indicators** to confirm the current state of the economy")

    with tab3:
        st.markdown("#### Lagging Indicators")
        st.markdown("Economic series that tend to **change after** the economy has changed.")

        lagging_indicators = [
            ("⏱️ Unemployment Duration", "How long people stay unemployed"),
            ("📦 Inventory/Sales Ratio", "Businesses adjust inventories slowly"),
            ("💼 Labor Cost per Unit", "Wages adjust with a lag"),
            ("💳 Consumer Credit/Income", "Credit changes after economic conditions"),
            ("🏦 Prime Rate", "Banks adjust rates after policy moves"),
            ("🏭 Commercial Loans", "Business borrowing lags activity"),
            ("💰 CPI for Services", "Service prices adjust slowly"),
        ]

        for indicator, description in lagging_indicators:
            st.markdown(
                f"""
            <div class="indicator-box">
            <p><strong>{indicator}</strong></p>
            <p style="font-size: 0.9rem;">{description}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        st.warning("⚠️ **Use lagging indicators** to confirm the economy has already turned")

    st.markdown("---")

    st.markdown("### 🎢 Cyclical vs Defensive Industries")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div class="cyclical-box">
        <h4>🎢 Cyclical Industries</h4>
        <p><strong>Above-average</strong> sensitivity to economy</p>
        <p><strong>Examples:</strong></p>
        <ul>
        <li>Automobiles</li>
        <li>Construction</li>
        <li>Steel</li>
        <li>Airlines</li>
        <li>Luxury goods</li>
        <li>Technology</li>
        </ul>
        <p><strong>Performance:</strong> Outperform in expansions, underperform in recessions</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="defensive-box">
        <h4>🛡️ Defensive Industries</h4>
        <p><strong>Below-average</strong> sensitivity to economy</p>
        <p><strong>Examples:</strong></p>
        <ul>
        <li>Utilities</li>
        <li>Food & beverages</li>
        <li>Healthcare</li>
        <li>Consumer staples</li>
        <li>Tobacco</li>
        <li>Pharmaceuticals</li>
        </ul>
        <p><strong>Performance:</strong> Stable performance throughout cycle</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("#### Performance Simulation")

    cycle_phase = st.select_slider(
        "Business Cycle Phase",
        options=["Deep Recession", "Recession", "Early Expansion", "Mid Expansion", "Late Expansion", "Peak"],
        value="Mid Expansion",
        key="cycle_phase",
    )

    phase_scores = {
        "Deep Recession": (-15, 5),
        "Recession": (-8, 3),
        "Early Expansion": (12, 4),
        "Mid Expansion": (18, 6),
        "Late Expansion": (10, 5),
        "Peak": (5, 4),
    }

    cyclical_return, defensive_return = phase_scores[cycle_phase]

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=["Cyclical Industries", "Defensive Industries"],
            y=[cyclical_return, defensive_return],
            marker_color=["#F96167" if cyclical_return < 0 else "#028090", "#97BC62"],
        )
    )
    fig.update_layout(
        title=f"Expected Returns in {cycle_phase}",
        yaxis_title="Expected Return (%)",
        height=400,
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)


def show_industry_analysis():
    st.markdown('<div class="section-header">🏭 Industry Analysis</div>', unsafe_allow_html=True)

    st.markdown("After analyzing the macroeconomy, the next step is to analyze specific **industries** or **sectors**.")

    st.markdown("### 📋 Industry Classification: NAICS")

    st.markdown(
        """
    <div class="concept-box">
    <h4>NAICS: North American Industry Classification System</h4>
    <p>Classification system that groups firms into industries using numerical codes.</p>
    <p><strong>Hierarchy:</strong></p>
    <ul>
    <li><strong>2-digit:</strong> Sector (e.g., 31-33 = Manufacturing)</li>
    <li><strong>3-digit:</strong> Subsector (e.g., 334 = Computer & Electronic Products)</li>
    <li><strong>4-digit:</strong> Industry Group (e.g., 3341 = Computer & Peripheral Equipment)</li>
    <li><strong>5-digit:</strong> Industry (e.g., 33411 = Computer & Peripheral Equipment Manufacturing)</li>
    <li><strong>6-digit:</strong> National Industry (most detailed)</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    naics_examples = pd.DataFrame(
        {
            "NAICS Code": ["11", "23", "31-33", "42", "44-45", "48-49", "51", "52", "54", "62", "71", "72"],
            "Sector": [
                "Agriculture, Forestry, Fishing",
                "Construction",
                "Manufacturing",
                "Wholesale Trade",
                "Retail Trade",
                "Transportation & Warehousing",
                "Information",
                "Finance & Insurance",
                "Professional Services",
                "Health Care",
                "Arts & Entertainment",
                "Accommodation & Food Services",
            ],
        }
    )

    st.dataframe(naics_examples, use_container_width=True, hide_index=True)

    st.markdown("---")

    st.markdown("### 📊 Industry Performance Comparison")

    industries = [
        "Biotech",
        "Airlines",
        "Aerospace",
        "Asset Mgmt",
        "Auto Mfg",
        "Banks",
        "Chemicals",
        "Food Products",
        "Healthcare",
        "Hotels",
        "Oil & Gas",
        "Pharma",
        "Railroads",
        "Restaurants",
        "Software",
        "Telecom",
        "Tobacco",
        "Trucking",
        "Utilities",
        "Construction",
    ]
    returns = [69.9, 89.2, 54.7, 45.5, 37.8, 34.0, 33.8, 32.5, 37.0, 35.7, 18.9, 30.7, 39.7, 27.2, 30.9, 19.9, 11.9, 24.4, 7.5, 30.3]

    sorted_indices = np.argsort(returns)[::-1]
    sorted_industries = [industries[i] for i in sorted_indices]
    sorted_returns = [returns[i] for i in sorted_indices]

    colors = [
        "#97BC62" if r > 30 else "#028090" if r > 15 else "#F9E795" if r > 0 else "#F96167"
        for r in sorted_returns
    ]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=sorted_returns, y=sorted_industries, orientation="h", marker_color=colors))
    fig.update_layout(
        title="Sample Industry Returns (%)",
        xaxis_title="Return (%)",
        yaxis_title="Industry",
        height=600,
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)

    st.info("💡 **Key Insight:** Industry selection can have a huge impact on portfolio returns!")

    st.markdown("---")

    st.markdown("### 🎯 Industry Sensitivity Analysis")

    st.markdown("Three factors determine industry sensitivity to the business cycle:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
        <div class="concept-box">
        <h4>1️⃣ Sales Sensitivity</h4>
        <p>How much do sales fluctuate with the economy?</p>
        <ul>
        <li><strong>High:</strong> Luxury goods, durables</li>
        <li><strong>Low:</strong> Necessities, staples</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="concept-box">
        <h4>2️⃣ Operating Leverage</h4>
        <p>Fixed vs variable costs</p>
        <ul>
        <li><strong>High:</strong> Airlines, steel (high fixed costs)</li>
        <li><strong>Low:</strong> Retail, services</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class="concept-box">
        <h4>3️⃣ Financial Leverage</h4>
        <p>Amount of debt financing</p>
        <ul>
        <li><strong>High:</strong> Utilities, real estate</li>
        <li><strong>Low:</strong> Tech, healthcare</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("#### Calculate Industry Cyclicality Score")

    col1, col2 = st.columns(2)

    with col1:
        sales_sens = st.slider("Sales Sensitivity (1=low, 5=high)", 1, 5, 3, key="ind_sales")
        operating_lev = st.slider("Operating Leverage (1=low, 5=high)", 1, 5, 3, key="ind_op")
        financial_lev = st.slider("Financial Leverage (1=low, 5=high)", 1, 5, 3, key="ind_fin")

    with col2:
        cyclicality_score = (sales_sens + operating_lev + financial_lev) / 3

        if cyclicality_score >= 4:
            classification = "Highly Cyclical"
            color = "#F96167"
            recommendation = "Overweight in expansions, underweight in recessions"
        elif cyclicality_score >= 3:
            classification = "Moderately Cyclical"
            color = "#F9E795"
            recommendation = "Neutral allocation, adjust tactically"
        else:
            classification = "Defensive"
            color = "#97BC62"
            recommendation = "Overweight in recessions, underweight in strong expansions"

        st.markdown(
            f"""
        <div class="concept-box" style="background-color: {color};">
        <h4>Industry Classification</h4>
        <p><strong>Cyclicality Score:</strong> {cyclicality_score:.2f}/5</p>
        <p><strong>Classification:</strong> {classification}</p>
        <hr>
        <p><strong>Investment Strategy:</strong></p>
        <p>{recommendation}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )


def show_sector_rotation():
    st.markdown('<div class="section-header">🔄 Sector Rotation</div>', unsafe_allow_html=True)

    st.markdown(
        """
    ### What is Sector Rotation?

    **Sector rotation** is an investment strategy that involves shifting portfolio allocations
    among industry sectors based on **macroeconomic forecasts** and **business cycle stages**.
    """
    )

    st.markdown(
        """
    <div class="concept-box">
    <h4>The Sector Rotation Strategy</h4>
    <ol>
    <li>Identify the current phase of the business cycle</li>
    <li>Forecast the next phase</li>
    <li>Overweight sectors that typically outperform in the next phase</li>
    <li>Underweight sectors that typically underperform</li>
    </ol>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown("### 🎯 Classic Sector Rotation Model")

    cycle_phases = ["Early\nRecession", "Full\nRecession", "Early\nRecovery", "Full\nRecovery", "Early\nExpansion", "Late\nExpansion"]

    sector_performance = {
        "Early\nRecession": {"Best": ["Utilities", "Consumer Staples", "Healthcare"], "Avoid": ["Technology", "Industrials", "Materials"]},
        "Full\nRecession": {"Best": ["Healthcare", "Consumer Staples", "Utilities"], "Avoid": ["Energy", "Financials", "Industrials"]},
        "Early\nRecovery": {"Best": ["Financials", "Industrials", "Technology"], "Avoid": ["Utilities", "Consumer Staples", "Healthcare"]},
        "Full\nRecovery": {"Best": ["Technology", "Industrials", "Materials"], "Avoid": ["Utilities", "Consumer Staples", "Energy"]},
        "Early\nExpansion": {"Best": ["Industrials", "Materials", "Energy"], "Avoid": ["Utilities", "Financials", "Healthcare"]},
        "Late\nExpansion": {"Best": ["Energy", "Materials", "Technology"], "Avoid": ["Consumer Discretionary", "Financials", "Industrials"]},
    }

    st.markdown("#### Interactive Sector Rotation Wheel")

    current_phase = st.select_slider("Business Cycle Phase", options=cycle_phases, value="Full\nRecovery", key="rot_phase")

    col1, col2 = st.columns(2)

    with col1:
        best_sectors = sector_performance[current_phase]["Best"]
        st.markdown(
            f"""
        <div class="defensive-box">
        <h4>✅ Overweight These Sectors</h4>
        <ul>
        {"".join([f"<li>{sector}</li>" for sector in best_sectors])}
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        avoid_sectors = sector_performance[current_phase]["Avoid"]
        st.markdown(
            f"""
        <div class="cyclical-box">
        <h4>❌ Underweight These Sectors</h4>
        <ul>
        {"".join([f"<li>{sector}</li>" for sector in avoid_sectors])}
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    st.markdown("### 📋 Detailed Sector Rotation Guide")

    rotation_guide = {
        "Peak → Early Recession": {
            "Economic Conditions": "Growth slowing, policy tightening, inflation concerns",
            "Move Out Of": "Cyclicals: Technology, Industrials, Consumer Discretionary",
            "Move Into": "Defensives: Utilities, Consumer Staples, Healthcare",
            "Rationale": "Defensive sectors have stable earnings in downturns",
        },
        "Trough → Early Recovery": {
            "Economic Conditions": "Bottom reached, policy easing, first signs of growth",
            "Move Out Of": "Defensives: Utilities, Consumer Staples",
            "Move Into": "Early Cyclicals: Financials, Technology, Industrials",
            "Rationale": "Financials benefit from steepening yield curve, cyclicals anticipate recovery",
        },
        "Early → Mid Expansion": {
            "Economic Conditions": "Accelerating growth, rising confidence",
            "Move Out Of": "Financials (already recovered)",
            "Move Into": "Full Cyclicals: Materials, Energy, Capital Goods",
            "Rationale": "Commodity prices rise with strong growth",
        },
        "Mid → Late Expansion": {
            "Economic Conditions": "Peak growth, inflation rising, policy may tighten",
            "Move Out Of": "Interest-sensitive sectors",
            "Move Into": "Energy, Materials (inflation hedge)",
            "Rationale": "Commodities perform well with inflation",
        },
    }

    selected_transition = st.selectbox("Select Cycle Transition", list(rotation_guide.keys()), key="rot_transition")
    guide = rotation_guide[selected_transition]

    st.markdown(
        f"""
    <div class="concept-box">
    <h4>{selected_transition}</h4>
    <p><strong>Economic Conditions:</strong> {guide['Economic Conditions']}</p>
    <hr>
    <p><strong>Move Out Of:</strong> {guide['Move Out Of']}</p>
    <p><strong>Move Into:</strong> {guide['Move Into']}</p>
    <hr>
    <p><strong>Rationale:</strong> {guide['Rationale']}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.warning(
        "⚠️ **Important:** Sector rotation requires accurate economic forecasting, which is difficult. Many investors prefer diversified sector exposure."
    )


def _five_forces_figure():
    fig = go.Figure()

    # Central node
    fig.add_shape(type="circle", x0=0.42, y0=0.42, x1=0.58, y1=0.58, line=dict(color="#21295C", width=3), fillcolor="#CADCFC")
    fig.add_annotation(x=0.50, y=0.50, text="Industry<br>Profitability", showarrow=False, font=dict(size=14, color="#1E2761"))

    # Force nodes positions
    nodes = {
        "Threat of\nNew Entrants": (0.15, 0.80),
        "Rivalry Among\nExisting Firms": (0.85, 0.80),
        "Threat of\nSubstitutes": (0.15, 0.20),
        "Buyer\nPower": (0.85, 0.20),
        "Supplier\nPower": (0.50, 0.90),
    }

    for label, (x, y) in nodes.items():
        fig.add_shape(type="rect", x0=x - 0.12, y0=y - 0.06, x1=x + 0.12, y1=y + 0.06, line=dict(color="#028090", width=2), fillcolor="#F2F2F2")
        fig.add_annotation(x=x, y=y, text=label, showarrow=False, font=dict(size=12, color="#065A82"))

        # Arrows to center
        fig.add_annotation(
            x=0.50,
            y=0.50,
            ax=x,
            ay=y,
            xref="x",
            yref="y",
            axref="x",
            ayref="y",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#21295C",
        )

    fig.update_layout(
        xaxis=dict(visible=False, range=[0, 1]),
        yaxis=dict(visible=False, range=[0, 1]),
        height=360,
        margin=dict(l=10, r=10, t=30, b=10),
        title="Porter’s Five Forces (Concept Map)",
        showlegend=False,
    )
    return fig


def show_industry_structure():
    st.markdown('<div class="section-header">🔧 Industry Structure Analysis</div>', unsafe_allow_html=True)

    st.markdown(
        """
    ### Porter's Five Forces Framework

    **Michael Porter's Five Forces** is a framework for analyzing industry structure and profitability.
    """
    )

    st.markdown("### 🎯 The Five Competitive Forces")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            """
        <div class="concept-box">
        <h4>Porter's Five Forces</h4>
        <ol>
        <li><strong>Threat of New Entrants:</strong> How easy is it for new competitors to enter?</li>
        <li><strong>Rivalry Among Existing Firms:</strong> How intense is competition?</li>
        <li><strong>Threat of Substitute Products:</strong> Can customers switch to alternatives?</li>
        <li><strong>Bargaining Power of Buyers:</strong> Do customers have negotiating power?</li>
        <li><strong>Bargaining Power of Suppliers:</strong> Do suppliers have pricing power?</li>
        </ol>
        <p><strong>Goal:</strong> Industries with weak forces → Higher profitability</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.plotly_chart(_five_forces_figure(), use_container_width=True)

    st.markdown("---")

    st.markdown("### 🔍 Industry Force Analysis Tool")

    st.markdown("Rate each competitive force for your industry (1=Weak/Favorable, 5=Strong/Unfavorable):")

    col1, col2 = st.columns(2)

    with col1:
        threat_entry = st.slider(
            "1. Threat of New Entrants",
            1,
            5,
            3,
            key="force_entry",
            help="High barriers = Low threat = Good for incumbents",
        )
        rivalry = st.slider(
            "2. Rivalry Among Competitors",
            1,
            5,
            3,
            key="force_rivalry",
            help="Fragmented market = High rivalry = Bad for profitability",
        )
        threat_subs = st.slider(
            "3. Threat of Substitutes",
            1,
            5,
            3,
            key="force_subs",
            help="Few substitutes = Low threat = Good for industry",
        )

    with col2:
        buyer_power = st.slider(
            "4. Bargaining Power of Buyers",
            1,
            5,
            3,
            key="force_buyers",
            help="Concentrated buyers = High power = Bad for sellers",
        )
        supplier_power = st.slider(
            "5. Bargaining Power of Suppliers",
            1,
            5,
            3,
            key="force_suppliers",
            help="Concentrated suppliers = High power = Bad for buyers",
        )

    total_score = threat_entry + rivalry + threat_subs + buyer_power + supplier_power
    avg_score = total_score / 5

    if avg_score <= 2:
        attractiveness = "Highly Attractive"
        color = "#97BC62"
        recommendation = "Industry has strong competitive advantages. Expect high profitability."
        text_color = "black"
    elif avg_score <= 3:
        attractiveness = "Moderately Attractive"
        color = "#028090"
        recommendation = "Industry has some competitive advantages. Average profitability expected."
        text_color = "white"
    elif avg_score <= 4:
        attractiveness = "Moderately Unattractive"
        color = "#F9E795"
        recommendation = "Industry faces competitive pressures. Below-average profitability."
        text_color = "black"
    else:
        attractiveness = "Highly Unattractive"
        color = "#F96167"
        recommendation = "Industry faces severe competitive pressures. Low profitability."
        text_color = "white"

    st.markdown(
        f"""
    <div class="concept-box" style="background-color: {color}; color: {text_color};">
    <h3>Industry Attractiveness: {attractiveness}</h3>
    <p><strong>Average Force Strength:</strong> {avg_score:.2f}/5</p>
    <p>{recommendation}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    categories = ["Threat of\nEntry", "Rivalry", "Threat of\nSubstitutes", "Buyer\nPower", "Supplier\nPower"]
    values = [threat_entry, rivalry, threat_subs, buyer_power, supplier_power]

    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            name="Industry Forces",
            line_color="#028090",
        )
    )
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
        showlegend=False,
        title="Five Forces Radar Chart",
        height=500,
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.markdown("### 📊 Industry Life Cycle")

    st.markdown("Industries evolve through predictable stages:")

    stages = ["Start-up", "Consolidation", "Maturity", "Decline"]
    characteristics = {
        "Start-up": {
            "Sales Growth": "Rapid but uncertain",
            "Competition": "Many small firms",
            "Profitability": "Negative or low",
            "Risk": "Very high",
            "Investment Strategy": "High risk/high return",
        },
        "Consolidation": {
            "Sales Growth": "High and stable",
            "Competition": "Leaders emerging",
            "Profitability": "Improving",
            "Risk": "Moderate",
            "Investment Strategy": "Growth investing",
        },
        "Maturity": {
            "Sales Growth": "Slow, stable",
            "Competition": "Few large firms",
            "Profitability": "High and stable",
            "Risk": "Low",
            "Investment Strategy": "Value/dividend investing",
        },
        "Decline": {
            "Sales Growth": "Negative",
            "Competition": "Consolidating",
            "Profitability": "Declining",
            "Risk": "High",
            "Investment Strategy": "Avoid or short",
        },
    }

    selected_stage = st.selectbox("Select Industry Life Cycle Stage", stages, key="lifecycle")
    stage_info = characteristics[selected_stage]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
        <div class="concept-box">
        <h4>{selected_stage} Stage Characteristics</h4>
        <p><strong>Sales Growth:</strong> {stage_info['Sales Growth']}</p>
        <p><strong>Competition:</strong> {stage_info['Competition']}</p>
        <p><strong>Profitability:</strong> {stage_info['Profitability']}</p>
        <p><strong>Risk Level:</strong> {stage_info['Risk']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="concept-box" style="background-color: #028090; color: white;">
        <h4>Investment Strategy</h4>
        <p><strong>{stage_info['Investment Strategy']}</strong></p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    time = np.linspace(0, 10, 100)
    sales = []
    for t in time:
        if t < 2:
            s = 10 * t**2
        elif t < 5:
            s = 40 + 30 * (t - 2)
        elif t < 8:
            s = 130 + 5 * (t - 5)
        else:
            s = 145 - 10 * (t - 8)
        sales.append(max(s, 0))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=sales, mode="lines", line=dict(color="#028090", width=3)))

    fig.add_vrect(x0=0, x1=2, fillcolor="#F9E795", opacity=0.2, annotation_text="Start-up", annotation_position="top left")
    fig.add_vrect(
        x0=2, x1=5, fillcolor="#97BC62", opacity=0.2, annotation_text="Consolidation", annotation_position="top left"
    )
    fig.add_vrect(x0=5, x1=8, fillcolor="#028090", opacity=0.2, annotation_text="Maturity", annotation_position="top left")
    fig.add_vrect(x0=8, x1=10, fillcolor="#F96167", opacity=0.2, annotation_text="Decline", annotation_position="top left")

    fig.update_layout(
        title="Industry Life Cycle: Sales Over Time",
        xaxis_title="Time",
        yaxis_title="Sales",
        height=400,
        showlegend=False,
    )

    st.plotly_chart(fig, use_container_width=True)


def show_quiz():
    st.markdown('<div class="section-header">✅ Test Your Knowledge</div>', unsafe_allow_html=True)

    if "ch12_score" not in st.session_state:
        st.session_state.ch12_score = 0
    if "ch12_submitted" not in st.session_state:
        st.session_state.ch12_submitted = set()

    st.markdown("### Question 1: Exchange Rates")
    st.markdown("A U.S. company that exports products will generally benefit from:")

    q1 = st.radio(
        "",
        ["A) A stronger U.S. dollar", "B) A weaker U.S. dollar", "C) No impact from exchange rates", "D) Higher interest rates"],
        key="ch12_q1",
        label_visibility="collapsed",
    )

    if st.button("Submit Answer", key="ch12_q1_btn") and "q1" not in st.session_state.ch12_submitted:
        st.session_state.ch12_submitted.add("q1")
        if q1 == "B) A weaker U.S. dollar":
            st.success("✅ Correct! A weaker dollar makes U.S. exports cheaper for foreign buyers.")
            st.session_state.ch12_score += 1
        else:
            st.error("❌ Incorrect. Exporters benefit from a weaker domestic currency.")

    st.markdown("---")

    st.markdown("### Question 2: Leading Indicators")
    st.markdown("Which of the following is a leading economic indicator?")

    q2 = st.radio(
        "",
        ["A) Unemployment rate", "B) Industrial production", "C) Stock market prices", "D) CPI for services"],
        key="ch12_q2",
        label_visibility="collapsed",
    )

    if st.button("Submit Answer", key="ch12_q2_btn") and "q2" not in st.session_state.ch12_submitted:
        st.session_state.ch12_submitted.add("q2")
        if q2 == "C) Stock market prices":
            st.success("✅ Correct! Stock prices lead the economy by anticipating future earnings.")
            st.session_state.ch12_score += 1
        else:
            st.error("❌ Incorrect. Stock prices are a leading indicator.")

    st.markdown("---")

    st.markdown("### Question 3: Industry Classification")
    st.markdown("Cyclical industries typically include:")

    q3 = st.radio(
        "",
        ["A) Utilities and healthcare", "B) Automobiles and construction", "C) Food and beverages", "D) Pharmaceuticals"],
        key="ch12_q3",
        label_visibility="collapsed",
    )

    if st.button("Submit Answer", key="ch12_q3_btn") and "q3" not in st.session_state.ch12_submitted:
        st.session_state.ch12_submitted.add("q3")
        if q3 == "B) Automobiles and construction":
            st.success("✅ Correct! These industries are highly sensitive to economic cycles.")
            st.session_state.ch12_score += 1
        else:
            st.error("❌ Incorrect. Cyclical industries include durables like autos and construction.")

    st.markdown("---")

    st.markdown("### Question 4: Sector Rotation")
    st.markdown("In early recession, investors should typically rotate into:")

    q4 = st.radio(
        "",
        ["A) Technology and industrials", "B) Defensive sectors like utilities", "C) Energy and materials", "D) Financials"],
        key="ch12_q4",
        label_visibility="collapsed",
    )

    if st.button("Submit Answer", key="ch12_q4_btn") and "q4" not in st.session_state.ch12_submitted:
        st.session_state.ch12_submitted.add("q4")
        if q4 == "B) Defensive sectors like utilities":
            st.success("✅ Correct! Defensive sectors perform better in recessions.")
            st.session_state.ch12_score += 1
        else:
            st.error("❌ Incorrect. Rotate into defensive sectors during recessions.")

    st.markdown("---")

    st.markdown("### Question 5: Porter's Five Forces")
    st.markdown("High barriers to entry in an industry generally result in:")

    q5 = st.radio(
        "",
        ["A) Lower profitability for existing firms", "B) Higher profitability for existing firms", "C) No impact on profitability", "D) Increased competition"],
        key="ch12_q5",
        label_visibility="collapsed",
    )

    if st.button("Submit Answer", key="ch12_q5_btn") and "q5" not in st.session_state.ch12_submitted:
        st.session_state.ch12_submitted.add("q5")
        if q5 == "B) Higher profitability for existing firms":
            st.success("✅ Correct! High barriers protect incumbents from new competition.")
            st.session_state.ch12_score += 1
        else:
            st.error("❌ Incorrect. High barriers to entry benefit existing firms.")

    st.markdown("---")

    if len(st.session_state.ch12_submitted) > 0:
        score_pct = (st.session_state.ch12_score / len(st.session_state.ch12_submitted)) * 100

        st.markdown(
            f"""
        <div class="concept-box">
        <h2>Your Score: {st.session_state.ch12_score} / {len(st.session_state.ch12_submitted)}</h2>
        <h3>{score_pct:.0f}%</h3>
        </div>
        """,
            unsafe_allow_html=True,
        )

        if score_pct >= 80:
            st.success("🎉 Excellent! You understand macroeconomic and industry analysis well.")
        elif score_pct >= 60:
            st.info("👍 Good job! Review the areas where you missed questions.")
        else:
            st.warning("📚 Keep studying! Review macro indicators, business cycles, and industry analysis.")

    if st.button("Reset Quiz", key="ch12_reset_quiz"):
        st.session_state.ch12_score = 0
        st.session_state.ch12_submitted = set()
        st.rerun()


if __name__ == "__main__":
    main()
