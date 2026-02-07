import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="International Investing",
    page_icon="🌍",
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
    .gain-box {
        background-color: #97BC62;
        padding: 1.5rem;
        border-radius: 8px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .loss-box {
        background-color: #F96167;
        padding: 1.5rem;
        border-radius: 8px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .warning-box {
        background-color: #F9E795;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
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
         "🌍 Global Markets",
         "💱 Exchange Rate Risk",
         "🔄 Currency Conversions",
         "📊 International Diversification",
         "⚖️ Political Risk",
         "🎯 Performance Attribution",
         "✅ Quiz"]
    )
    
    if page == "🏠 Home":
        show_home()
    elif page == "🌍 Global Markets":
        show_global_markets()
    elif page == "💱 Exchange Rate Risk":
        show_exchange_risk()
    elif page == "🔄 Currency Conversions":
        show_currency_conversions()
    elif page == "📊 International Diversification":
        show_diversification()
    elif page == "⚖️ Political Risk":
        show_political_risk()
    elif page == "🎯 Performance Attribution":
        show_attribution()
    elif page == "✅ Quiz":
        show_quiz()

def show_home():
    st.markdown('<div class="main-header">🌍 Globalization and International Investing</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">International Markets, Currency Risk & Diversification</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">🌍 Global Markets</h3>
        <p>Opportunities worldwide</p>
        <ul>
        <li>Developed markets</li>
        <li>Emerging markets</li>
        <li>Market capitalization</li>
        <li>GDP relationships</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">💱 Currency Risk</h3>
        <p>Exchange rate effects</p>
        <ul>
        <li>Currency appreciation/depreciation</li>
        <li>Return conversions</li>
        <li>Hedging strategies</li>
        <li>Carry trade</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">📊 Diversification</h3>
        <p>International benefits</p>
        <ul>
        <li>Correlation reduction</li>
        <li>Risk reduction</li>
        <li>Efficient frontier</li>
        <li>Home bias</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown('<div class="section-header">📋 Chapter Overview</div>', unsafe_allow_html=True)
    
    st.markdown("""
    This interactive app covers **Globalization and International Investing**.
    
    ### Why Invest Internationally?
    
    1. **Diversification** - Lower correlation between countries
    2. **Growth Opportunities** - Access to emerging markets
    3. **Higher Returns** - Capture global growth
    4. **Risk Management** - Reduce country-specific risk
    
    ### Key Challenges:
    
    1. **Exchange Rate Risk** - Currency fluctuations affect returns
    2. **Political Risk** - Government policy changes
    3. **Information Barriers** - Less transparency
    4. **Higher Costs** - Transaction and management fees
    
    ### 🎯 Learning Objectives:
    
    By the end of this module, you will be able to:
    - Understand global equity market structure
    - Calculate returns with currency conversions
    - Assess exchange rate risk and hedging
    - Evaluate international diversification benefits
    - Analyze political risk factors
    - Perform international performance attribution
    """)
    
    st.info("💡 **Key Insight:** U.S. stocks represent only ~40% of global market cap. International diversification can reduce portfolio risk!")

def show_global_markets():
    st.markdown('<div class="section-header">🌍 Global Equity Markets</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### The Global Investment Landscape
    """)
    
    # Sample market data
    developed_markets = pd.DataFrame({
        'Country': ['United States', 'Japan', 'United Kingdom', 'France', 'Canada', 
                   'Germany', 'Switzerland', 'Australia'],
        'Market Cap ($ Trillion)': [45.0, 6.2, 3.2, 2.8, 2.5, 2.1, 1.9, 1.7],
        'GDP ($ Trillion)': [23.0, 4.2, 3.1, 2.9, 2.1, 4.3, 0.8, 1.7],
        'Type': ['Developed']*8
    })
    
    emerging_markets = pd.DataFrame({
        'Country': ['China', 'India', 'Brazil', 'South Korea', 'Taiwan', 
                   'Mexico', 'Indonesia', 'South Africa'],
        'Market Cap ($ Trillion)': [11.2, 3.5, 1.1, 1.8, 1.7, 0.5, 0.6, 0.9],
        'GDP ($ Trillion)': [17.9, 3.7, 2.1, 1.7, 0.8, 1.4, 1.3, 0.4],
        'Type': ['Emerging']*8
    })
    
    all_markets = pd.concat([developed_markets, emerging_markets])
    
    # Calculate percentages
    total_market_cap = all_markets['Market Cap ($ Trillion)'].sum()
    all_markets['% of World'] = (all_markets['Market Cap ($ Trillion)'] / total_market_cap * 100).round(1)
    all_markets['Market Cap/GDP'] = (all_markets['Market Cap ($ Trillion)'] / all_markets['GDP ($ Trillion)'] * 100).round(0)
    
    tab1, tab2, tab3 = st.tabs(["Market Capitalization", "Developed vs Emerging", "Market Cap/GDP"])
    
    with tab1:
        st.markdown("### 🌐 Global Market Capitalization Distribution")
        
        fig = px.treemap(all_markets, 
                        path=['Type', 'Country'],
                        values='Market Cap ($ Trillion)',
                        title='World Equity Market Capitalization',
                        color='Type',
                        color_discrete_map={'Developed': '#028090', 'Emerging': '#97BC62'})
        
        fig.update_layout(height=600)
        st.plotly_chart(fig, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="concept-box">
            <h4>Total World Market Cap</h4>
            <h2>${total_market_cap:.1f} Trillion</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            us_pct = (45.0 / total_market_cap) * 100
            st.markdown(f"""
            <div class="concept-box">
            <h4>U.S. Share of World</h4>
            <h2>{us_pct:.1f}%</h2>
            <p>~{100-us_pct:.0f}% is non-U.S.!</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 📊 Developed vs Emerging Markets")
        
        # Bar chart comparison
        comparison = all_markets.groupby('Type')[['Market Cap ($ Trillion)', 'GDP ($ Trillion)']].sum().reset_index()
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Market Cap',
            x=comparison['Type'],
            y=comparison['Market Cap ($ Trillion)'],
            marker_color='#028090'
        ))
        fig.add_trace(go.Bar(
            name='GDP',
            x=comparison['Type'],
            y=comparison['GDP ($ Trillion)'],
            marker_color='#97BC62'
        ))
        
        fig.update_layout(
            title="Developed vs Emerging: Market Cap & GDP",
            yaxis_title="Trillions ($)",
            barmode='group',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Table
        st.markdown("#### Market Data by Country")
        display_df = all_markets[['Country', 'Type', 'Market Cap ($ Trillion)', 'GDP ($ Trillion)', '% of World']].sort_values('Market Cap ($ Trillion)', ascending=False)
        st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    with tab3:
        st.markdown("### 📈 Market Capitalization as % of GDP")
        
        st.markdown("""
        <div class="concept-box">
        <h4>What This Shows</h4>
        <p><strong>Market Cap/GDP ratio</strong> indicates financial market development:</p>
        <ul>
        <li><strong>High ratio (>100%):</strong> Well-developed financial markets</li>
        <li><strong>Low ratio (<50%):</strong> Underdeveloped markets, growth potential</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        fig = px.bar(all_markets.sort_values('Market Cap/GDP', ascending=True),
                    x='Market Cap/GDP',
                    y='Country',
                    orientation='h',
                    color='Type',
                    title='Market Capitalization as % of GDP',
                    color_discrete_map={'Developed': '#028090', 'Emerging': '#97BC62'})
        
        fig.update_layout(height=600, xaxis_title="Market Cap / GDP (%)")
        st.plotly_chart(fig, use_container_width=True)

def show_exchange_risk():
    st.markdown('<div class="section-header">💱 Exchange Rate Risk</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Currency Risk: The Hidden Factor
    
    When investing internationally, you're exposed to **two sources of return**:
    1. **Local market return** (stock performance in local currency)
    2. **Currency return** (exchange rate changes)
    """)
    
    st.markdown("""
    <div class="formula-box">
    <strong>Total Return (in USD) = (1 + Local Return) × (1 + Currency Return) - 1</strong><br><br>
    Or approximately: Total Return ≈ Local Return + Currency Return
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive Calculator
    st.markdown("### 🧮 Currency Impact Calculator")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("#### Investment Details")
        local_return = st.slider("Local Market Return (%)", -30.0, 50.0, 10.0, 1.0, key="fx_local") / 100
        
        st.markdown("#### Exchange Rate")
        initial_rate = st.number_input("Initial Exchange Rate (Foreign/USD)", value=2.0, step=0.1, key="fx_init")
        final_rate = st.number_input("Final Exchange Rate (Foreign/USD)", value=2.1, step=0.1, key="fx_final")
        
        # Example: £1 = $2 initially, £1 = $2.10 finally
        st.markdown("""
        <div class="concept-box" style="font-size: 0.9rem;">
        <p><strong>Example:</strong> British Pound</p>
        <p>Initial: £1 = ${:.2f}</p>
        <p>Final: £1 = ${:.2f}</p>
        </div>
        """.format(initial_rate, final_rate), unsafe_allow_html=True)
    
    with col2:
        # Calculate currency return
        currency_return = (final_rate - initial_rate) / initial_rate
        
        # Total return
        total_return_exact = (1 + local_return) * (1 + currency_return) - 1
        total_return_approx = local_return + currency_return
        
        # Dollar appreciation or depreciation
        if currency_return > 0:
            fx_status = "Foreign Currency APPRECIATED"
            fx_color = "gain-box"
            fx_effect = "GAIN"
        elif currency_return < 0:
            fx_status = "Foreign Currency DEPRECATED"
            fx_color = "loss-box"
            fx_effect = "LOSS"
        else:
            fx_status = "No Currency Change"
            fx_color = "concept-box"
            fx_effect = "NEUTRAL"
        
        st.markdown(f"""
        <div class="{fx_color}">
        <h3>{fx_status}</h3>
        <h2>{fx_effect}: {abs(currency_return)*100:.2f}%</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Results breakdown
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.metric("Local Return", f"{local_return*100:.2f}%")
            st.metric("Currency Return", f"{currency_return*100:.2f}%")
        
        with col_b:
            st.metric("Total Return (Exact)", f"{total_return_exact*100:.2f}%")
            st.metric("Total Return (Approx)", f"{total_return_approx*100:.2f}%")
        
        # Investment example
        investment = 10000
        local_value = investment * (1 + local_return)
        total_value = investment * (1 + total_return_exact)
        currency_impact = total_value - local_value
        
        st.markdown(f"""
        <div class="concept-box">
        <h4>On $10,000 Investment</h4>
        <p><strong>Value from stock gains:</strong> ${local_value:,.2f}</p>
        <p><strong>Currency impact:</strong> ${currency_impact:+,.2f}</p>
        <hr>
        <p><strong>Final USD value:</strong> ${total_value:,.2f}</p>
        <p><strong>Total profit/loss:</strong> ${(total_value - investment):+,.2f}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Visualization
    st.markdown("### 📊 Currency Risk Scenarios")
    
    scenarios = {
        'Strong Depreciation': -0.15,
        'Mild Depreciation': -0.05,
        'No Change': 0.00,
        'Mild Appreciation': 0.05,
        'Strong Appreciation': 0.15
    }
    
    scenario_returns = []
    for scenario, fx_change in scenarios.items():
        total = (1 + local_return) * (1 + fx_change) - 1
        scenario_returns.append({
            'Scenario': scenario,
            'Currency Change': f'{fx_change*100:+.0f}%',
            'Total Return': total * 100
        })
    
    scenario_df = pd.DataFrame(scenario_returns)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=scenario_df['Scenario'],
        y=scenario_df['Total Return'],
        marker_color=['#F96167', '#F9E795', '#CADCFC', '#97BC62', '#028090'],
        text=[f'{r:.1f}%' for r in scenario_df['Total Return']],
        textposition='outside'
    ))
    
    fig.add_hline(y=local_return*100, line_dash="dash", line_color="red",
                 annotation_text=f"Local Return: {local_return*100:.1f}%")
    
    fig.update_layout(
        title="How Currency Changes Affect Total Returns",
        xaxis_title="Currency Scenario",
        yaxis_title="Total Return in USD (%)",
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_currency_conversions():
    st.markdown('<div class="section-header">🔄 Currency Conversions & Arbitrage</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Basic Conversion", "Carry Trade", "Covered Interest Arbitrage"])
    
    with tab1:
        st.markdown("### 💱 Currency Conversion Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            amount_usd = st.number_input("Amount in USD ($)", value=10000.0, step=100.0, key="conv_usd")
            exchange_rate = st.number_input("Exchange Rate (Foreign per USD)", value=0.85, step=0.01, key="conv_rate",
                                          help="E.g., EUR/USD = 0.85 means €0.85 per $1")
            
            foreign_amount = amount_usd * exchange_rate
            
            st.markdown(f"""
            <div class="concept-box">
            <h4>Conversion Result</h4>
            <p>${amount_usd:,.2f} USD</p>
            <p>= {foreign_amount:,.2f} Foreign Currency</p>
            <hr>
            <p><strong>Rate:</strong> {exchange_rate:.4f} per USD</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### Round-Trip Conversion")
            
            return_rate = st.number_input("Return Exchange Rate", value=0.88, step=0.01, key="conv_return")
            
            returned_usd = foreign_amount / return_rate
            round_trip_gain = returned_usd - amount_usd
            round_trip_pct = (round_trip_gain / amount_usd) * 100
            
            box_color = "gain-box" if round_trip_gain > 0 else "loss-box" if round_trip_gain < 0 else "concept-box"
            
            st.markdown(f"""
            <div class="{box_color}">
            <h4>Round-Trip Result</h4>
            <h2>${returned_usd:,.2f}</h2>
            <p>Gain/Loss: ${round_trip_gain:+,.2f}</p>
            <p>Return: {round_trip_pct:+.2f}%</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 📈 Carry Trade Strategy")
        
        st.markdown("""
        <div class="concept-box">
        <h4>What is a Carry Trade?</h4>
        <p>Borrow in low-interest currency, invest in high-interest currency.</p>
        <p><strong>Profit = Interest Rate Differential - Currency Depreciation</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            borrow_rate = st.slider("Borrow Rate (e.g., JPY) %", 0.0, 5.0, 0.5, 0.25, key="carry_borrow") / 100
            invest_rate = st.slider("Invest Rate (e.g., USD) %", 0.0, 10.0, 4.0, 0.25, key="carry_invest") / 100
            fx_change = st.slider("Currency Change %", -10.0, 10.0, -2.0, 0.5, key="carry_fx",
                                 help="Negative = borrowed currency appreciated") / 100
        
        with col2:
            interest_diff = invest_rate - borrow_rate
            net_return = interest_diff + fx_change
            
            investment_amt = 100000
            profit = investment_amt * net_return
            
            box_color = "gain-box" if net_return > 0 else "loss-box"
            
            st.markdown(f"""
            <div class="{box_color}">
            <h4>Carry Trade Result</h4>
            <h3>Net Return: {net_return*100:.2f}%</h3>
            <hr>
            <p>Interest earned: {invest_rate*100:.2f}%</p>
            <p>Interest paid: {borrow_rate*100:.2f}%</p>
            <p>Interest differential: {interest_diff*100:.2f}%</p>
            <p>Currency change: {fx_change*100:+.2f}%</p>
            <hr>
            <p><strong>Profit on $100K:</strong> ${profit:+,.2f}</p>
            </div>
            """, unsafe_allow_html=True)
            
            break_even = interest_diff
            st.warning(f"⚠️ **Break-even:** Borrowed currency can appreciate up to {break_even*100:.2f}% before losing money")
    
    with tab3:
        st.markdown("### 🔒 Covered Interest Arbitrage")
        
        st.markdown("""
        <div class="concept-box">
        <h4>Covered Interest Parity</h4>
        <p>The relationship that prevents arbitrage:</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="formula-box">
        <strong>F/S = (1 + r_domestic) / (1 + r_foreign)</strong><br><br>
        Where:<br>
        F = Forward rate<br>
        S = Spot rate<br>
        r = Interest rates
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Market Quotes")
            us_rate_arb = st.number_input("U.S. Interest Rate (%)", value=6.15, step=0.25, key="arb_us") / 100
            uk_rate_arb = st.number_input("UK Interest Rate (%)", value=10.0, step=0.25, key="arb_uk") / 100
            spot_rate = st.number_input("Spot Rate ($/£)", value=2.0, step=0.05, key="arb_spot")
            forward_rate = st.number_input("Forward Rate ($/£)", value=1.95, step=0.05, key="arb_forward")
        
        with col2:
            # Calculate fair forward rate
            fair_forward = spot_rate * (1 + us_rate_arb) / (1 + uk_rate_arb)
            
            # Arbitrage opportunity
            if abs(forward_rate - fair_forward) > 0.01:
                # Execute arbitrage
                borrow_usd = 1.0
                amount_gbp = borrow_usd / spot_rate
                invested_gbp = amount_gbp * (1 + uk_rate_arb)
                forward_usd = invested_gbp * forward_rate
                owe_usd = borrow_usd * (1 + us_rate_arb)
                arb_profit = forward_usd - owe_usd
                
                st.markdown(f"""
                <div class="gain-box">
                <h4>🚨 ARBITRAGE OPPORTUNITY!</h4>
                <h2>${arb_profit:.4f} per dollar</h2>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="concept-box">
                <h4>Arbitrage Steps:</h4>
                <ol>
                <li>Borrow $1.00 at {us_rate_arb*100:.2f}%</li>
                <li>Convert to £{amount_gbp:.4f} at spot</li>
                <li>Invest at {uk_rate_arb*100:.2f}% → £{invested_gbp:.4f}</li>
                <li>Sell forward at ${forward_rate:.2f}/£ → ${forward_usd:.4f}</li>
                <li>Repay ${owe_usd:.4f}</li>
                </ol>
                <p><strong>Risk-free profit:</strong> ${arb_profit:.4f}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="concept-box">
                <h4>✅ No Arbitrage</h4>
                <p><strong>Fair Forward Rate:</strong> ${fair_forward:.4f}/£</p>
                <p><strong>Actual Forward Rate:</strong> ${forward_rate:.4f}/£</p>
                <p>Rates are in equilibrium (covered interest parity holds)</p>
                </div>
                """, unsafe_allow_html=True)

def show_diversification():
    st.markdown('<div class="section-header">📊 International Diversification Benefits</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### The Power of Global Diversification
    
    International diversification can reduce portfolio risk through **low correlations** between markets.
    """)
    
    # Sample correlation matrix
    st.markdown("### 🔗 International Market Correlations")
    
    countries = ['US', 'UK', 'Japan', 'Germany', 'Emerging']
    correlation_matrix = pd.DataFrame(
        [[1.00, 0.75, 0.55, 0.70, 0.60],
         [0.75, 1.00, 0.60, 0.80, 0.55],
         [0.55, 0.60, 1.00, 0.65, 0.50],
         [0.70, 0.80, 0.65, 1.00, 0.58],
         [0.60, 0.55, 0.50, 0.58, 1.00]],
        index=countries,
        columns=countries
    )
    
    fig = px.imshow(correlation_matrix,
                    labels=dict(color="Correlation"),
                    x=countries,
                    y=countries,
                    color_continuous_scale='RdYlGn_r',
                    title="Historical Correlations Between Markets")
    
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 **Key Observation:** Correlations < 1.0 provide diversification benefits. Lower correlations = better diversification!")
    
    st.markdown("---")
    
    # Portfolio diversification simulator
    st.markdown("### 🎲 Diversification Benefit Calculator")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("#### Domestic Portfolio")
        us_weight = st.slider("U.S. Weight (%)", 0, 100, 100, 5, key="div_us") / 100
        
        st.markdown("#### International Allocation")
        intl_weight = 1 - us_weight
        
        if intl_weight > 0:
            developed_split = st.slider("Developed Markets (%)", 0, 100, 60, 5, key="div_dev") / 100
            emerging_split = 1 - developed_split
        else:
            developed_split = 0
            emerging_split = 0
        
        # Risk parameters
        us_std = 18.0
        dev_std = 20.0
        em_std = 28.0
        
        us_return = 10.0
        dev_return = 11.0
        em_return = 14.0
    
    with col2:
        # Calculate portfolio statistics
        port_return = (us_weight * us_return + 
                      intl_weight * developed_split * dev_return + 
                      intl_weight * emerging_split * em_return)
        
        # Simplified portfolio variance (assuming given correlations)
        us_var = (us_weight * us_std) ** 2
        dev_var = (intl_weight * developed_split * dev_std) ** 2
        em_var = (intl_weight * emerging_split * em_std) ** 2
        
        # Add correlation terms (simplified)
        correlation_effect = 2 * us_weight * intl_weight * developed_split * 0.70 * us_std * dev_std
        correlation_effect += 2 * us_weight * intl_weight * emerging_split * 0.60 * us_std * em_std
        correlation_effect += 2 * intl_weight * developed_split * intl_weight * emerging_split * 0.55 * dev_std * em_std
        
        port_variance = us_var + dev_var + em_var + correlation_effect
        port_std = np.sqrt(abs(port_variance))
        
        sharpe = (port_return - 3.0) / port_std
        
        st.markdown(f"""
        <div class="concept-box">
        <h4>Portfolio Composition</h4>
        <p><strong>U.S.:</strong> {us_weight*100:.0f}%</p>
        <p><strong>Developed Intl:</strong> {(intl_weight * developed_split)*100:.0f}%</p>
        <p><strong>Emerging:</strong> {(intl_weight * emerging_split)*100:.0f}%</p>
        </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.metric("Expected Return", f"{port_return:.2f}%")
            st.metric("Portfolio Risk", f"{port_std:.2f}%")
        
        with col_b:
            st.metric("Sharpe Ratio", f"{sharpe:.3f}")
            risk_reduction = ((us_std - port_std) / us_std) * 100
            st.metric("Risk Reduction", f"{risk_reduction:.1f}%")
    
    # Efficient frontier
    st.markdown("---")
    st.markdown("### 📈 International vs Domestic Efficient Frontier")
    
    # Generate efficient frontiers
    weights = np.linspace(0, 1, 50)
    
    domestic_returns = []
    domestic_risks = []
    intl_returns = []
    intl_risks = []
    
    for w in weights:
        # Domestic only (varying stock/bond mix)
        dom_ret = w * 10.0 + (1-w) * 4.0
        dom_risk = w * 18.0
        domestic_returns.append(dom_ret)
        domestic_risks.append(dom_risk)
        
        # International diversified
        intl_ret = w * 10.5 + (1-w) * 4.0
        intl_risk = w * 15.0  # Lower due to diversification
        intl_returns.append(intl_ret)
        intl_risks.append(intl_risk)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=domestic_risks, y=domestic_returns,
        mode='lines',
        name='Domestic Only',
        line=dict(color='#F96167', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=intl_risks, y=intl_returns,
        mode='lines',
        name='International',
        line=dict(color='#97BC62', width=3)
    ))
    
    fig.update_layout(
        title="Efficient Frontier: Domestic vs International",
        xaxis_title="Risk (Standard Deviation %)",
        yaxis_title="Expected Return (%)",
        height=500,
        legend=dict(x=0.7, y=0.1)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("✅ **Benefit:** International diversification shifts the efficient frontier up and to the left (better risk-return trade-off)!")

def show_political_risk():
    st.markdown('<div class="section-header">⚖️ Political Risk Assessment</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Understanding Political Risk
    
    **Political risk** refers to the possibility that government actions will adversely affect investment returns.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="concept-box">
        <h4>Types of Political Risk</h4>
        <ul>
        <li><strong>Expropriation:</strong> Government seizes assets</li>
        <li><strong>Tax Changes:</strong> Increased taxation</li>
        <li><strong>Capital Controls:</strong> Restrictions on repatriating funds</li>
        <li><strong>Currency Restrictions:</strong> Limits on currency exchange</li>
        <li><strong>Regulatory Changes:</strong> New rules affecting business</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="concept-box">
        <h4>Risk Factors</h4>
        <ul>
        <li>Government stability</li>
        <li>Corruption levels</li>
        <li>Rule of law</li>
        <li>Democratic institutions</li>
        <li>Civil liberties</li>
        <li>Military influence</li>
        <li>External conflicts</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Sample political risk scores
    st.markdown("### 🗺️ Political Risk Scores by Country")
    
    political_risk_data = pd.DataFrame({
        'Country': ['Switzerland', 'Norway', 'Singapore', 'Germany', 'United States', 
                   'Japan', 'United Kingdom', 'South Korea', 'Brazil', 'India', 
                   'Russia', 'China', 'Turkey', 'Argentina', 'Venezuela'],
        'Political Risk Score': [92, 90, 88, 87, 83, 82, 81, 78, 65, 62, 55, 58, 48, 45, 25],
        'Category': ['Very Low', 'Very Low', 'Very Low', 'Very Low', 'Low', 
                    'Low', 'Low', 'Low', 'Moderate', 'Moderate', 
                    'High', 'High', 'High', 'High', 'Very High']
    })
    
    fig = px.bar(political_risk_data.sort_values('Political Risk Score'),
                x='Political Risk Score',
                y='Country',
                orientation='h',
                color='Category',
                title='Political Risk Scores (100 = Lowest Risk)',
                color_discrete_map={
                    'Very Low': '#97BC62',
                    'Low': '#028090',
                    'Moderate': '#F9E795',
                    'High': '#F96167',
                    'Very High': '#8B0000'
                })
    
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Interactive risk assessment
    st.markdown("### 🎯 Country Risk Assessment Tool")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("#### Risk Factors (0-100)")
        
        gov_stability = st.slider("Government Stability", 0, 100, 70, 5, key="pr_gov")
        rule_of_law = st.slider("Rule of Law", 0, 100, 65, 5, key="pr_law")
        corruption = st.slider("Anti-Corruption", 0, 100, 60, 5, key="pr_corr")
        economy = st.slider("Economic Health", 0, 100, 75, 5, key="pr_econ")
        military = st.slider("Civil Peace", 0, 100, 80, 5, key="pr_mil")
    
    with col2:
        # Calculate composite score
        weights = [0.25, 0.25, 0.15, 0.20, 0.15]
        factors = [gov_stability, rule_of_law, corruption, economy, military]
        composite_score = sum(w * f for w, f in zip(weights, factors))
        
        # Determine risk category
        if composite_score >= 80:
            risk_category = "Very Low Risk"
            risk_color = "gain-box"
            recommendation = "Suitable for conservative investors"
        elif composite_score >= 65:
            risk_category = "Low Risk"
            risk_color = "gain-box"
            recommendation = "Good for most investors"
        elif composite_score >= 50:
            risk_category = "Moderate Risk"
            risk_color = "warning-box"
            recommendation = "Suitable for risk-tolerant investors"
        elif composite_score >= 35:
            risk_category = "High Risk"
            risk_color = "loss-box"
            recommendation = "Only for aggressive investors"
        else:
            risk_category = "Very High Risk"
            risk_color = "loss-box"
            recommendation = "Avoid or very small allocation"
        
        st.markdown(f"""
        <div class="{risk_color}">
        <h3>Composite Risk Score</h3>
        <h1>{composite_score:.0f}</h1>
        <h4>{risk_category}</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="concept-box">
        <h4>Investment Recommendation</h4>
        <p>{recommendation}</p>
        <hr>
        <h5>Score Breakdown:</h5>
        <p>Government Stability: {gov_stability:.0f}</p>
        <p>Rule of Law: {rule_of_law:.0f}</p>
        <p>Anti-Corruption: {corruption:.0f}</p>
        <p>Economic Health: {economy:.0f}</p>
        <p>Civil Peace: {military:.0f}</p>
        </div>
        """, unsafe_allow_html=True)

def show_attribution():
    st.markdown('<div class="section-header">🎯 International Performance Attribution</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Decomposing International Returns
    
    For international portfolios, performance attribution includes additional factors:
    1. **Currency Selection** - Currency hedging decisions
    2. **Country Selection** - Which countries to overweight/underweight
    3. **Stock Selection** - Which stocks within each country
    4. **Asset Allocation** - Stocks vs bonds vs cash
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 International Attribution Analysis")
    
    # Sample countries
    countries = ['United States', 'United Kingdom', 'Japan']
    
    st.markdown("#### Define Portfolio Weights and Returns")
    
    attribution_data = []
    
    for i, country in enumerate(countries):
        st.markdown(f"##### {country}")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            bench_weight = st.number_input(f"Benchmark %", value=[50.0, 30.0, 20.0][i], 
                                          step=1.0, key=f"attr_bw_{i}") / 100
        
        with col2:
            port_weight = st.number_input(f"Portfolio %", value=[45.0, 35.0, 20.0][i], 
                                         step=1.0, key=f"attr_pw_{i}") / 100
        
        with col3:
            bench_return = st.number_input(f"Bench Return %", value=[12.0, 10.0, 8.0][i], 
                                          step=0.5, key=f"attr_br_{i}") / 100
        
        with col4:
            port_return = st.number_input(f"Port Return %", value=[13.0, 11.0, 7.5][i], 
                                         step=0.5, key=f"attr_pr_{i}") / 100
        
        attribution_data.append({
            'Country': country,
            'Benchmark Weight': bench_weight,
            'Portfolio Weight': port_weight,
            'Benchmark Return': bench_return,
            'Portfolio Return': port_return
        })
    
    st.markdown("---")
    
    # Calculate attribution
    st.markdown("### 📋 Attribution Results")
    
    # Benchmark total return
    bench_total = sum(d['Benchmark Weight'] * d['Benchmark Return'] for d in attribution_data)
    
    # Portfolio total return
    port_total = sum(d['Portfolio Weight'] * d['Portfolio Return'] for d in attribution_data)
    
    # Excess return
    excess_return = port_total - bench_total
    
    # Attribution effects
    results = []
    allocation_total = 0
    selection_total = 0
    
    for d in attribution_data:
        # Allocation effect: (Portfolio weight - Benchmark weight) × Benchmark return
        allocation = (d['Portfolio Weight'] - d['Benchmark Weight']) * d['Benchmark Return']
        allocation_total += allocation
        
        # Selection effect: Benchmark weight × (Portfolio return - Benchmark return)
        selection = d['Benchmark Weight'] * (d['Portfolio Return'] - d['Benchmark Return'])
        selection_total += selection
        
        # Interaction effect
        interaction = (d['Portfolio Weight'] - d['Benchmark Weight']) * (d['Portfolio Return'] - d['Benchmark Return'])
        
        results.append({
            'Country': d['Country'],
            'Allocation Effect': f'{allocation*100:.2f}%',
            'Selection Effect': f'{selection*100:.2f}%',
            'Interaction': f'{interaction*100:.2f}%',
            'Total': f'{(allocation + selection + interaction)*100:.2f}%'
        })
    
    results_df = pd.DataFrame(results)
    st.dataframe(results_df, use_container_width=True, hide_index=True)
    
    # Summary
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="concept-box">
        <h4>Benchmark Return</h4>
        <h2>{bench_total*100:.2f}%</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="gain-box">
        <h4>Portfolio Return</h4>
        <h2>{port_total*100:.2f}%</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        box_color = "gain-box" if excess_return > 0 else "loss-box"
        st.markdown(f"""
        <div class="{box_color}">
        <h4>Excess Return</h4>
        <h2>{excess_return*100:+.2f}%</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(f"""
    <div class="concept-box">
    <h4>Attribution Summary</h4>
    <p><strong>Country Allocation Effect:</strong> {allocation_total*100:+.2f}%
    {' (Good country selection!)' if allocation_total > 0 else ' (Poor country selection)'}</p>
    <p><strong>Stock Selection Effect:</strong> {selection_total*100:+.2f}%
    {' (Good stock picking!)' if selection_total > 0 else ' (Poor stock picking)'}</p>
    <hr>
    <p><strong>Total Active Return:</strong> {excess_return*100:+.2f}%</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Visualization
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=['Allocation', 'Selection', 'Total'],
        y=[allocation_total*100, selection_total*100, excess_return*100],
        marker_color=['#028090', '#97BC62', '#1E2761'],
        text=[f'{allocation_total*100:.2f}%', f'{selection_total*100:.2f}%', f'{excess_return*100:.2f}%'],
        textposition='auto'
    ))
    
    fig.update_layout(
        title="Performance Attribution Breakdown",
        yaxis_title="Contribution to Excess Return (%)",
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_quiz():
    st.markdown('<div class="section-header">✅ Test Your Knowledge</div>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'ch19_score' not in st.session_state:
        st.session_state.ch19_score = 0
    if 'ch19_submitted' not in st.session_state:
        st.session_state.ch19_submitted = set()
    
    # Question 1
    st.markdown("### Question 1: Currency Risk")
    st.markdown("If a U.S. investor buys a foreign stock that rises 10% in local currency, but the foreign currency depreciates 5%, the approximate USD return is:")
    
    q1 = st.radio("",
                 ["A) 15%", "B) 10%", "C) 5%", "D) -5%"],
                 key="q1", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q1_btn") and "q1" not in st.session_state.ch19_submitted:
        st.session_state.ch19_submitted.add("q1")
        if q1 == "C) 5%":
            st.success("✅ Correct! Approx return = 10% + (-5%) = 5%")
            st.session_state.ch19_score += 1
        else:
            st.error("❌ Incorrect. Total return ≈ Local return + Currency return = 10% - 5% = 5%")
    
    st.markdown("---")
    
    # Question 2
    st.markdown("### Question 2: Diversification")
    st.markdown("The main benefit of international diversification is:")
    
    q2 = st.radio("",
                 ["A) Higher returns always", "B) Lower correlations between markets",
                  "C) No currency risk", "D) Guaranteed profits"],
                 key="q2", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q2_btn") and "q2" not in st.session_state.ch19_submitted:
        st.session_state.ch19_submitted.add("q2")
        if q2 == "B) Lower correlations between markets":
            st.success("✅ Correct! International diversification works because of imperfect correlations.")
            st.session_state.ch19_score += 1
        else:
            st.error("❌ Incorrect. The key benefit is lower correlations, which reduces portfolio risk.")
    
    st.markdown("---")
    
    # Question 3
    st.markdown("### Question 3: Political Risk")
    st.markdown("Political risk includes all EXCEPT:")
    
    q3 = st.radio("",
                 ["A) Expropriation of assets", "B) Changes in tax policy",
                  "C) Market volatility", "D) Currency restrictions"],
                 key="q3", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q3_btn") and "q3" not in st.session_state.ch19_submitted:
        st.session_state.ch19_submitted.add("q3")
        if q3 == "C) Market volatility":
            st.success("✅ Correct! Market volatility is market risk, not political risk.")
            st.session_state.ch19_score += 1
        else:
            st.error("❌ Incorrect. Market volatility is not political risk; it's market risk.")
    
    st.markdown("---")
    
    # Question 4
    st.markdown("### Question 4: Covered Interest Parity")
    st.markdown("Covered interest parity states that:")
    
    q4 = st.radio("",
                 ["A) All countries have equal interest rates", 
                  "B) Forward rates reflect interest rate differentials",
                  "C) Exchange rates never change", "D) Stocks always beat bonds"],
                 key="q4", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q4_btn") and "q4" not in st.session_state.ch19_submitted:
        st.session_state.ch19_submitted.add("q4")
        if q4 == "B) Forward rates reflect interest rate differentials":
            st.success("✅ Correct! CIP: F/S = (1 + r_domestic)/(1 + r_foreign)")
            st.session_state.ch19_score += 1
        else:
            st.error("❌ Incorrect. CIP links forward rates to interest rate differentials.")
    
    st.markdown("---")
    
    # Question 5
    st.markdown("### Question 5: Home Bias")
    st.markdown("The phenomenon where investors overweight domestic stocks is called:")
    
    q5 = st.radio("",
                 ["A) Market timing", "B) Home bias",
                  "C) Currency hedging", "D) Political risk"],
                 key="q5", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q5_btn") and "q5" not in st.session_state.ch19_submitted:
        st.session_state.ch19_submitted.add("q5")
        if q5 == "B) Home bias":
            st.success("✅ Correct! Home bias is the tendency to over-invest in domestic markets.")
            st.session_state.ch19_score += 1
        else:
            st.error("❌ Incorrect. This is called home bias.")
    
    st.markdown("---")
    
    # Score Display
    if len(st.session_state.ch19_submitted) > 0:
        score_pct = (st.session_state.ch19_score / len(st.session_state.ch19_submitted)) * 100
        
        st.markdown(f"""
        <div class="concept-box">
        <h2>Your Score: {st.session_state.ch19_score} / {len(st.session_state.ch19_submitted)}</h2>
        <h3>{score_pct:.0f}%</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if score_pct >= 80:
            st.success("🎉 Excellent! You understand international investing well.")
        elif score_pct >= 60:
            st.info("👍 Good work! Review currency risk and diversification benefits.")
        else:
            st.warning("📚 Keep studying! Review exchange rates and international diversification.")
    
    if st.button("Reset Quiz", key="reset_quiz"):
        st.session_state.ch19_score = 0
        st.session_state.ch19_submitted = set()
        st.rerun()

if __name__ == "__main__":
    main()
