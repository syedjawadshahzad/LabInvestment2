import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(
    page_title="Financial Statement Analysis",
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
    .ratio-box {
        background-color: #CADCFC;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .metric-good {
        background-color: #97BC62;
        padding: 1rem;
        border-radius: 8px;
        color: white;
        text-align: center;
    }
    .metric-warning {
        background-color: #F9E795;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    .metric-bad {
        background-color: #F96167;
        padding: 1rem;
        border-radius: 8px;
        color: white;
        text-align: center;
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
         "📄 Financial Statements",
         "💰 Profitability Ratios",
         "🔍 DuPont Analysis",
         "💧 Liquidity Ratios",
         "⚖️ Leverage Ratios",
         "📊 Complete Analysis",
         "✅ Quiz"]
    )
    
    if page == "🏠 Home":
        show_home()
    elif page == "📄 Financial Statements":
        show_financial_statements()
    elif page == "💰 Profitability Ratios":
        show_profitability()
    elif page == "🔍 DuPont Analysis":
        show_dupont()
    elif page == "💧 Liquidity Ratios":
        show_liquidity()
    elif page == "⚖️ Leverage Ratios":
        show_leverage()
    elif page == "📊 Complete Analysis":
        show_complete_analysis()
    elif page == "✅ Quiz":
        show_quiz()

