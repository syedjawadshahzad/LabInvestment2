import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats

# Page configuration
st.set_page_config(
    page_title="Portfolio Performance Evaluation",
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
    .metric-excellent {
        background-color: #97BC62;
        padding: 1.5rem;
        border-radius: 8px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .metric-good {
        background-color: #028090;
        padding: 1.5rem;
        border-radius: 8px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .metric-poor {
        background-color: #F96167;
        padding: 1.5rem;
        border-radius: 8px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .formula-box {
        background-color: #CADCFC;
        padding: 1rem;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        margin: 1rem 0;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Helper Functions
def sharpe_ratio(returns, risk_free_rate=0.02):
    """Calculate Sharpe Ratio"""
    excess_return = np.mean(returns) - risk_free_rate
    std_dev = np.std(returns, ddof=1)
    return excess_return / std_dev if std_dev > 0 else 0

def treynor_ratio(returns, beta, risk_free_rate=0.02):
    """Calculate Treynor Ratio"""
    excess_return = np.mean(returns) - risk_free_rate
    return excess_return / beta if beta != 0 else 0

def jensens_alpha(returns, market_returns, beta, risk_free_rate=0.02):
    """Calculate Jensen's Alpha"""
    portfolio_return = np.mean(returns)
    market_return = np.mean(market_returns)
    expected_return = risk_free_rate + beta * (market_return - risk_free_rate)
    return portfolio_return - expected_return

def information_ratio(returns, benchmark_returns):
    """Calculate Information Ratio"""
    tracking_error_returns = returns - benchmark_returns
    excess_return = np.mean(tracking_error_returns)
    tracking_error = np.std(tracking_error_returns, ddof=1)
    return excess_return / tracking_error if tracking_error > 0 else 0

# Main App
def main():
    # Sidebar Navigation
    st.sidebar.markdown("## 📚 Navigation")
    page = st.sidebar.radio(
        "Choose a topic:",
        ["🏠 Home",
         "📊 Return Measures",
         "📈 Risk-Adjusted Metrics",
         "🎯 Sharpe & Treynor",
         "💎 Alpha & Information Ratio",
         "🔍 Performance Attribution",
         "⏱️ Market Timing",
         "✅ Quiz"]
    )
    
    if page == "🏠 Home":
        show_home()
    elif page == "📊 Return Measures":
        show_return_measures()
    elif page == "📈 Risk-Adjusted Metrics":
        show_risk_adjusted()
    elif page == "🎯 Sharpe & Treynor":
        show_sharpe_treynor()
    elif page == "💎 Alpha & Information Ratio":
        show_alpha_ir()
    elif page == "🔍 Performance Attribution":
        show_attribution()
    elif page == "⏱️ Market Timing":
        show_market_timing()
    elif page == "✅ Quiz":
        show_quiz()

def show_home():
    st.markdown('<div class="main-header">📊 Portfolio Performance Evaluation</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Measuring and Analyzing Portfolio Performance</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">📊 Return Metrics</h3>
        <p>Measure performance</p>
        <ul>
        <li>Arithmetic average</li>
        <li>Geometric average</li>
        <li>Dollar-weighted return</li>
        <li>Time-weighted return</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">📈 Risk-Adjusted</h3>
        <p>Account for risk</p>
        <ul>
        <li>Sharpe Ratio</li>
        <li>Treynor Ratio</li>
        <li>Jensen's Alpha</li>
        <li>Information Ratio</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">🔍 Attribution</h3>
        <p>Decompose returns</p>
        <ul>
        <li>Asset allocation</li>
        <li>Security selection</li>
        <li>Market timing</li>
        <li>Style analysis</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown('<div class="section-header">📋 Chapter Overview</div>', unsafe_allow_html=True)
    
    st.markdown("""
    This interactive app covers **Portfolio Performance Evaluation**.
    
    ### Key Questions Answered:
    
    1. **How do we measure returns?** - Time-weighted vs dollar-weighted
    2. **How do we adjust for risk?** - Sharpe, Treynor, Alpha, Information Ratio
    3. **Did the manager add value?** - Alpha and benchmark comparisons
    4. **What drove performance?** - Attribution analysis
    5. **Can managers time the market?** - Market timing evaluation
    
    ### 🎯 Learning Objectives:
    
    By the end of this module, you will be able to:
    - Calculate and interpret different return measures
    - Compute risk-adjusted performance metrics
    - Evaluate portfolio managers using Sharpe and Treynor ratios
    - Understand Jensen's Alpha and Information Ratio
    - Perform performance attribution analysis
    - Assess market timing ability
    """)
    
    st.info("💡 **Key Insight:** Raw returns don't tell the whole story. Risk-adjusted metrics reveal whether managers truly add value or just take more risk!")

def show_return_measures():
    st.markdown('<div class="section-header">📊 Return Measures</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Different Ways to Measure Returns
    
    Not all return calculations are created equal!
    """)
    
    tab1, tab2, tab3 = st.tabs(["Arithmetic vs Geometric", "Time-Weighted Return", "Dollar-Weighted Return"])
    
    with tab1:
        st.markdown("### 🔢 Arithmetic vs Geometric Average")
        
        st.markdown("""
        <div class="formula-box">
        <strong>Arithmetic Average:</strong><br>
        rₐ = (r₁ + r₂ + ... + rₙ) / n<br><br>
        <strong>Geometric Average:</strong><br>
        rg = [(1 + r₁) × (1 + r₂) × ... × (1 + rₙ)]^(1/n) - 1
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Interactive Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Annual Returns (%)**")
            r1 = st.number_input("Year 1", value=20.0, step=1.0, key="ar_r1") / 100
            r2 = st.number_input("Year 2", value=-10.0, step=1.0, key="ar_r2") / 100
            r3 = st.number_input("Year 3", value=15.0, step=1.0, key="ar_r3") / 100
            r4 = st.number_input("Year 4", value=5.0, step=1.0, key="ar_r4") / 100
        
        with col2:
            returns = [r1, r2, r3, r4]
            
            # Arithmetic
            arithmetic_avg = np.mean(returns)
            
            # Geometric
            cumulative = 1
            for r in returns:
                cumulative *= (1 + r)
            geometric_avg = cumulative ** (1/len(returns)) - 1
            
            # Terminal wealth
            initial_investment = 100
            final_wealth = initial_investment * cumulative
            
            st.markdown(f"""
            <div class="metric-good">
            <h3>Arithmetic Average</h3>
            <h2>{arithmetic_avg*100:.2f}%</h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-excellent">
            <h3>Geometric Average</h3>
            <h2>{geometric_avg*100:.2f}%</h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="concept-box">
            <h4>Terminal Wealth</h4>
            <p>Initial: ${initial_investment:.2f}</p>
            <p>Final: ${final_wealth:.2f}</p>
            <p>Total Return: {(final_wealth/initial_investment - 1)*100:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="concept-box">
        <h4>Key Differences</h4>
        <p><strong>Arithmetic:</strong> Simple average of returns. Always ≥ geometric.</p>
        <p><strong>Geometric:</strong> Compound annual growth rate (CAGR). Better for multi-period analysis.</p>
        <p><strong>When they differ:</strong> High volatility makes geometric < arithmetic.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Visualization
        years = list(range(len(returns) + 1))
        wealth = [initial_investment]
        for r in returns:
            wealth.append(wealth[-1] * (1 + r))
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years, y=wealth,
            mode='lines+markers',
            name='Wealth',
            line=dict(color='#028090', width=3),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title="Wealth Growth Over Time",
            xaxis_title="Year",
            yaxis_title="Portfolio Value ($)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("### ⏱️ Time-Weighted Return")
        
        st.markdown("""
        <div class="concept-box">
        <h4>What is it?</h4>
        <p><strong>Time-weighted return</strong> measures portfolio manager's performance independent of cash flows.</p>
        <p>Eliminates the effect of investor contributions/withdrawals.</p>
        <p><strong>Best for:</strong> Evaluating manager skill</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="formula-box">
        <strong>Time-Weighted Return:</strong><br>
        Return over each period, geometrically linked<br>
        TWR = [(1 + r₁) × (1 + r₂) × ... × (1 + rₙ)]^(1/n) - 1
        </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 **Use TWR to compare fund managers** - it removes the effect of investor cash flow timing!")
    
    with tab3:
        st.markdown("### 💰 Dollar-Weighted Return (IRR)")
        
        st.markdown("""
        <div class="concept-box">
        <h4>What is it?</h4>
        <p><strong>Dollar-weighted return</strong> is the internal rate of return (IRR) of all cash flows.</p>
        <p>Accounts for the timing and amount of contributions/withdrawals.</p>
        <p><strong>Best for:</strong> Measuring investor's actual experience</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="formula-box">
        <strong>Dollar-Weighted Return (IRR):</strong><br>
        0 = CF₀ + CF₁/(1+r) + CF₂/(1+r)² + ... + CFₙ/(1+r)ⁿ<br>
        Solve for r = IRR
        </div>
        """, unsafe_allow_html=True)
        
        st.warning("⚠️ **IRR can mislead** when evaluating managers - it's affected by when investors add/withdraw money!")

def show_risk_adjusted():
    st.markdown('<div class="section-header">📈 Risk-Adjusted Performance</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Why Risk-Adjustment Matters
    
    Higher returns don't necessarily mean better performance if achieved through higher risk.
    """)
    
    st.markdown("""
    <div class="concept-box">
    <h4>The Challenge</h4>
    <p>Portfolio A: 15% return, 20% volatility</p>
    <p>Portfolio B: 12% return, 10% volatility</p>
    <p><strong>Which is better?</strong> Need risk-adjusted metrics!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Comparison tool
    st.markdown("### 📊 Portfolio Comparison Tool")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Portfolio A")
        return_a = st.number_input("Return (%)", value=15.0, step=1.0, key="comp_ra") / 100
        std_a = st.number_input("Std Dev (%)", value=20.0, step=1.0, key="comp_sa") / 100
        beta_a = st.number_input("Beta", value=1.2, step=0.1, key="comp_ba")
    
    with col2:
        st.markdown("#### Portfolio B")
        return_b = st.number_input("Return (%)", value=12.0, step=1.0, key="comp_rb") / 100
        std_b = st.number_input("Std Dev (%)", value=10.0, step=1.0, key="comp_sb") / 100
        beta_b = st.number_input("Beta", value=0.8, step=0.1, key="comp_bb")
    
    with col3:
        st.markdown("#### Market/Benchmark")
        rf = st.number_input("Risk-Free Rate (%)", value=3.0, step=0.5, key="comp_rf") / 100
        market_return = st.number_input("Market Return (%)", value=10.0, step=1.0, key="comp_mr") / 100
        market_std = st.number_input("Market Std Dev (%)", value=18.0, step=1.0, key="comp_ms") / 100
    
    # Calculate metrics
    sharpe_a = (return_a - rf) / std_a if std_a > 0 else 0
    sharpe_b = (return_b - rf) / std_b if std_b > 0 else 0
    sharpe_m = (market_return - rf) / market_std if market_std > 0 else 0
    
    treynor_a = (return_a - rf) / beta_a if beta_a != 0 else 0
    treynor_b = (return_b - rf) / beta_b if beta_b != 0 else 0
    treynor_m = (market_return - rf) / 1.0  # Market beta = 1
    
    alpha_a = return_a - (rf + beta_a * (market_return - rf))
    alpha_b = return_b - (rf + beta_b * (market_return - rf))
    
    # Display comparison
    st.markdown("---")
    st.markdown("### 📊 Performance Comparison")
    
    comparison_df = pd.DataFrame({
        'Metric': ['Return', 'Std Dev', 'Beta', 'Sharpe Ratio', 'Treynor Ratio', 'Jensen\'s Alpha'],
        'Portfolio A': [f'{return_a*100:.2f}%', f'{std_a*100:.2f}%', f'{beta_a:.2f}',
                       f'{sharpe_a:.4f}', f'{treynor_a:.4f}', f'{alpha_a*100:.2f}%'],
        'Portfolio B': [f'{return_b*100:.2f}%', f'{std_b*100:.2f}%', f'{beta_b:.2f}',
                       f'{sharpe_b:.4f}', f'{treynor_b:.4f}', f'{alpha_b*100:.2f}%'],
        'Market': [f'{market_return*100:.2f}%', f'{market_std*100:.2f}%', '1.00',
                  f'{sharpe_m:.4f}', f'{treynor_m:.4f}', '0.00%']
    })
    
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)
    
    # Winner analysis
    col1, col2, col3 = st.columns(3)
    
    with col1:
        winner_sharpe = 'A' if sharpe_a > sharpe_b else 'B' if sharpe_b > sharpe_a else 'Tie'
        st.markdown(f"""
        <div class="{'metric-excellent' if winner_sharpe == 'A' else 'metric-good' if winner_sharpe == 'B' else 'concept-box'}">
        <h4>Best Sharpe Ratio</h4>
        <h2>Portfolio {winner_sharpe}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        winner_treynor = 'A' if treynor_a > treynor_b else 'B' if treynor_b > treynor_a else 'Tie'
        st.markdown(f"""
        <div class="{'metric-excellent' if winner_treynor == 'A' else 'metric-good' if winner_treynor == 'B' else 'concept-box'}">
        <h4>Best Treynor Ratio</h4>
        <h2>Portfolio {winner_treynor}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        winner_alpha = 'A' if alpha_a > alpha_b else 'B' if alpha_b > alpha_a else 'Tie'
        st.markdown(f"""
        <div class="{'metric-excellent' if winner_alpha == 'A' else 'metric-good' if winner_alpha == 'B' else 'concept-box'}">
        <h4>Best Alpha</h4>
        <h2>Portfolio {winner_alpha}</h2>
        </div>
        """, unsafe_allow_html=True)

def show_sharpe_treynor():
    st.markdown('<div class="section-header">🎯 Sharpe & Treynor Ratios</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📏 Sharpe Ratio")
        
        st.markdown("""
        <div class="formula-box">
        <strong>Sharpe Ratio = (Rₚ - Rբ) / σₚ</strong><br><br>
        Excess return per unit of total risk
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="concept-box">
        <h4>What it measures:</h4>
        <ul>
        <li><strong>Numerator:</strong> Excess return over risk-free rate</li>
        <li><strong>Denominator:</strong> Total risk (standard deviation)</li>
        <li><strong>Use for:</strong> Stand-alone portfolios</li>
        <li><strong>Higher is better</strong></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📐 Treynor Ratio")
        
        st.markdown("""
        <div class="formula-box">
        <strong>Treynor Ratio = (Rₚ - Rբ) / βₚ</strong><br><br>
        Excess return per unit of systematic risk
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="concept-box">
        <h4>What it measures:</h4>
        <ul>
        <li><strong>Numerator:</strong> Excess return over risk-free rate</li>
        <li><strong>Denominator:</strong> Systematic risk (beta)</li>
        <li><strong>Use for:</strong> Well-diversified portfolios</li>
        <li><strong>Higher is better</strong></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive Calculator
    st.markdown("### 🧮 Sharpe & Treynor Calculator")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        port_return = st.number_input("Portfolio Return (%)", value=15.0, step=1.0, key="st_return") / 100
        port_std = st.number_input("Portfolio Std Dev (%)", value=22.0, step=1.0, key="st_std") / 100
        port_beta = st.number_input("Portfolio Beta", value=1.3, step=0.1, key="st_beta")
        rf_rate = st.number_input("Risk-Free Rate (%)", value=3.0, step=0.5, key="st_rf") / 100
    
    with col2:
        sharpe = (port_return - rf_rate) / port_std if port_std > 0 else 0
        treynor = (port_return - rf_rate) / port_beta if port_beta != 0 else 0
        
        # Sharpe rating
        if sharpe > 2:
            sharpe_rating = "Excellent"
            sharpe_color = "metric-excellent"
        elif sharpe > 1:
            sharpe_rating = "Good"
            sharpe_color = "metric-good"
        elif sharpe > 0:
            sharpe_rating = "Acceptable"
            sharpe_color = "concept-box"
        else:
            sharpe_rating = "Poor"
            sharpe_color = "metric-poor"
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown(f"""
            <div class="{sharpe_color}">
            <h4>Sharpe Ratio</h4>
            <h2>{sharpe:.4f}</h2>
            <p>{sharpe_rating}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_b:
            st.markdown(f"""
            <div class="metric-good">
            <h4>Treynor Ratio</h4>
            <h2>{treynor:.4f}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="concept-box">
        <h4>Interpretation</h4>
        <p><strong>Sharpe Ratio:</strong> Earning {sharpe:.4f} excess return per unit of total risk</p>
        <p><strong>Treynor Ratio:</strong> Earning {treynor:.4f} excess return per unit of beta</p>
        <hr>
        <p><strong>Sharpe benchmarks:</strong></p>
        <p>< 0: Poor | 0-1: Acceptable | 1-2: Good | > 2: Excellent</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # M² Measure
    st.markdown("### 📊 M² (M-Squared) Measure")
    
    st.markdown("""
    <div class="concept-box">
    <h4>Modigliani-Modigliani (M²) Measure</h4>
    <p>Risk-adjusted return that matches portfolio volatility to benchmark.</p>
    <p><strong>Interpretation:</strong> How much would portfolio return if it had same risk as market?</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        market_std_m2 = st.number_input("Market Std Dev (%)", value=18.0, step=1.0, key="m2_mstd") / 100
        market_return_m2 = st.number_input("Market Return (%)", value=12.0, step=1.0, key="m2_mret") / 100
    
    with col2:
        # Calculate M²
        leverage_factor = market_std_m2 / port_std if port_std > 0 else 1
        adjusted_return = rf_rate + leverage_factor * (port_return - rf_rate)
        m_squared = adjusted_return - market_return_m2
        
        st.markdown(f"""
        <div class="metric-excellent">
        <h4>M² Measure</h4>
        <h2>{m_squared*100:.2f}%</h2>
        <p>Outperformance at market risk level</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="concept-box">
        <p><strong>Adjusted Return:</strong> {adjusted_return*100:.2f}%</p>
        <p><strong>Market Return:</strong> {market_return_m2*100:.2f}%</p>
        <p><strong>Leverage Factor:</strong> {leverage_factor:.2f}x</p>
        </div>
        """, unsafe_allow_html=True)

def show_alpha_ir():
    st.markdown('<div class="section-header">💎 Alpha & Information Ratio</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌟 Jensen's Alpha")
        
        st.markdown("""
        <div class="formula-box">
        <strong>α = Rₚ - [Rբ + β(Rₘ - Rբ)]</strong><br><br>
        Excess return above CAPM prediction
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="concept-box">
        <h4>What it measures:</h4>
        <ul>
        <li>Abnormal return after adjusting for systematic risk</li>
        <li>Value added by manager's skill</li>
        <li><strong>Positive alpha:</strong> Outperformance</li>
        <li><strong>Negative alpha:</strong> Underperformance</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📊 Information Ratio")
        
        st.markdown("""
        <div class="formula-box">
        <strong>IR = α / σ(eₚ)</strong><br><br>
        Alpha per unit of diversifiable risk
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="concept-box">
        <h4>What it measures:</h4>
        <ul>
        <li>Consistency of alpha generation</li>
        <li>Risk-adjusted active management skill</li>
        <li><strong>Higher is better</strong></li>
        <li>Typical good value: > 0.5</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive Calculator
    st.markdown("### 🧮 Alpha & Information Ratio Calculator")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("#### Portfolio Performance")
        portfolio_return_alpha = st.number_input("Portfolio Return (%)", value=14.0, step=1.0, key="alpha_pr") / 100
        portfolio_beta = st.number_input("Portfolio Beta", value=1.1, step=0.1, key="alpha_beta")
        tracking_error = st.number_input("Tracking Error (%)", value=4.0, step=0.5, key="alpha_te") / 100
        
        st.markdown("#### Market Data")
        rf_alpha = st.number_input("Risk-Free Rate (%)", value=3.0, step=0.5, key="alpha_rf") / 100
        market_return_alpha = st.number_input("Market Return (%)", value=11.0, step=1.0, key="alpha_mr") / 100
    
    with col2:
        # Calculate alpha
        expected_return = rf_alpha + portfolio_beta * (market_return_alpha - rf_alpha)
        alpha = portfolio_return_alpha - expected_return
        
        # Calculate information ratio
        information_ratio_val = alpha / tracking_error if tracking_error > 0 else 0
        
        # Alpha rating
        if alpha > 0.02:
            alpha_rating = "Excellent"
            alpha_color = "metric-excellent"
        elif alpha > 0:
            alpha_rating = "Positive"
            alpha_color = "metric-good"
        elif alpha > -0.02:
            alpha_rating = "Neutral"
            alpha_color = "concept-box"
        else:
            alpha_rating = "Poor"
            alpha_color = "metric-poor"
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown(f"""
            <div class="{alpha_color}">
            <h4>Jensen's Alpha</h4>
            <h2>{alpha*100:.2f}%</h2>
            <p>{alpha_rating}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_b:
            ir_color = "metric-excellent" if information_ratio_val > 0.5 else "metric-good" if information_ratio_val > 0 else "metric-poor"
            st.markdown(f"""
            <div class="{ir_color}">
            <h4>Information Ratio</h4>
            <h2>{information_ratio_val:.4f}</h2>
            <p>{'Excellent' if information_ratio_val > 0.5 else 'Good' if information_ratio_val > 0 else 'Poor'}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="concept-box">
        <h4>Analysis</h4>
        <p><strong>Actual Return:</strong> {portfolio_return_alpha*100:.2f}%</p>
        <p><strong>Expected Return (CAPM):</strong> {expected_return*100:.2f}%</p>
        <p><strong>Alpha:</strong> {alpha*100:.2f}% {'(Manager added value!)' if alpha > 0 else '(Underperformed!)'}</p>
        <hr>
        <p><strong>Tracking Error:</strong> {tracking_error*100:.2f}%</p>
        <p><strong>Information Ratio:</strong> {information_ratio_val:.4f}</p>
        <p>Earning {alpha*100:.2f}% alpha with {tracking_error*100:.2f}% tracking error</p>
        </div>
        """, unsafe_allow_html=True)

def show_attribution():
    st.markdown('<div class="section-header">🔍 Performance Attribution</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Decomposing Portfolio Returns
    
    **Performance attribution** breaks down returns to identify sources of value added or lost.
    """)
    
    st.markdown("""
    <div class="concept-box">
    <h4>Three Main Components</h4>
    <ol>
    <li><strong>Asset Allocation:</strong> Weighting different asset classes</li>
    <li><strong>Security Selection:</strong> Choosing specific securities within classes</li>
    <li><strong>Interaction:</strong> Combined effect of both decisions</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive Attribution Analysis
    st.markdown("### 📊 Attribution Analysis Tool")
    
    st.markdown("**Define Asset Classes and Returns:**")
    
    # Create 3 asset classes
    asset_classes = []
    for i in range(3):
        st.markdown(f"#### Asset Class {i+1}")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            name = st.text_input(f"Name", value=["Stocks", "Bonds", "Cash"][i], key=f"ac_name_{i}")
        
        with col2:
            bench_weight = st.number_input(f"Benchmark Weight (%)", value=[60.0, 30.0, 10.0][i], 
                                          step=1.0, key=f"ac_bw_{i}") / 100
        
        with col3:
            port_weight = st.number_input(f"Portfolio Weight (%)", value=[70.0, 20.0, 10.0][i], 
                                         step=1.0, key=f"ac_pw_{i}") / 100
        
        with col4:
            asset_return = st.number_input(f"Return (%)", value=[15.0, 8.0, 3.0][i], 
                                          step=0.5, key=f"ac_ret_{i}") / 100
        
        asset_classes.append({
            'name': name,
            'bench_weight': bench_weight,
            'port_weight': port_weight,
            'return': asset_return
        })
    
    # Calculate attribution
    st.markdown("---")
    st.markdown("### 📋 Attribution Results")
    
    attribution_results = []
    
    # Benchmark return
    benchmark_return = sum(ac['bench_weight'] * ac['return'] for ac in asset_classes)
    
    # Portfolio return
    portfolio_return = sum(ac['port_weight'] * ac['return'] for ac in asset_classes)
    
    # Total excess return
    total_excess = portfolio_return - benchmark_return
    
    # For each asset class
    allocation_effect_total = 0
    selection_effect_total = 0
    
    for ac in asset_classes:
        # Allocation effect: (Portfolio weight - Benchmark weight) × Benchmark return for that class
        # Simplified: use overall benchmark return
        allocation_effect = (ac['port_weight'] - ac['bench_weight']) * benchmark_return
        
        # Selection effect: Benchmark weight × (Asset return - Benchmark return)
        selection_effect = ac['bench_weight'] * (ac['return'] - benchmark_return)
        
        allocation_effect_total += allocation_effect
        selection_effect_total += selection_effect
        
        attribution_results.append({
            'Asset Class': ac['name'],
            'Benchmark Weight': f"{ac['bench_weight']*100:.1f}%",
            'Portfolio Weight': f"{ac['port_weight']*100:.1f}%",
            'Return': f"{ac['return']*100:.2f}%",
            'Allocation Effect': f"{allocation_effect*100:.2f}%",
            'Selection Effect': f"{selection_effect*100:.2f}%"
        })
    
    attribution_df = pd.DataFrame(attribution_results)
    st.dataframe(attribution_df, use_container_width=True, hide_index=True)
    
    # Summary
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-good">
        <h4>Benchmark Return</h4>
        <h2>{benchmark_return*100:.2f}%</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-excellent">
        <h4>Portfolio Return</h4>
        <h2>{portfolio_return*100:.2f}%</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        excess_color = "metric-excellent" if total_excess > 0 else "metric-poor"
        st.markdown(f"""
        <div class="{excess_color}">
        <h4>Excess Return</h4>
        <h2>{total_excess*100:.2f}%</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(f"""
    <div class="concept-box">
    <h4>Attribution Summary</h4>
    <p><strong>Allocation Effect:</strong> {allocation_effect_total*100:.2f}% 
    {' (Good asset allocation!)' if allocation_effect_total > 0 else ' (Poor asset allocation)'}</p>
    <p><strong>Selection Effect:</strong> {selection_effect_total*100:.2f}% 
    {' (Good security selection!)' if selection_effect_total > 0 else ' (Poor security selection)'}</p>
    <hr>
    <p><strong>Total Attribution:</strong> {(allocation_effect_total + selection_effect_total)*100:.2f}%</p>
    </div>
    """, unsafe_allow_html=True)

def show_market_timing():
    st.markdown('<div class="section-header">⏱️ Market Timing</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Can Managers Time the Market?
    
    **Market timing** involves shifting between risky and risk-free assets based on market forecasts.
    """)
    
    st.markdown("""
    <div class="concept-box">
    <h4>Perfect Market Timing</h4>
    <p>With perfect foresight, market timing creates an <strong>option-like payoff</strong>:</p>
    <ul>
    <li>Invest in stocks when market rises</li>
    <li>Hold cash when market falls</li>
    <li>Results in convex return pattern</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Simulate market timing
    st.markdown("### 📊 Market Timing Simulation")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Timing Skill")
        success_rate = st.slider("Success Rate (%)", 0, 100, 60, 5, key="mt_success") / 100
        num_periods = st.slider("Number of Periods", 10, 100, 50, 10, key="mt_periods")
        
        st.markdown("#### Market Parameters")
        bull_return = st.number_input("Bull Market Return (%)", value=20.0, step=5.0, key="mt_bull") / 100
        bear_return = st.number_input("Bear Market Return (%)", value=-10.0, step=5.0, key="mt_bear") / 100
        rf_rate_mt = st.number_input("Risk-Free Rate (%)", value=3.0, step=0.5, key="mt_rf") / 100
    
    with col2:
        # Simulate market periods (50/50 bull/bear)
        np.random.seed(42)
        market_states = np.random.choice(['Bull', 'Bear'], size=num_periods, p=[0.5, 0.5])
        
        # Market returns
        market_returns = [bull_return if state == 'Bull' else bear_return for state in market_states]
        
        # Perfect timer returns
        perfect_returns = [max(ret, rf_rate_mt) for ret in market_returns]
        
        # Imperfect timer returns (based on success rate)
        timer_choices = np.random.random(num_periods)
        imperfect_returns = []
        for i, state in enumerate(market_states):
            if timer_choices[i] < success_rate:
                # Correct call
                if state == 'Bull':
                    imperfect_returns.append(market_returns[i])
                else:
                    imperfect_returns.append(rf_rate_mt)
            else:
                # Wrong call
                if state == 'Bull':
                    imperfect_returns.append(rf_rate_mt)
                else:
                    imperfect_returns.append(market_returns[i])
        
        # Calculate cumulative returns
        market_cum = np.cumprod([1 + r for r in market_returns])
        perfect_cum = np.cumprod([1 + r for r in perfect_returns])
        imperfect_cum = np.cumprod([1 + r for r in imperfect_returns])
        
        # Plot
        periods = list(range(num_periods + 1))
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=periods, y=[1] + list(market_cum),
            mode='lines',
            name='Buy & Hold',
            line=dict(color='gray', width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=periods, y=[1] + list(perfect_cum),
            mode='lines',
            name='Perfect Timer',
            line=dict(color='#97BC62', width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=periods, y=[1] + list(imperfect_cum),
            mode='lines',
            name=f'Timer ({success_rate*100:.0f}% accuracy)',
            line=dict(color='#028090', width=2)
        ))
        
        fig.update_layout(
            title="Market Timing Performance",
            xaxis_title="Period",
            yaxis_title="Cumulative Wealth",
            height=500,
            hovermode='x'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Final results
    market_final = market_cum[-1]
    perfect_final = perfect_cum[-1]
    imperfect_final = imperfect_cum[-1]
    
    market_ann = (market_final ** (1/num_periods) - 1) * 100
    perfect_ann = (perfect_final ** (1/num_periods) - 1) * 100
    imperfect_ann = (imperfect_final ** (1/num_periods) - 1) * 100
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Buy & Hold", f"{market_ann:.2f}%", delta=f"${market_final:.2f}")
    col2.metric("Perfect Timer", f"{perfect_ann:.2f}%", delta=f"${perfect_final:.2f}")
    col3.metric(f"Timer ({success_rate*100:.0f}%)", f"{imperfect_ann:.2f}%", delta=f"${imperfect_final:.2f}")
    
    st.warning("⚠️ **Reality Check:** Few managers consistently demonstrate market timing skill. Success rate must be > 50% to add value!")

def show_quiz():
    st.markdown('<div class="section-header">✅ Test Your Knowledge</div>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'ch18_score' not in st.session_state:
        st.session_state.ch18_score = 0
    if 'ch18_submitted' not in st.session_state:
        st.session_state.ch18_submitted = set()
    
    # Question 1
    st.markdown("### Question 1: Sharpe Ratio")
    st.markdown("The Sharpe ratio measures:")
    
    q1 = st.radio("",
                 ["A) Total return", "B) Excess return per unit of total risk",
                  "C) Excess return per unit of systematic risk", "D) Alpha"],
                 key="q1", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q1_btn") and "q1" not in st.session_state.ch18_submitted:
        st.session_state.ch18_submitted.add("q1")
        if q1 == "B) Excess return per unit of total risk":
            st.success("✅ Correct! Sharpe = (Rₚ - Rբ) / σₚ")
            st.session_state.ch18_score += 1
        else:
            st.error("❌ Incorrect. Sharpe ratio uses total risk (std dev) in denominator.")
    
    st.markdown("---")
    
    # Question 2
    st.markdown("### Question 2: Treynor vs Sharpe")
    st.markdown("Treynor ratio is more appropriate than Sharpe ratio when:")
    
    q2 = st.radio("",
                 ["A) Portfolio is poorly diversified", "B) Portfolio is well-diversified",
                  "C) Returns are negative", "D) Both are always equally appropriate"],
                 key="q2", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q2_btn") and "q2" not in st.session_state.ch18_submitted:
        st.session_state.ch18_submitted.add("q2")
        if q2 == "B) Portfolio is well-diversified":
            st.success("✅ Correct! Treynor uses beta (systematic risk), appropriate when diversified.")
            st.session_state.ch18_score += 1
        else:
            st.error("❌ Incorrect. Treynor is for well-diversified portfolios (beta matters).")
    
    st.markdown("---")
    
    # Question 3
    st.markdown("### Question 3: Jensen's Alpha")
    st.markdown("A positive Jensen's alpha indicates:")
    
    q3 = st.radio("",
                 ["A) High beta", "B) Low volatility",
                  "C) Outperformance relative to CAPM", "D) Perfect market timing"],
                 key="q3", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q3_btn") and "q3" not in st.session_state.ch18_submitted:
        st.session_state.ch18_submitted.add("q3")
        if q3 == "C) Outperformance relative to CAPM":
            st.success("✅ Correct! Positive alpha means beating CAPM prediction.")
            st.session_state.ch18_score += 1
        else:
            st.error("❌ Incorrect. Alpha measures excess return above CAPM.")
    
    st.markdown("---")
    
    # Question 4
    st.markdown("### Question 4: Return Measures")
    st.markdown("Geometric average return is always:")
    
    q4 = st.radio("",
                 ["A) Greater than arithmetic average", "B) Less than or equal to arithmetic average",
                  "C) Equal to arithmetic average", "D) Unrelated to arithmetic average"],
                 key="q4", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q4_btn") and "q4" not in st.session_state.ch18_submitted:
        st.session_state.ch18_submitted.add("q4")
        if q4 == "B) Less than or equal to arithmetic average":
            st.success("✅ Correct! Geometric ≤ Arithmetic (equal only if no volatility)")
            st.session_state.ch18_score += 1
        else:
            st.error("❌ Incorrect. Geometric average ≤ Arithmetic average.")
    
    st.markdown("---")
    
    # Question 5
    st.markdown("### Question 5: Performance Attribution")
    st.markdown("Performance attribution decomposes returns into:")
    
    q5 = st.radio("",
                 ["A) Asset allocation and security selection", "B) Alpha and beta",
                  "C) Systematic and unsystematic risk", "D) Mean and variance"],
                 key="q5", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q5_btn") and "q5" not in st.session_state.ch18_submitted:
        st.session_state.ch18_submitted.add("q5")
        if q5 == "A) Asset allocation and security selection":
            st.success("✅ Correct! Attribution separates allocation and selection effects.")
            st.session_state.ch18_score += 1
        else:
            st.error("❌ Incorrect. Attribution breaks down asset allocation vs security selection.")
    
    st.markdown("---")
    
    # Score Display
    if len(st.session_state.ch18_submitted) > 0:
        score_pct = (st.session_state.ch18_score / len(st.session_state.ch18_submitted)) * 100
        
        st.markdown(f"""
        <div class="concept-box">
        <h2>Your Score: {st.session_state.ch18_score} / {len(st.session_state.ch18_submitted)}</h2>
        <h3>{score_pct:.0f}%</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if score_pct >= 80:
            st.success("🎉 Excellent! You understand portfolio performance evaluation well.")
        elif score_pct >= 60:
            st.info("👍 Good work! Review risk-adjusted metrics.")
        else:
            st.warning("📚 Keep studying! Review Sharpe, Treynor, and Alpha concepts.")
    
    if st.button("Reset Quiz", key="reset_quiz"):
        st.session_state.ch18_score = 0
        st.session_state.ch18_submitted = set()
        st.rerun()

if __name__ == "__main__":
    main()