def show_home():
    st.markdown('<div class="main-header">📊 Financial Statement Analysis</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Ratio Analysis & Performance Measurement</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">📄 Three Statements</h3>
        <p>Foundation of analysis</p>
        <ul>
        <li>Income Statement (P&L)</li>
        <li>Balance Sheet</li>
        <li>Cash Flow Statement</li>
        <li>Statement linkages</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">📊 Financial Ratios</h3>
        <p>Measure performance</p>
        <ul>
        <li>Profitability (ROE, ROA, Margin)</li>
        <li>Liquidity (Current, Quick)</li>
        <li>Leverage (Debt/Equity)</li>
        <li>Efficiency (Turnover)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">🔍 DuPont Analysis</h3>
        <p>Decompose performance</p>
        <ul>
        <li>ROE breakdown (5 factors)</li>
        <li>Identify drivers</li>
        <li>Industry comparison</li>
        <li>Trend analysis</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown('<div class="section-header">📋 Chapter Overview</div>', unsafe_allow_html=True)
    
    st.markdown("""
    This interactive app covers **Financial Statement Analysis**.
    
    ### Analysis Framework:
    
    1. **Financial Statements** → Understanding the three core statements
    2. **Profitability Ratios** → ROE, ROA, margins, EVA
    3. **DuPont Analysis** → Five-way decomposition of ROE
    4. **Liquidity Ratios** → Short-term financial health
    5. **Leverage Ratios** → Capital structure and solvency
    
    ### 🎯 Learning Objectives:
    
    By the end of this module, you will be able to:
    - Interpret the three main financial statements
    - Calculate and analyze key financial ratios
    - Perform DuPont analysis to decompose ROE
    - Assess liquidity and leverage positions
    - Compare companies using ratio analysis
    - Identify quality of earnings issues
    """)
    
    st.info("💡 **Key Insight:** Financial ratios are meaningless in isolation. Always compare to: (1) Historical trends, (2) Industry peers, (3) Benchmarks.")

def show_financial_statements():
    st.markdown('<div class="section-header">📄 The Three Financial Statements</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Core Financial Statements
    
    Every public company must file three key financial statements:
    """)
    
    tab1, tab2, tab3 = st.tabs(["Income Statement", "Balance Sheet", "Cash Flow Statement"])
    
    with tab1:
        st.markdown("### 💵 Income Statement (P&L)")
        
        st.markdown("""
        <div class="concept-box">
        <h4>Purpose</h4>
        <p>Shows firm's <strong>revenues and expenses</strong> during a period (quarter or year)</p>
        <p><strong>Bottom line:</strong> Net Income (profit or loss)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Typical Structure")
        
        st.markdown("""
        <div class="ratio-box">
        <strong>Revenue (Sales)</strong><br>
        − Cost of Goods Sold (COGS)<br>
        = <strong>Gross Profit</strong><br>
        − Operating Expenses (SG&A)<br>
        − Depreciation & Amortization<br>
        = <strong>EBIT (Operating Income)</strong><br>
        − Interest Expense<br>
        = <strong>EBT (Pre-tax Income)</strong><br>
        − Taxes<br>
        = <strong>Net Income</strong>
        </div>
        """, unsafe_allow_html=True)
        
        # Sample Income Statement
        st.markdown("#### Interactive Income Statement")
        
        col1, col2 = st.columns(2)
        
        with col1:
            revenue = st.number_input("Revenue ($M)", value=10000.0, step=100.0, key="is_rev")
            cogs = st.number_input("COGS ($M)", value=6000.0, step=100.0, key="is_cogs")
            opex = st.number_input("Operating Expenses ($M)", value=2000.0, step=100.0, key="is_opex")
            depreciation = st.number_input("Depreciation ($M)", value=500.0, step=50.0, key="is_dep")
            interest = st.number_input("Interest Expense ($M)", value=200.0, step=10.0, key="is_int")
            tax_rate = st.slider("Tax Rate (%)", 0.0, 50.0, 25.0, 1.0, key="is_tax") / 100
        
        with col2:
            gross_profit = revenue - cogs
            ebit = gross_profit - opex - depreciation
            ebt = ebit - interest
            tax = ebt * tax_rate
            net_income = ebt - tax
            
            gross_margin = (gross_profit / revenue) * 100 if revenue > 0 else 0
            operating_margin = (ebit / revenue) * 100 if revenue > 0 else 0
            net_margin = (net_income / revenue) * 100 if revenue > 0 else 0
            
            st.markdown(f"""
            <div class="concept-box">
            <h4>Income Statement Summary</h4>
            <p><strong>Revenue:</strong> ${revenue:.0f}M</p>
            <p><strong>Gross Profit:</strong> ${gross_profit:.0f}M ({gross_margin:.1f}%)</p>
            <p><strong>EBIT:</strong> ${ebit:.0f}M ({operating_margin:.1f}%)</p>
            <p><strong>EBT:</strong> ${ebt:.0f}M</p>
            <p><strong>Tax:</strong> ${tax:.0f}M</p>
            <hr>
            <h3><strong>Net Income:</strong> ${net_income:.0f}M ({net_margin:.1f}%)</h3>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 🏦 Balance Sheet")
        
        st.markdown("""
        <div class="concept-box">
        <h4>Purpose</h4>
        <p>Shows firm's <strong>financial position at a point in time</strong></p>
        <p><strong>Fundamental equation:</strong> Assets = Liabilities + Equity</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="ratio-box">
            <h4>ASSETS (What the firm owns)</h4>
            <p><strong>Current Assets:</strong></p>
            <ul>
            <li>Cash & Equivalents</li>
            <li>Accounts Receivable</li>
            <li>Inventory</li>
            </ul>
            <p><strong>Non-Current Assets:</strong></p>
            <ul>
            <li>Property, Plant & Equipment</li>
            <li>Intangible Assets</li>
            <li>Long-term Investments</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="ratio-box">
            <h4>LIABILITIES + EQUITY</h4>
            <p><strong>Current Liabilities:</strong></p>
            <ul>
            <li>Accounts Payable</li>
            <li>Short-term Debt</li>
            <li>Accrued Expenses</li>
            </ul>
            <p><strong>Long-term Liabilities:</strong></p>
            <ul>
            <li>Long-term Debt</li>
            <li>Deferred Tax</li>
            </ul>
            <p><strong>Shareholders' Equity:</strong></p>
            <ul>
            <li>Common Stock</li>
            <li>Retained Earnings</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Simple balance sheet check
        st.markdown("#### Balance Sheet Checker")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_assets = st.number_input("Total Assets ($M)", value=5000.0, step=100.0, key="bs_assets")
        
        with col2:
            total_liab = st.number_input("Total Liabilities ($M)", value=3000.0, step=100.0, key="bs_liab")
        
        with col3:
            total_equity = st.number_input("Total Equity ($M)", value=2000.0, step=100.0, key="bs_equity")
        
        difference = total_assets - (total_liab + total_equity)
        
        if abs(difference) < 0.01:
            st.success(f"✅ **Balanced!** Assets = Liabilities + Equity")
        else:
            st.error(f"❌ **Not Balanced!** Difference: ${difference:.2f}M")
    
    with tab3:
        st.markdown("### 💸 Cash Flow Statement")
        
        st.markdown("""
        <div class="concept-box">
        <h4>Purpose</h4>
        <p>Shows firm's <strong>cash receipts and payments</strong> during a period</p>
        <p><strong>Key insight:</strong> Cash ≠ Earnings (due to accrual accounting)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Three Categories of Cash Flow")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="ratio-box">
            <h4>Operating Activities</h4>
            <p>Cash from core business</p>
            <ul>
            <li>+ Collections from customers</li>
            <li>− Payments to suppliers</li>
            <li>− Operating expenses</li>
            <li>− Taxes</li>
            </ul>
            <p><strong>Should be positive!</strong></p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="ratio-box">
            <h4>Investing Activities</h4>
            <p>Long-term investments</p>
            <ul>
            <li>− CapEx (PP&E)</li>
            <li>− Acquisitions</li>
            <li>+ Asset sales</li>
            </ul>
            <p><strong>Usually negative</strong></p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="ratio-box">
            <h4>Financing Activities</h4>
            <p>Capital structure changes</p>
            <ul>
            <li>+ Debt issued</li>
            <li>− Debt repaid</li>
            <li>+ Equity issued</li>
            <li>− Dividends paid</li>
            </ul>
            <p><strong>Can be + or −</strong></p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("#### Cash Flow Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            cf_ops = st.number_input("Operating Cash Flow ($M)", value=1500.0, step=50.0, key="cf_ops")
            cf_inv = st.number_input("Investing Cash Flow ($M)", value=-800.0, step=50.0, key="cf_inv")
            cf_fin = st.number_input("Financing Cash Flow ($M)", value=-500.0, step=50.0, key="cf_fin")
        
        with col2:
            net_cf = cf_ops + cf_inv + cf_fin
            
            st.markdown(f"""
            <div class="concept-box">
            <h4>Net Change in Cash</h4>
            <p>Operating CF: ${cf_ops:.0f}M</p>
            <p>Investing CF: ${cf_inv:.0f}M</p>
            <p>Financing CF: ${cf_fin:.0f}M</p>
            <hr>
            <h3>Net Change: ${net_cf:.0f}M</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Free Cash Flow
            fcf = cf_ops + cf_inv  # Simplified
            st.markdown(f"""
            <div class="concept-box">
            <h4>Free Cash Flow</h4>
            <p>FCF = Operating CF + Investing CF</p>
            <h3>${fcf:.0f}M</h3>
            <p><em>Cash available to investors</em></p>
            </div>
            """, unsafe_allow_html=True)

def show_profitability():
    st.markdown('<div class="section-header">💰 Profitability Ratios</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Key Profitability Measures
    
    These ratios measure how effectively a company generates profits.
    """)
    
    # ROE Focus
    st.markdown("### 🎯 Return on Equity (ROE)")
    
    st.markdown("""
    <div class="concept-box">
    <h4>The Most Important Profitability Ratio</h4>
    <p><strong>ROE = Net Income / Shareholders' Equity</strong></p>
    <p>Measures return earned on shareholders' investment</p>
    <p><strong>Higher is better</strong> (typical range: 10-20%)</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("#### Input Data")
        net_income_roe = st.number_input("Net Income ($M)", value=400.0, step=10.0, key="prof_ni")
        equity_roe = st.number_input("Shareholders' Equity ($M)", value=2000.0, step=100.0, key="prof_eq")
        
        total_assets_roe = st.number_input("Total Assets ($M)", value=5000.0, step=100.0, key="prof_assets")
        sales_roe = st.number_input("Sales ($M)", value=10000.0, step=100.0, key="prof_sales")
    
    with col2:
        roe = (net_income_roe / equity_roe) * 100 if equity_roe > 0 else 0
        roa = (net_income_roe / total_assets_roe) * 100 if total_assets_roe > 0 else 0
        margin = (net_income_roe / sales_roe) * 100 if sales_roe > 0 else 0
        turnover = sales_roe / total_assets_roe if total_assets_roe > 0 else 0
        leverage_mult = total_assets_roe / equity_roe if equity_roe > 0 else 0
        
        # ROE Rating
        if roe >= 20:
            roe_rating = "Excellent"
            roe_color = "#97BC62"
        elif roe >= 15:
            roe_rating = "Good"
            roe_color = "#028090"
        elif roe >= 10:
            roe_rating = "Average"
            roe_color = "#F9E795"
        else:
            roe_rating = "Below Average"
            roe_color = "#F96167"
        
        st.markdown(f"""
        <div class="metric-good" style="background-color: {roe_color};">
        <h2>ROE: {roe:.2f}%</h2>
        <p><strong>Rating: {roe_rating}</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="concept-box">
        <h4>Related Metrics</h4>
        <p><strong>ROA:</strong> {roa:.2f}%</p>
        <p><strong>Profit Margin:</strong> {margin:.2f}%</p>
        <p><strong>Asset Turnover:</strong> {turnover:.2f}x</p>
        <p><strong>Leverage Multiplier:</strong> {leverage_mult:.2f}x</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Economic Value Added
    st.markdown("### 💎 Economic Value Added (EVA)")
    
    st.markdown("""
    <div class="concept-box">
    <h4>EVA (Residual Income)</h4>
    <p>Dollar value of return in excess of opportunity cost</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="ratio-box">
    <strong>EVA = (ROA − Cost of Capital) × Total Assets</strong><br><br>
    Or: EVA = EBIT × (1 − Tax Rate) − (WACC × Total Assets)
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        ebit_eva = st.number_input("EBIT ($M)", value=800.0, step=50.0, key="eva_ebit")
        tax_rate_eva = st.slider("Tax Rate (%)", 0.0, 50.0, 25.0, 1.0, key="eva_tax") / 100
        wacc_eva = st.slider("WACC (%)", 5.0, 15.0, 10.0, 0.5, key="eva_wacc") / 100
        assets_eva = st.number_input("Total Assets ($M)", value=5000.0, step=100.0, key="eva_assets")
    
    with col2:
        nopat = ebit_eva * (1 - tax_rate_eva)
        capital_charge = wacc_eva * assets_eva
        eva = nopat - capital_charge
        
        eva_color = "#97BC62" if eva > 0 else "#F96167"
        
        st.markdown(f"""
        <div class="metric-good" style="background-color: {eva_color};">
        <h3>Economic Value Added</h3>
        <h2>${eva:.0f}M</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="concept-box">
        <h4>EVA Breakdown</h4>
        <p><strong>NOPAT:</strong> ${nopat:.0f}M</p>
        <p><strong>Capital Charge:</strong> ${capital_charge:.0f}M</p>
        <p><strong>EVA:</strong> ${eva:.0f}M</p>
        <hr>
        <p>{'✅ Creating value!' if eva > 0 else '❌ Destroying value!'}</p>
        </div>
        """, unsafe_allow_html=True)

def show_dupont():
    st.markdown('<div class="section-header">🔍 DuPont Analysis</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### DuPont ROE Decomposition
    
    Break down **ROE** into its five component drivers to understand what's driving performance.
    """)
    
    st.markdown("""
    <div class="ratio-box">
    <strong>ROE = Tax Burden × Interest Burden × Profit Margin × Asset Turnover × Leverage</strong><br><br>
    ROE = (Net Income / EBT) × (EBT / EBIT) × (EBIT / Sales) × (Sales / Assets) × (Assets / Equity)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🧮 DuPont Calculator")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("#### Financial Data")
        sales_dp = st.number_input("Sales ($M)", value=10000.0, step=100.0, key="dp_sales")
        ebit_dp = st.number_input("EBIT ($M)", value=1500.0, step=50.0, key="dp_ebit")
        interest_dp = st.number_input("Interest Expense ($M)", value=200.0, step=10.0, key="dp_int")
        ebt_dp = ebit_dp - interest_dp
        tax_dp = st.number_input("Tax ($M)", value=325.0, step=10.0, key="dp_tax")
        net_income_dp = ebt_dp - tax_dp
        
        assets_dp = st.number_input("Total Assets ($M)", value=5000.0, step=100.0, key="dp_assets")
        equity_dp = st.number_input("Shareholders' Equity ($M)", value=2000.0, step=100.0, key="dp_equity")
    
    with col2:
        # Calculate five factors
        tax_burden = net_income_dp / ebt_dp if ebt_dp > 0 else 0
        interest_burden = ebt_dp / ebit_dp if ebit_dp > 0 else 0
        profit_margin = ebit_dp / sales_dp if sales_dp > 0 else 0
        asset_turnover = sales_dp / assets_dp if assets_dp > 0 else 0
        leverage = assets_dp / equity_dp if equity_dp > 0 else 0
        
        # Calculate ROE
        roe_dp = tax_burden * interest_burden * profit_margin * asset_turnover * leverage
        
        # Also calculate directly
        roe_direct = net_income_dp / equity_dp if equity_dp > 0 else 0
        
        st.markdown(f"""
        <div class="metric-good">
        <h2>ROE: {roe_dp*100:.2f}%</h2>
        <p>(Direct calculation: {roe_direct*100:.2f}%)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="concept-box">
        <h4>Five Components</h4>
        <p><strong>1. Tax Burden:</strong> {tax_burden:.4f} ({(1-tax_burden)*100:.1f}% tax rate)</p>
        <p><strong>2. Interest Burden:</strong> {interest_burden:.4f}</p>
        <p><strong>3. Profit Margin:</strong> {profit_margin*100:.2f}%</p>
        <p><strong>4. Asset Turnover:</strong> {asset_turnover:.2f}x</p>
        <p><strong>5. Leverage:</strong> {leverage:.2f}x</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Visual breakdown
    st.markdown("### 📊 DuPont Waterfall Chart")
    
    # Create waterfall
    components = ['Tax<br>Burden', 'Interest<br>Burden', 'Margin', 'Turnover', 'Leverage', 'ROE']
    values = [tax_burden, interest_burden, profit_margin, asset_turnover, leverage, roe_dp]
    
    # For waterfall, show cumulative product
    cumulative = [1]
    for v in values[:-1]:
        cumulative.append(cumulative[-1] * v)
    
    fig = go.Figure()
    
    # Bars for each component
    colors = ['#028090', '#97BC62', '#F9E795', '#CADCFC', '#F96167', '#1E2761']
    
    for i, (comp, val) in enumerate(zip(components[:-1], values[:-1])):
        fig.add_trace(go.Bar(
            x=[comp],
            y=[val],
            name=comp,
            marker_color=colors[i],
            text=[f'{val:.3f}'],
            textposition='auto'
        ))
    
    # Final ROE bar
    fig.add_trace(go.Bar(
        x=[components[-1]],
        y=[roe_dp],
        name='ROE',
        marker_color=colors[-1],
        text=[f'{roe_dp*100:.2f}%'],
        textposition='auto'
    ))
    
    fig.update_layout(
        title="DuPont ROE Components",
        yaxis_title="Value",
        height=500,
        showlegend=False,
        xaxis={'categoryorder':'total ascending'}
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # ROA vs ROE
    st.markdown("### ⚖️ ROA vs ROE: The Impact of Leverage")
    
    roa_dp = net_income_dp / assets_dp if assets_dp > 0 else 0
    
    st.markdown(f"""
    <div class="concept-box">
    <h4>Key Relationship</h4>
    <p><strong>ROA = Margin × Turnover</strong> = {profit_margin*100:.2f}% × {asset_turnover:.2f} = {roa_dp*100:.2f}%</p>
    <p><strong>ROE = ROA × Leverage</strong> = {roa_dp*100:.2f}% × {leverage:.2f} = {roe_dp*100:.2f}%</p>
    <hr>
    <p><strong>Leverage multiplies ROA to get ROE!</strong></p>
    <p>If ROA > Cost of Debt, leverage increases ROE (good)</p>
    <p>If ROA < Cost of Debt, leverage decreases ROE (bad)</p>
    </div>
    """, unsafe_allow_html=True)

def show_liquidity():
    st.markdown('<div class="section-header">💧 Liquidity Ratios</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Measuring Short-Term Financial Health
    
    **Liquidity** is the ability to convert assets into cash quickly to meet short-term obligations.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Balance Sheet Data")
        cash = st.number_input("Cash & Equivalents ($M)", value=500.0, step=50.0, key="liq_cash")
        receivables = st.number_input("Accounts Receivable ($M)", value=800.0, step=50.0, key="liq_ar")
        inventory = st.number_input("Inventory ($M)", value=1200.0, step=50.0, key="liq_inv")
        current_liab = st.number_input("Current Liabilities ($M)", value=1500.0, step=50.0, key="liq_cl")
        
        current_assets = cash + receivables + inventory
    
    with col2:
        # Calculate ratios
        current_ratio = current_assets / current_liab if current_liab > 0 else 0
        quick_ratio = (cash + receivables) / current_liab if current_liab > 0 else 0
        cash_ratio = cash / current_liab if current_liab > 0 else 0
        
        st.markdown(f"""
        <div class="concept-box">
        <h4>Current Assets Breakdown</h4>
        <p>Cash: ${cash:.0f}M</p>
        <p>Receivables: ${receivables:.0f}M</p>
        <p>Inventory: ${inventory:.0f}M</p>
        <hr>
        <p><strong>Total Current Assets: ${current_assets:.0f}M</strong></p>
        <p><strong>Current Liabilities: ${current_liab:.0f}M</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Display ratios
    st.markdown("### 📊 Liquidity Ratios Summary")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Current Ratio")
        st.markdown("""
        <div class="ratio-box">
        <strong>Formula:</strong><br>
        Current Assets / Current Liabilities
        </div>
        """, unsafe_allow_html=True)
        
        if current_ratio >= 2.0:
            color = "#97BC62"
            rating = "Excellent"
        elif current_ratio >= 1.5:
            color = "#028090"
            rating = "Good"
        elif current_ratio >= 1.0:
            color = "#F9E795"
            rating = "Adequate"
        else:
            color = "#F96167"
            rating = "Poor"
        
        st.markdown(f"""
        <div class="metric-good" style="background-color: {color}; color: {'white' if color in ['#97BC62', '#F96167'] else 'black'};">
        <h2>{current_ratio:.2f}</h2>
        <p>{rating}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("**Benchmark:** > 1.5 is good")
    
    with col2:
        st.markdown("#### Quick Ratio (Acid Test)")
        st.markdown("""
        <div class="ratio-box">
        <strong>Formula:</strong><br>
        (Cash + Receivables) / Current Liabilities
        </div>
        """, unsafe_allow_html=True)
        
        if quick_ratio >= 1.5:
            color = "#97BC62"
            rating = "Excellent"
        elif quick_ratio >= 1.0:
            color = "#028090"
            rating = "Good"
        elif quick_ratio >= 0.75:
            color = "#F9E795"
            rating = "Adequate"
        else:
            color = "#F96167"
            rating = "Poor"
        
        st.markdown(f"""
        <div class="metric-good" style="background-color: {color}; color: {'white' if color in ['#97BC62', '#F96167'] else 'black'};">
        <h2>{quick_ratio:.2f}</h2>
        <p>{rating}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("**Benchmark:** > 1.0 is good")
    
    with col3:
        st.markdown("#### Cash Ratio")
        st.markdown("""
        <div class="ratio-box">
        <strong>Formula:</strong><br>
        Cash / Current Liabilities
        </div>
        """, unsafe_allow_html=True)
        
        if cash_ratio >= 0.5:
            color = "#97BC62"
            rating = "Excellent"
        elif cash_ratio >= 0.3:
            color = "#028090"
            rating = "Good"
        elif cash_ratio >= 0.2:
            color = "#F9E795"
            rating = "Adequate"
        else:
            color = "#F96167"
            rating = "Poor"
        
        st.markdown(f"""
        <div class="metric-good" style="background-color: {color}; color: {'white' if color in ['#97BC62', '#F96167'] else 'black'};">
        <h2>{cash_ratio:.2f}</h2>
        <p>{rating}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("**Benchmark:** > 0.2 is good")
    
    st.markdown("---")
    
    # Visualization
    st.markdown("### 📈 Liquidity Analysis")
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Current Assets',
        x=['Liquidity Position'],
        y=[current_assets],
        marker_color='#97BC62'
    ))
    
    fig.add_trace(go.Bar(
        name='Current Liabilities',
        x=['Liquidity Position'],
        y=[current_liab],
        marker_color='#F96167'
    ))
    
    fig.update_layout(
        title="Current Assets vs Current Liabilities",
        yaxis_title="Amount ($M)",
        height=400,
        barmode='group'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    if current_assets > current_liab:
        surplus = current_assets - current_liab
        st.success(f"✅ **Liquidity Surplus:** ${surplus:.0f}M - Company can easily meet short-term obligations")
    else:
        deficit = current_liab - current_assets
        st.error(f"❌ **Liquidity Deficit:** ${deficit:.0f}M - Company may struggle to meet short-term obligations")

def show_leverage():
    st.markdown('<div class="section-header">⚖️ Leverage & Solvency Ratios</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Measuring Financial Risk
    
    **Leverage ratios** measure the extent to which a company uses debt financing.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Capital Structure")
        total_debt = st.number_input("Total Debt ($M)", value=3000.0, step=100.0, key="lev_debt")
        total_equity_lev = st.number_input("Total Equity ($M)", value=2000.0, step=100.0, key="lev_eq")
        
        st.markdown("#### Coverage Ratios")
        ebit_lev = st.number_input("EBIT ($M)", value=800.0, step=50.0, key="lev_ebit")
        interest_lev = st.number_input("Interest Expense ($M)", value=200.0, step=10.0, key="lev_int")
    
    with col2:
        # Calculate ratios
        total_capital = total_debt + total_equity_lev
        debt_to_equity = total_debt / total_equity_lev if total_equity_lev > 0 else 0
        debt_to_capital = total_debt / total_capital if total_capital > 0 else 0
        equity_multiplier = total_capital / total_equity_lev if total_equity_lev > 0 else 0
        
        interest_coverage = ebit_lev / interest_lev if interest_lev > 0 else 0
        
        st.markdown(f"""
        <div class="concept-box">
        <h4>Capital Structure Summary</h4>
        <p>Total Debt: ${total_debt:.0f}M ({debt_to_capital*100:.1f}%)</p>
        <p>Total Equity: ${total_equity_lev:.0f}M ({(1-debt_to_capital)*100:.1f}%)</p>
        <p>Total Capital: ${total_capital:.0f}M</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Display leverage metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Debt-to-Equity Ratio")
        st.markdown("""
        <div class="ratio-box">
        <strong>Formula:</strong><br>
        Total Debt / Total Equity
        </div>
        """, unsafe_allow_html=True)
        
        if debt_to_equity < 0.5:
            color = "#97BC62"
            rating = "Conservative"
        elif debt_to_equity < 1.0:
            color = "#028090"
            rating = "Moderate"
        elif debt_to_equity < 2.0:
            color = "#F9E795"
            rating = "Aggressive"
        else:
            color = "#F96167"
            rating = "Very High Risk"
        
        st.markdown(f"""
        <div class="metric-good" style="background-color: {color}; color: {'white' if color in ['#97BC62', '#F96167'] else 'black'};">
        <h2>{debt_to_equity:.2f}</h2>
        <p>{rating}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### Debt-to-Capital Ratio")
        st.markdown("""
        <div class="ratio-box">
        <strong>Formula:</strong><br>
        Total Debt / (Debt + Equity)
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="metric-good" style="background-color: #028090; color: white;">
        <h2>{debt_to_capital*100:.1f}%</h2>
        <p>Debt portion</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("#### Interest Coverage")
        st.markdown("""
        <div class="ratio-box">
        <strong>Formula:</strong><br>
        EBIT / Interest Expense
        </div>
        """, unsafe_allow_html=True)
        
        if interest_coverage >= 5:
            color = "#97BC62"
            rating = "Safe"
        elif interest_coverage >= 3:
            color = "#028090"
            rating = "Adequate"
        elif interest_coverage >= 1.5:
            color = "#F9E795"
            rating = "At Risk"
        else:
            color = "#F96167"
            rating = "Distressed"
        
        st.markdown(f"""
        <div class="metric-good" style="background-color: {color}; color: {'white' if color in ['#97BC62', '#F96167'] else 'black'};">
        <h2>{interest_coverage:.2f}x</h2>
        <p>{rating}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("**Benchmark:** > 3x is good")
    
    st.markdown("---")
    
    # Capital structure pie chart
    st.markdown("### 🥧 Capital Structure Visualization")
    
    fig = go.Figure(data=[go.Pie(
        labels=['Debt', 'Equity'],
        values=[total_debt, total_equity_lev],
        marker=dict(colors=['#F96167', '#97BC62']),
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>Amount: $%{value:.0f}M<br>Percentage: %{percent}<extra></extra>'
    )])
    
    fig.update_layout(title="Debt vs Equity", height=400)
    st.plotly_chart(fig, use_container_width=True)

def show_complete_analysis():
    st.markdown('<div class="section-header">📊 Complete Financial Analysis</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Comprehensive Company Analysis
    
    Input complete financial data to get a full ratio analysis dashboard.
    """)
    
    # Comprehensive input
    with st.expander("📄 Input Financial Statements", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### Income Statement")
            revenue_full = st.number_input("Revenue ($M)", value=10000.0, step=100.0, key="full_rev")
            cogs_full = st.number_input("COGS ($M)", value=6000.0, step=100.0, key="full_cogs")
            opex_full = st.number_input("Operating Expenses ($M)", value=2000.0, step=100.0, key="full_opex")
            interest_full = st.number_input("Interest Expense ($M)", value=200.0, step=10.0, key="full_int")
            tax_full = st.number_input("Tax Expense ($M)", value=450.0, step=10.0, key="full_tax")
        
        with col2:
            st.markdown("#### Balance Sheet - Assets")
            cash_full = st.number_input("Cash ($M)", value=500.0, step=50.0, key="full_cash")
            ar_full = st.number_input("Accounts Receivable ($M)", value=800.0, step=50.0, key="full_ar")
            inv_full = st.number_input("Inventory ($M)", value=1200.0, step=50.0, key="full_inv")
            ppe_full = st.number_input("PP&E ($M)", value=2500.0, step=100.0, key="full_ppe")
        
        with col3:
            st.markdown("#### Balance Sheet - Liabilities & Equity")
            ap_full = st.number_input("Accounts Payable ($M)", value=600.0, step=50.0, key="full_ap")
            st_debt_full = st.number_input("Short-term Debt ($M)", value=400.0, step=50.0, key="full_std")
            lt_debt_full = st.number_input("Long-term Debt ($M)", value=2000.0, step=100.0, key="full_ltd")
            equity_full = st.number_input("Shareholders' Equity ($M)", value=2000.0, step=100.0, key="full_eq")
    
    # Calculate all metrics
    gross_profit_full = revenue_full - cogs_full
    ebit_full = gross_profit_full - opex_full
    ebt_full = ebit_full - interest_full
    net_income_full = ebt_full - tax_full
    
    current_assets_full = cash_full + ar_full + inv_full
    total_assets_full = current_assets_full + ppe_full
    
    current_liab_full = ap_full + st_debt_full
    total_debt_full = st_debt_full + lt_debt_full
    total_liab_full = current_liab_full + lt_debt_full
    
    # All ratios
    roe_full = (net_income_full / equity_full * 100) if equity_full > 0 else 0
    roa_full = (net_income_full / total_assets_full * 100) if total_assets_full > 0 else 0
    gross_margin_full = (gross_profit_full / revenue_full * 100) if revenue_full > 0 else 0
    operating_margin_full = (ebit_full / revenue_full * 100) if revenue_full > 0 else 0
    net_margin_full = (net_income_full / revenue_full * 100) if revenue_full > 0 else 0
    
    asset_turnover_full = revenue_full / total_assets_full if total_assets_full > 0 else 0
    
    current_ratio_full = current_assets_full / current_liab_full if current_liab_full > 0 else 0
    quick_ratio_full = (cash_full + ar_full) / current_liab_full if current_liab_full > 0 else 0
    
    debt_to_equity_full = total_debt_full / equity_full if equity_full > 0 else 0
    interest_coverage_full = ebit_full / interest_full if interest_full > 0 else 0
    
    # Dashboard
    st.markdown("---")
    st.markdown("### 📊 Financial Dashboard")
    
    # Profitability
    st.markdown("#### 💰 Profitability")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    col1.metric("ROE", f"{roe_full:.1f}%")
    col2.metric("ROA", f"{roa_full:.1f}%")
    col3.metric("Gross Margin", f"{gross_margin_full:.1f}%")
    col4.metric("Operating Margin", f"{operating_margin_full:.1f}%")
    col5.metric("Net Margin", f"{net_margin_full:.1f}%")
    
    # Efficiency
    st.markdown("#### ⚡ Efficiency")
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("Asset Turnover", f"{asset_turnover_full:.2f}x")
    col2.metric("Days Sales Outstanding", f"{(ar_full/revenue_full*365):.0f} days")
    col3.metric("Days Inventory", f"{(inv_full/cogs_full*365):.0f} days")
    col4.metric("Days Payable", f"{(ap_full/cogs_full*365):.0f} days")
    
    # Liquidity
    st.markdown("#### 💧 Liquidity")
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Current Ratio", f"{current_ratio_full:.2f}")
    col2.metric("Quick Ratio", f"{quick_ratio_full:.2f}")
    col3.metric("Working Capital", f"${current_assets_full - current_liab_full:.0f}M")
    
    # Leverage
    st.markdown("#### ⚖️ Leverage")
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Debt-to-Equity", f"{debt_to_equity_full:.2f}")
    col2.metric("Interest Coverage", f"{interest_coverage_full:.2f}x")
    col3.metric("Equity Multiplier", f"{total_assets_full/equity_full:.2f}x")
    
    st.markdown("---")
    
    # Summary scorecard
    st.markdown("### 📋 Overall Health Scorecard")
    
    # Score each category
    prof_score = (roe_full >= 15) + (roa_full >= 10) + (net_margin_full >= 10)
    liq_score = (current_ratio_full >= 1.5) + (quick_ratio_full >= 1.0)
    lev_score = (debt_to_equity_full <= 1.0) + (interest_coverage_full >= 3)
    
    total_score = prof_score + liq_score + lev_score
    max_score = 7
    
    score_pct = (total_score / max_score) * 100
    
    if score_pct >= 80:
        overall_rating = "Excellent"
        color = "#97BC62"
    elif score_pct >= 60:
        overall_rating = "Good"
        color = "#028090"
    elif score_pct >= 40:
        overall_rating = "Fair"
        color = "#F9E795"
    else:
        overall_rating = "Poor"
        color = "#F96167"
    
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("Profitability", f"{prof_score}/3")
    col2.metric("Liquidity", f"{liq_score}/2")
    col3.metric("Leverage", f"{lev_score}/2")
    col4.metric("Overall", f"{total_score}/{max_score}")
    
    st.markdown(f"""
    <div class="metric-good" style="background-color: {color}; color: {'white' if color in ['#97BC62', '#F96167'] else 'black'};">
    <h2>Financial Health: {overall_rating}</h2>
    <p>Score: {score_pct:.0f}%</p>
    </div>
    """, unsafe_allow_html=True)

def show_quiz():
    st.markdown('<div class="section-header">✅ Test Your Knowledge</div>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'ch14_score' not in st.session_state:
        st.session_state.ch14_score = 0
    if 'ch14_submitted' not in st.session_state:
        st.session_state.ch14_submitted = set()
    
    # Question 1
    st.markdown("### Question 1: ROE Decomposition")
    st.markdown("In the DuPont formula, ROE is NOT directly affected by:")
    
    q1 = st.radio("",
                 ["A) Profit margin", "B) Asset turnover", "C) Current ratio", "D) Financial leverage"],
                 key="q1", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q1_btn") and "q1" not in st.session_state.ch14_submitted:
        st.session_state.ch14_submitted.add("q1")
        if q1 == "C) Current ratio":
            st.success("✅ Correct! Current ratio measures liquidity, not ROE.")
            st.session_state.ch14_score += 1
        else:
            st.error("❌ Incorrect. Current ratio is not part of the DuPont formula.")
    
    st.markdown("---")
    
    # Question 2
    st.markdown("### Question 2: Liquidity")
    st.markdown("The most conservative liquidity measure is:")
    
    q2 = st.radio("",
                 ["A) Current ratio", "B) Quick ratio", "C) Cash ratio", "D) Working capital"],
                 key="q2", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q2_btn") and "q2" not in st.session_state.ch14_submitted:
        st.session_state.ch14_submitted.add("q2")
        if q2 == "C) Cash ratio":
            st.success("✅ Correct! Cash ratio only includes cash, the most liquid asset.")
            st.session_state.ch14_score += 1
        else:
            st.error("❌ Incorrect. Cash ratio is most conservative (Cash/Current Liabilities).")
    
    st.markdown("---")
    
    # Question 3
    st.markdown("### Question 3: Leverage")
    st.markdown("If a company has positive ROA but negative ROE, this suggests:")
    
    q3 = st.radio("",
                 ["A) High profitability", "B) Excessive leverage with high interest costs",
                  "C) Strong liquidity", "D) Low asset turnover"],
                 key="q3", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q3_btn") and "q3" not in st.session_state.ch14_submitted:
        st.session_state.ch14_submitted.add("q3")
        if q3 == "B) Excessive leverage with high interest costs":
            st.success("✅ Correct! High interest expense can make ROE negative even with positive ROA.")
            st.session_state.ch14_score += 1
        else:
            st.error("❌ Incorrect. Excessive interest expense from high leverage causes this.")
    
    st.markdown("---")
    
    # Question 4
    st.markdown("### Question 4: Economic Value Added")
    st.markdown("A positive EVA indicates that the firm is:")
    
    q4 = st.radio("",
                 ["A) Earning less than its cost of capital", "B) Earning more than its cost of capital",
                  "C) Breaking even", "D) Has zero debt"],
                 key="q4", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q4_btn") and "q4" not in st.session_state.ch14_submitted:
        st.session_state.ch14_submitted.add("q4")
        if q4 == "B) Earning more than its cost of capital":
            st.success("✅ Correct! EVA = (ROA - WACC) × Assets. Positive means creating value.")
            st.session_state.ch14_score += 1
        else:
            st.error("❌ Incorrect. Positive EVA means returns exceed the cost of capital.")
    
    st.markdown("---")
    
    # Question 5
    st.markdown("### Question 5: Financial Statements")
    st.markdown("The statement that shows cash generated from operations is:")
    
    q5 = st.radio("",
                 ["A) Income statement", "B) Balance sheet",
                  "C) Cash flow statement", "D) Statement of retained earnings"],
                 key="q5", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q5_btn") and "q5" not in st.session_state.ch14_submitted:
        st.session_state.ch14_submitted.add("q5")
        if q5 == "C) Cash flow statement":
            st.success("✅ Correct! The cash flow statement shows operating, investing, and financing cash flows.")
            st.session_state.ch14_score += 1
        else:
            st.error("❌ Incorrect. Cash flow statement shows cash from operations.")
    
    st.markdown("---")
    
    # Score Display
    if len(st.session_state.ch14_submitted) > 0:
        score_pct = (st.session_state.ch14_score / len(st.session_state.ch14_submitted)) * 100
        
        st.markdown(f"""
        <div class="concept-box">
        <h2>Your Score: {st.session_state.ch14_score} / {len(st.session_state.ch14_submitted)}</h2>
        <h3>{score_pct:.0f}%</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if score_pct >= 80:
            st.success("🎉 Excellent! You understand financial statement analysis very well.")
        elif score_pct >= 60:
            st.info("👍 Good work! Review ratio calculations and interpretations.")
        else:
            st.warning("📚 Keep studying! Review the three statements and key ratios.")
    
    if st.button("Reset Quiz", key="reset_quiz"):
        st.session_state.ch14_score = 0
        st.session_state.ch14_submitted = set()
        st.rerun()

if __name__ == "__main__":
    main()
