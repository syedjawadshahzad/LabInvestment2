import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Options Markets",
    page_icon="📈",
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
    .call-box {
        background-color: #97BC62;
        padding: 1rem;
        border-radius: 8px;
        color: white;
        margin: 0.5rem 0;
    }
    .put-box {
        background-color: #F96167;
        padding: 1rem;
        border-radius: 8px;
        color: white;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Helper Functions
def call_payoff(stock_price, strike, premium, position='long'):
    """Calculate call option payoff"""
    if position == 'long':
        intrinsic = np.maximum(stock_price - strike, 0)
        return intrinsic - premium
    else:  # short
        intrinsic = -np.maximum(stock_price - strike, 0)
        return intrinsic + premium

def put_payoff(stock_price, strike, premium, position='long'):
    """Calculate put option payoff"""
    if position == 'long':
        intrinsic = np.maximum(strike - stock_price, 0)
        return intrinsic - premium
    else:  # short
        intrinsic = -np.maximum(strike - stock_price, 0)
        return intrinsic + premium

# Main App
def main():
    # Sidebar Navigation
    st.sidebar.markdown("## 📚 Navigation")
    page = st.sidebar.radio(
        "Choose a topic:",
        ["🏠 Home",
         "📞 Call Options",
         "📉 Put Options",
         "🎨 Payoff Diagrams",
         "🛡️ Option Strategies",
         "🔧 Strategy Builder",
         "💼 Advanced Strategies",
         "✅ Quiz"]
    )
    
    if page == "🏠 Home":
        show_home()
    elif page == "📞 Call Options":
        show_call_options()
    elif page == "📉 Put Options":
        show_put_options()
    elif page == "🎨 Payoff Diagrams":
        show_payoff_diagrams()
    elif page == "🛡️ Option Strategies":
        show_option_strategies()
    elif page == "🔧 Strategy Builder":
        show_strategy_builder()
    elif page == "💼 Advanced Strategies":
        show_advanced_strategies()
    elif page == "✅ Quiz":
        show_quiz()

def show_home():
    st.markdown('<div class="main-header">📈 Options Markets</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Options Contracts & Trading Strategies</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="call-box">
        <h3>📞 Call Options</h3>
        <p>Right to BUY</p>
        <ul>
        <li>Bullish strategy</li>
        <li>Limited downside</li>
        <li>Unlimited upside</li>
        <li>Leverage</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="put-box">
        <h3>📉 Put Options</h3>
        <p>Right to SELL</p>
        <ul>
        <li>Bearish strategy</li>
        <li>Portfolio insurance</li>
        <li>Limited downside</li>
        <li>High upside</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="concept-box">
        <h3 style="color: #028090;">🎨 Strategies</h3>
        <p>Combine options</p>
        <ul>
        <li>Protective put</li>
        <li>Covered call</li>
        <li>Straddle</li>
        <li>Spreads</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown('<div class="section-header">📋 Chapter Overview</div>', unsafe_allow_html=True)
    
    st.markdown("""
    This interactive app covers **Options Markets** from *Essentials of Investments* by Bodie, Kane, and Marcus.
    
    ### Option Basics:
    
    - **Call Option:** Right (not obligation) to **BUY** an asset at a specified price
    - **Put Option:** Right (not obligation) to **SELL** an asset at a specified price
    - **Strike Price (K):** The agreed-upon transaction price
    - **Premium:** The price paid for the option
    - **Expiration:** When the option contract ends
    
    ### 🎯 Learning Objectives:
    
    By the end of this module, you will be able to:
    - Understand call and put option mechanics
    - Draw and interpret payoff diagrams
    - Calculate option profits and losses
    - Design and analyze option strategies
    - Compare protective puts, covered calls, straddles, and spreads
    - Apply options for hedging and speculation
    """)
    
    st.info("💡 **Key Insight:** Options provide asymmetric payoffs - limited downside, potentially unlimited upside. This makes them powerful tools for hedging and speculation!")

def show_call_options():
    st.markdown('<div class="section-header">📞 Call Options</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### What is a Call Option?
    
    A **call option** gives the holder the **right to BUY** an asset at a specified **strike price** on or before expiration.
    """)
    
    st.markdown("""
    <div class="formula-box">
    <strong>Call Option Payoff at Expiration:</strong><br><br>
    Payoff = max(Sᴛ - K, 0)<br>
    Profit = Payoff - Premium<br><br>
    Where:<br>
    Sᴛ = Stock price at expiration<br>
    K = Strike price
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive Call Option
    st.markdown("### 📊 Interactive Call Option Analysis")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Option Details")
        strike_call = st.number_input("Strike Price (K)", value=100.0, step=5.0, key="call_strike")
        premium_call = st.number_input("Option Premium", value=5.0, step=0.5, key="call_premium")
        
        st.markdown("#### At Expiration")
        stock_price_call = st.slider("Stock Price at Expiration", 50.0, 150.0, 100.0, 1.0, key="call_stock")
        
        # Calculate
        intrinsic = max(stock_price_call - strike_call, 0)
        profit = intrinsic - premium_call
        roi = (profit / premium_call) * 100 if premium_call > 0 else 0
        
        # Status
        if stock_price_call > strike_call:
            status = "In the Money"
            status_color = "#97BC62"
        elif stock_price_call == strike_call:
            status = "At the Money"
            status_color = "#F9E795"
        else:
            status = "Out of the Money"
            status_color = "#F96167"
        
        st.markdown(f"""
        <div class="concept-box" style="background-color: {status_color};">
        <h4>Option Status</h4>
        <p><strong>{status}</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Results
        st.markdown("#### Results at Expiration")
        
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Intrinsic Value", f"${intrinsic:.2f}")
        col_b.metric("Profit/Loss", f"${profit:.2f}", 
                    delta=f"{roi:.1f}%" if profit != 0 else "0%")
        col_c.metric("ROI", f"{roi:.1f}%")
        
        # Payoff diagram
        stock_range = np.linspace(50, 150, 100)
        payoffs = [max(s - strike_call, 0) - premium_call for s in stock_range]
        intrinsics = [max(s - strike_call, 0) for s in stock_range]
        
        fig = go.Figure()
        
        # Profit line
        fig.add_trace(go.Scatter(
            x=stock_range, y=payoffs,
            mode='lines',
            name='Profit/Loss',
            line=dict(color='#028090', width=3)
        ))
        
        # Zero line
        fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.5)
        
        # Strike price line
        fig.add_vline(x=strike_call, line_dash="dot", line_color="red",
                     annotation_text=f"Strike: ${strike_call:.0f}")
        
        # Current stock price
        fig.add_trace(go.Scatter(
            x=[stock_price_call], y=[profit],
            mode='markers',
            name='Current Position',
            marker=dict(size=15, color='red', symbol='star')
        ))
        
        fig.update_layout(
            title="Long Call Payoff Diagram",
            xaxis_title="Stock Price at Expiration ($)",
            yaxis_title="Profit/Loss ($)",
            height=500,
            hovermode='x'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Key Characteristics
    st.markdown("### 🎯 Call Option Characteristics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="call-box">
        <h4>✅ Advantages</h4>
        <ul>
        <li><strong>Limited Risk:</strong> Maximum loss = Premium</li>
        <li><strong>Unlimited Upside:</strong> Profit as stock rises</li>
        <li><strong>Leverage:</strong> Control $100 stock with $5 option</li>
        <li><strong>Lower Capital:</strong> Cheaper than buying stock</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="concept-box">
        <h4>⚠️ Risks</h4>
        <ul>
        <li><strong>Time Decay:</strong> Value decreases as expiration approaches</li>
        <li><strong>Total Loss Possible:</strong> Lose 100% of premium</li>
        <li><strong>Must Be Right:</strong> Stock must rise above strike + premium</li>
        <li><strong>Break-even:</strong> Sᴛ must exceed K + Premium</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="formula-box">
    <strong>Break-even Price = Strike + Premium</strong><br>
    Break-even = ${strike_call:.2f} + ${premium_call:.2f} = ${strike_call + premium_call:.2f}
    </div>
    """, unsafe_allow_html=True)

def show_put_options():
    st.markdown('<div class="section-header">📉 Put Options</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### What is a Put Option?
    
    A **put option** gives the holder the **right to SELL** an asset at a specified **strike price** on or before expiration.
    """)
    
    st.markdown("""
    <div class="formula-box">
    <strong>Put Option Payoff at Expiration:</strong><br><br>
    Payoff = max(K - Sᴛ, 0)<br>
    Profit = Payoff - Premium<br><br>
    Where:<br>
    K = Strike price<br>
    Sᴛ = Stock price at expiration
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive Put Option
    st.markdown("### 📊 Interactive Put Option Analysis")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Option Details")
        strike_put = st.number_input("Strike Price (K)", value=100.0, step=5.0, key="put_strike")
        premium_put = st.number_input("Option Premium", value=5.0, step=0.5, key="put_premium")
        
        st.markdown("#### At Expiration")
        stock_price_put = st.slider("Stock Price at Expiration", 50.0, 150.0, 100.0, 1.0, key="put_stock")
        
        # Calculate
        intrinsic_put = max(strike_put - stock_price_put, 0)
        profit_put = intrinsic_put - premium_put
        roi_put = (profit_put / premium_put) * 100 if premium_put > 0 else 0
        
        # Status
        if stock_price_put < strike_put:
            status = "In the Money"
            status_color = "#97BC62"
        elif stock_price_put == strike_put:
            status = "At the Money"
            status_color = "#F9E795"
        else:
            status = "Out of the Money"
            status_color = "#F96167"
        
        st.markdown(f"""
        <div class="concept-box" style="background-color: {status_color};">
        <h4>Option Status</h4>
        <p><strong>{status}</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Results
        st.markdown("#### Results at Expiration")
        
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Intrinsic Value", f"${intrinsic_put:.2f}")
        col_b.metric("Profit/Loss", f"${profit_put:.2f}", 
                    delta=f"{roi_put:.1f}%" if profit_put != 0 else "0%")
        col_c.metric("ROI", f"{roi_put:.1f}%")
        
        # Payoff diagram
        stock_range = np.linspace(50, 150, 100)
        payoffs_put = [max(strike_put - s, 0) - premium_put for s in stock_range]
        
        fig = go.Figure()
        
        # Profit line
        fig.add_trace(go.Scatter(
            x=stock_range, y=payoffs_put,
            mode='lines',
            name='Profit/Loss',
            line=dict(color='#F96167', width=3)
        ))
        
        # Zero line
        fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.5)
        
        # Strike price line
        fig.add_vline(x=strike_put, line_dash="dot", line_color="red",
                     annotation_text=f"Strike: ${strike_put:.0f}")
        
        # Current stock price
        fig.add_trace(go.Scatter(
            x=[stock_price_put], y=[profit_put],
            mode='markers',
            name='Current Position',
            marker=dict(size=15, color='red', symbol='star')
        ))
        
        fig.update_layout(
            title="Long Put Payoff Diagram",
            xaxis_title="Stock Price at Expiration ($)",
            yaxis_title="Profit/Loss ($)",
            height=500,
            hovermode='x'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Key Characteristics
    st.markdown("### 🎯 Put Option Characteristics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="put-box">
        <h4>✅ Advantages</h4>
        <ul>
        <li><strong>Limited Risk:</strong> Maximum loss = Premium</li>
        <li><strong>High Upside:</strong> Profit as stock falls</li>
        <li><strong>Portfolio Insurance:</strong> Protect against declines</li>
        <li><strong>Bearish Play:</strong> Profit without short selling</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="concept-box">
        <h4>⚠️ Risks</h4>
        <ul>
        <li><strong>Time Decay:</strong> Value decreases over time</li>
        <li><strong>Limited Upside:</strong> Maximum profit = K - Premium</li>
        <li><strong>Must Be Right:</strong> Stock must fall below strike - premium</li>
        <li><strong>Premium Cost:</strong> Paying for insurance</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="formula-box">
    <strong>Break-even Price = Strike - Premium</strong><br>
    Break-even = ${strike_put:.2f} - ${premium_put:.2f} = ${strike_put - premium_put:.2f}
    </div>
    """, unsafe_allow_html=True)

def show_payoff_diagrams():
    st.markdown('<div class="section-header">🎨 Payoff Diagrams Comparison</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Understanding Payoff Diagrams
    
    Visualize how different option positions profit or lose at various stock prices.
    """)
    
    # Common parameters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        strike_common = st.number_input("Strike Price", value=100.0, step=5.0, key="pd_strike")
    
    with col2:
        premium_common = st.number_input("Premium", value=5.0, step=0.5, key="pd_premium")
    
    with col3:
        stock_min = strike_common - 50
        stock_max = strike_common + 50
    
    stock_range = np.linspace(stock_min, stock_max, 200)
    
    # Calculate all four basic positions
    long_call = [max(s - strike_common, 0) - premium_common for s in stock_range]
    short_call = [-max(s - strike_common, 0) + premium_common for s in stock_range]
    long_put = [max(strike_common - s, 0) - premium_common for s in stock_range]
    short_put = [-max(strike_common - s, 0) + premium_common for s in stock_range]
    
    # Create figure with 4 subplots
    from plotly.subplots import make_subplots
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Long Call', 'Short Call', 'Long Put', 'Short Put')
    )
    
    # Long Call
    fig.add_trace(
        go.Scatter(x=stock_range, y=long_call, name='Long Call',
                  line=dict(color='#97BC62', width=3)),
        row=1, col=1
    )
    fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.3, row=1, col=1)
    
    # Short Call
    fig.add_trace(
        go.Scatter(x=stock_range, y=short_call, name='Short Call',
                  line=dict(color='#F96167', width=3)),
        row=1, col=2
    )
    fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.3, row=1, col=2)
    
    # Long Put
    fig.add_trace(
        go.Scatter(x=stock_range, y=long_put, name='Long Put',
                  line=dict(color='#97BC62', width=3)),
        row=2, col=1
    )
    fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.3, row=2, col=1)
    
    # Short Put
    fig.add_trace(
        go.Scatter(x=stock_range, y=short_put, name='Short Put',
                  line=dict(color='#F96167', width=3)),
        row=2, col=2
    )
    fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.3, row=2, col=2)
    
    fig.update_xaxes(title_text="Stock Price", row=1, col=1)
    fig.update_xaxes(title_text="Stock Price", row=1, col=2)
    fig.update_xaxes(title_text="Stock Price", row=2, col=1)
    fig.update_xaxes(title_text="Stock Price", row=2, col=2)
    
    fig.update_yaxes(title_text="Profit/Loss", row=1, col=1)
    fig.update_yaxes(title_text="Profit/Loss", row=1, col=2)
    fig.update_yaxes(title_text="Profit/Loss", row=2, col=1)
    fig.update_yaxes(title_text="Profit/Loss", row=2, col=2)
    
    fig.update_layout(height=800, showlegend=False, title_text="Four Basic Option Positions")
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Summary table
    st.markdown("### 📋 Position Summary")
    
    summary = pd.DataFrame({
        'Position': ['Long Call', 'Short Call', 'Long Put', 'Short Put'],
        'Max Profit': ['Unlimited', f'${premium_common:.2f}', f'${strike_common - premium_common:.2f}', f'${premium_common:.2f}'],
        'Max Loss': [f'${premium_common:.2f}', 'Unlimited', f'${premium_common:.2f}', f'${strike_common - premium_common:.2f}'],
        'Break-even': [f'${strike_common + premium_common:.2f}', f'${strike_common + premium_common:.2f}',
                      f'${strike_common - premium_common:.2f}', f'${strike_common - premium_common:.2f}'],
        'View': ['Bullish', 'Bearish', 'Bearish', 'Bullish']
    })
    
    st.dataframe(summary, use_container_width=True, hide_index=True)

def show_option_strategies():
    st.markdown('<div class="section-header">🛡️ Option Strategies</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Common Option Strategies
    
    Combine options with stocks or other options to create specific risk-return profiles.
    """)
    
    strategy = st.selectbox(
        "Select Strategy",
        ["Protective Put", "Covered Call", "Straddle", "Bull Spread"],
        key="strategy_select"
    )
    
    if strategy == "Protective Put":
        show_protective_put()
    elif strategy == "Covered Call":
        show_covered_call()
    elif strategy == "Straddle":
        show_straddle()
    elif strategy == "Bull Spread":
        show_bull_spread()

def show_protective_put():
    st.markdown("### 🛡️ Protective Put")
    
    st.markdown("""
    <div class="concept-box">
    <h4>Strategy</h4>
    <p><strong>Position:</strong> Long Stock + Long Put</p>
    <p><strong>Purpose:</strong> Insurance against stock price decline</p>
    <p><strong>Also called:</strong> Portfolio insurance</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        stock_price_pp = st.number_input("Current Stock Price", value=100.0, step=5.0, key="pp_stock")
        strike_pp = st.number_input("Put Strike Price", value=95.0, step=5.0, key="pp_strike")
        premium_pp = st.number_input("Put Premium", value=3.0, step=0.5, key="pp_premium")
    
    with col2:
        stock_range_pp = np.linspace(stock_price_pp - 40, stock_price_pp + 40, 200)
        
        # Stock only
        stock_payoff = stock_range_pp - stock_price_pp
        
        # Protective put
        put_payoff_pp = [max(strike_pp - s, 0) - premium_pp for s in stock_range_pp]
        protective_put_payoff = stock_payoff + np.array(put_payoff_pp)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=stock_range_pp, y=stock_payoff,
            mode='lines',
            name='Stock Only',
            line=dict(color='gray', width=2, dash='dash')
        ))
        
        fig.add_trace(go.Scatter(
            x=stock_range_pp, y=protective_put_payoff,
            mode='lines',
            name='Protective Put',
            line=dict(color='#028090', width=3)
        ))
        
        fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.3)
        fig.add_vline(x=strike_pp, line_dash="dot", line_color="red",
                     annotation_text=f"Put Strike: ${strike_pp:.0f}")
        
        fig.update_layout(
            title="Protective Put vs Stock Only",
            xaxis_title="Stock Price at Expiration",
            yaxis_title="Profit/Loss",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    max_loss = stock_price_pp - strike_pp + premium_pp
    
    st.markdown(f"""
    <div class="concept-box">
    <h4>Strategy Analysis</h4>
    <p><strong>Maximum Loss:</strong> ${max_loss:.2f} (stock falls to strike)</p>
    <p><strong>Maximum Gain:</strong> Unlimited (as stock rises)</p>
    <p><strong>Cost of Insurance:</strong> ${premium_pp:.2f}</p>
    <p><strong>Protected Below:</strong> ${strike_pp:.2f}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("✅ **Use when:** You own stock but want downside protection")

def show_covered_call():
    st.markdown("### 📞 Covered Call")
    
    st.markdown("""
    <div class="concept-box">
    <h4>Strategy</h4>
    <p><strong>Position:</strong> Long Stock + Short Call</p>
    <p><strong>Purpose:</strong> Generate income from stock holdings</p>
    <p><strong>Trade-off:</strong> Cap upside for premium income</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        stock_price_cc = st.number_input("Current Stock Price", value=100.0, step=5.0, key="cc_stock")
        strike_cc = st.number_input("Call Strike Price", value=105.0, step=5.0, key="cc_strike")
        premium_cc = st.number_input("Call Premium Received", value=4.0, step=0.5, key="cc_premium")
    
    with col2:
        stock_range_cc = np.linspace(stock_price_cc - 40, stock_price_cc + 40, 200)
        
        # Stock only
        stock_payoff_cc = stock_range_cc - stock_price_cc
        
        # Covered call
        call_payoff_cc = [-max(s - strike_cc, 0) + premium_cc for s in stock_range_cc]
        covered_call_payoff = stock_payoff_cc + np.array(call_payoff_cc)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=stock_range_cc, y=stock_payoff_cc,
            mode='lines',
            name='Stock Only',
            line=dict(color='gray', width=2, dash='dash')
        ))
        
        fig.add_trace(go.Scatter(
            x=stock_range_cc, y=covered_call_payoff,
            mode='lines',
            name='Covered Call',
            line=dict(color='#97BC62', width=3)
        ))
        
        fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.3)
        fig.add_vline(x=strike_cc, line_dash="dot", line_color="red",
                     annotation_text=f"Call Strike: ${strike_cc:.0f}")
        
        fig.update_layout(
            title="Covered Call vs Stock Only",
            xaxis_title="Stock Price at Expiration",
            yaxis_title="Profit/Loss",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    max_profit = strike_cc - stock_price_cc + premium_cc
    
    st.markdown(f"""
    <div class="concept-box">
    <h4>Strategy Analysis</h4>
    <p><strong>Maximum Profit:</strong> ${max_profit:.2f} (if stock > strike)</p>
    <p><strong>Maximum Loss:</strong> ${stock_price_cc - premium_cc:.2f} (if stock goes to zero)</p>
    <p><strong>Income Generated:</strong> ${premium_cc:.2f}</p>
    <p><strong>Upside Capped at:</strong> ${strike_cc:.2f}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **Use when:** You own stock and don't expect large upward moves")

def show_straddle():
    st.markdown("### 🎯 Straddle")
    
    st.markdown("""
    <div class="concept-box">
    <h4>Strategy</h4>
    <p><strong>Position:</strong> Long Call + Long Put (same strike & expiration)</p>
    <p><strong>Purpose:</strong> Profit from large price moves in either direction</p>
    <p><strong>Bet:</strong> High volatility</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        strike_strad = st.number_input("Strike Price (both)", value=100.0, step=5.0, key="strad_strike")
        call_premium_strad = st.number_input("Call Premium", value=5.0, step=0.5, key="strad_call")
        put_premium_strad = st.number_input("Put Premium", value=5.0, step=0.5, key="strad_put")
        
        total_premium = call_premium_strad + put_premium_strad
    
    with col2:
        stock_range_strad = np.linspace(strike_strad - 50, strike_strad + 50, 200)
        
        # Straddle payoff
        call_payoff_strad = [max(s - strike_strad, 0) - call_premium_strad for s in stock_range_strad]
        put_payoff_strad = [max(strike_strad - s, 0) - put_premium_strad for s in stock_range_strad]
        straddle_payoff = np.array(call_payoff_strad) + np.array(put_payoff_strad)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=stock_range_strad, y=straddle_payoff,
            mode='lines',
            name='Straddle',
            line=dict(color='#1E2761', width=3),
            fill='tonexty'
        ))
        
        fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.5)
        fig.add_vline(x=strike_strad, line_dash="dot", line_color="red",
                     annotation_text=f"Strike: ${strike_strad:.0f}")
        
        # Break-even lines
        break_even_up = strike_strad + total_premium
        break_even_down = strike_strad - total_premium
        
        fig.add_vline(x=break_even_up, line_dash="dot", line_color="green",
                     annotation_text=f"BE: ${break_even_up:.0f}")
        fig.add_vline(x=break_even_down, line_dash="dot", line_color="green",
                     annotation_text=f"BE: ${break_even_down:.0f}")
        
        fig.update_layout(
            title="Long Straddle Payoff",
            xaxis_title="Stock Price at Expiration",
            yaxis_title="Profit/Loss",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(f"""
    <div class="concept-box">
    <h4>Strategy Analysis</h4>
    <p><strong>Maximum Loss:</strong> ${total_premium:.2f} (if stock = strike)</p>
    <p><strong>Maximum Profit:</strong> Unlimited</p>
    <p><strong>Upper Break-even:</strong> ${strike_strad + total_premium:.2f}</p>
    <p><strong>Lower Break-even:</strong> ${strike_strad - total_premium:.2f}</p>
    <p><strong>Need move of:</strong> ${total_premium:.2f} in either direction</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.warning("⚠️ **Use when:** You expect large price movement but uncertain of direction")

def show_bull_spread():
    st.markdown("### 📈 Bull Spread")
    
    st.markdown("""
    <div class="concept-box">
    <h4>Strategy</h4>
    <p><strong>Position:</strong> Buy Call (lower strike) + Sell Call (higher strike)</p>
    <p><strong>Purpose:</strong> Bullish bet with limited risk and reward</p>
    <p><strong>Reduces cost:</strong> Premium from short call offsets long call cost</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        strike_low = st.number_input("Lower Strike (buy)", value=100.0, step=5.0, key="bs_low")
        strike_high = st.number_input("Higher Strike (sell)", value=110.0, step=5.0, key="bs_high")
        premium_low = st.number_input("Premium Paid", value=6.0, step=0.5, key="bs_prem_low")
        premium_high = st.number_input("Premium Received", value=2.0, step=0.5, key="bs_prem_high")
        
        net_cost = premium_low - premium_high
    
    with col2:
        stock_range_bs = np.linspace(strike_low - 30, strike_high + 30, 200)
        
        # Bull spread payoff
        long_call_bs = [max(s - strike_low, 0) - premium_low for s in stock_range_bs]
        short_call_bs = [-max(s - strike_high, 0) + premium_high for s in stock_range_bs]
        bull_spread_payoff = np.array(long_call_bs) + np.array(short_call_bs)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=stock_range_bs, y=bull_spread_payoff,
            mode='lines',
            name='Bull Spread',
            line=dict(color='#97BC62', width=3),
            fill='tozeroy'
        ))
        
        fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.5)
        fig.add_vline(x=strike_low, line_dash="dot", line_color="blue",
                     annotation_text=f"Buy: ${strike_low:.0f}")
        fig.add_vline(x=strike_high, line_dash="dot", line_color="red",
                     annotation_text=f"Sell: ${strike_high:.0f}")
        
        fig.update_layout(
            title="Bull Call Spread Payoff",
            xaxis_title="Stock Price at Expiration",
            yaxis_title="Profit/Loss",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    max_profit = strike_high - strike_low - net_cost
    max_loss = net_cost
    break_even_bs = strike_low + net_cost
    
    st.markdown(f"""
    <div class="concept-box">
    <h4>Strategy Analysis</h4>
    <p><strong>Net Cost:</strong> ${net_cost:.2f}</p>
    <p><strong>Maximum Profit:</strong> ${max_profit:.2f} (if stock > ${strike_high:.0f})</p>
    <p><strong>Maximum Loss:</strong> ${max_loss:.2f} (if stock < ${strike_low:.0f})</p>
    <p><strong>Break-even:</strong> ${break_even_bs:.2f}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **Use when:** Moderately bullish, want to reduce cost of long call")

def show_strategy_builder():
    st.markdown('<div class="section-header">🔧 Custom Strategy Builder</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Build Your Own Option Strategy
    
    Combine multiple options to create custom payoff profiles.
    """)
    
    # Number of legs
    num_legs = st.number_input("Number of Positions", 1, 4, 2, key="builder_legs")
    
    st.markdown("---")
    
    positions = []
    
    for i in range(num_legs):
        st.markdown(f"#### Position {i+1}")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            option_type = st.selectbox(f"Type", ["Call", "Put"], key=f"type_{i}")
        
        with col2:
            position_type = st.selectbox(f"Position", ["Long", "Short"], key=f"pos_{i}")
        
        with col3:
            strike = st.number_input(f"Strike", value=100.0 + i*5, step=5.0, key=f"strike_{i}")
        
        with col4:
            premium = st.number_input(f"Premium", value=5.0, step=0.5, key=f"prem_{i}")
        
        positions.append({
            'type': option_type,
            'position': position_type,
            'strike': strike,
            'premium': premium
        })
    
    # Calculate combined payoff
    stock_range = np.linspace(50, 150, 200)
    total_payoff = np.zeros(len(stock_range))
    
    for pos in positions:
        if pos['type'] == 'Call':
            if pos['position'] == 'Long':
                payoff = np.array([max(s - pos['strike'], 0) - pos['premium'] for s in stock_range])
            else:
                payoff = np.array([-max(s - pos['strike'], 0) + pos['premium'] for s in stock_range])
        else:  # Put
            if pos['position'] == 'Long':
                payoff = np.array([max(pos['strike'] - s, 0) - pos['premium'] for s in stock_range])
            else:
                payoff = np.array([-max(pos['strike'] - s, 0) + pos['premium'] for s in stock_range])
        
        total_payoff += payoff
    
    # Plot
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=stock_range, y=total_payoff,
        mode='lines',
        name='Combined Strategy',
        line=dict(color='#1E2761', width=4),
        fill='tozeroy'
    ))
    
    fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.5)
    
    # Add strike lines
    for i, pos in enumerate(positions):
        color = '#97BC62' if pos['type'] == 'Call' else '#F96167'
        fig.add_vline(x=pos['strike'], line_dash="dot", line_color=color,
                     annotation_text=f"{pos['position']} {pos['type']}: ${pos['strike']:.0f}")
    
    fig.update_layout(
        title="Custom Strategy Payoff Diagram",
        xaxis_title="Stock Price at Expiration",
        yaxis_title="Profit/Loss",
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Analysis
    max_profit = np.max(total_payoff)
    max_loss = np.min(total_payoff)
    
    # Find break-evens (where payoff crosses zero)
    break_evens = []
    for i in range(len(total_payoff)-1):
        if total_payoff[i] * total_payoff[i+1] < 0:  # Sign change
            break_evens.append(stock_range[i])
    
    st.markdown(f"""
    <div class="concept-box">
    <h4>Strategy Analysis</h4>
    <p><strong>Maximum Profit:</strong> ${max_profit:.2f}</p>
    <p><strong>Maximum Loss:</strong> ${max_loss:.2f}</p>
    <p><strong>Risk/Reward Ratio:</strong> {abs(max_loss/max_profit):.2f} if max_profit > 0 else 'N/A'</p>
    <p><strong>Break-even Points:</strong> {', '.join([f'${be:.2f}' for be in break_evens]) if break_evens else 'None found'}</p>
    </div>
    """, unsafe_allow_html=True)

def show_advanced_strategies():
    st.markdown('<div class="section-header">💼 Advanced Option Concepts</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Beyond Basic Options
    """)
    
    tab1, tab2, tab3 = st.tabs(["Option-like Securities", "Convertibles", "Exotic Options"])
    
    with tab1:
        st.markdown("### 📜 Option-like Securities")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="concept-box">
            <h4>Callable Bonds</h4>
            <p><strong>Structure:</strong> Bond + Short Call</p>
            <p>Issuer has right to call (buy back) bond</p>
            <ul>
            <li>Bondholders receive higher coupon</li>
            <li>Compensation for call risk</li>
            <li>Usually has call protection period</li>
            </ul>
            <p><strong>Value:</strong> Straight Bond - Call Option</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="concept-box">
            <h4>Warrants</h4>
            <p><strong>Definition:</strong> Long-term call option issued by company</p>
            <p>Key differences from regular calls:</p>
            <ul>
            <li>Longer maturity (years)</li>
            <li>Issued by the company</li>
            <li>Dilutive when exercised</li>
            <li>Often attached to bonds</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 🔄 Convertible Securities")
        
        st.markdown("""
        <div class="concept-box">
        <h4>Convertible Bonds</h4>
        <p><strong>Structure:</strong> Bond + Long Call on Stock</p>
        <p>Bondholder has right to convert to stock</p>
        <p><strong>Value = Straight Bond Value + Call Option Value</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Convertible bond visualization
        col1, col2 = st.columns(2)
        
        with col1:
            conversion_ratio = st.number_input("Conversion Ratio", value=20.0, step=1.0, key="conv_ratio")
            bond_floor = st.number_input("Bond Floor Value", value=1000.0, step=50.0, key="conv_floor")
        
        with col2:
            stock_prices = np.linspace(0, 100, 100)
            conversion_value = stock_prices * conversion_ratio
            convertible_value = np.maximum(conversion_value, bond_floor)
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=stock_prices, y=conversion_value,
                mode='lines',
                name='Conversion Value',
                line=dict(color='#028090', width=2, dash='dash')
            ))
            
            fig.add_trace(go.Scatter(
                x=stock_prices, y=convertible_value,
                mode='lines',
                name='Convertible Value',
                line=dict(color='#1E2761', width=3)
            ))
            
            fig.add_hline(y=bond_floor, line_dash="dot", line_color="red",
                         annotation_text=f"Bond Floor: ${bond_floor:.0f}")
            
            fig.update_layout(
                title="Convertible Bond Value",
                xaxis_title="Stock Price",
                yaxis_title="Bond Value",
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("### 🌟 Exotic Options")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="concept-box">
            <h4>Asian Options</h4>
            <p>Payoff based on <strong>average</strong> price</p>
            <p><strong>Example:</strong> Average over last 30 days</p>
            <p><strong>Benefit:</strong> Reduces manipulation risk</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="concept-box">
            <h4>Barrier Options</h4>
            <p>Activate/deactivate at certain price levels</p>
            <p><strong>Knock-in:</strong> Activates if barrier hit</p>
            <p><strong>Knock-out:</strong> Terminates if barrier hit</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="concept-box">
            <h4>Digital (Binary) Options</h4>
            <p>Fixed payoff if condition met</p>
            <p><strong>Example:</strong> Pay $100 if stock > $50</p>
            <p><strong>All or nothing</strong> payoff</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="concept-box">
            <h4>Lookback Options</h4>
            <p>Payoff based on max/min price during life</p>
            <p><strong>Call:</strong> Pay minimum, receive current</p>
            <p><strong>Put:</strong> Pay current, receive maximum</p>
            </div>
            """, unsafe_allow_html=True)

def show_quiz():
    st.markdown('<div class="section-header">✅ Test Your Knowledge</div>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'ch15_score' not in st.session_state:
        st.session_state.ch15_score = 0
    if 'ch15_submitted' not in st.session_state:
        st.session_state.ch15_submitted = set()
    
    # Question 1
    st.markdown("### Question 1: Call Option Basics")
    st.markdown("A call option gives the holder the right to:")
    
    q1 = st.radio("",
                 ["A) Sell an asset at the strike price", "B) Buy an asset at the strike price",
                  "C) Receive dividends", "D) Vote in shareholder meetings"],
                 key="q1", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q1_btn") and "q1" not in st.session_state.ch15_submitted:
        st.session_state.ch15_submitted.add("q1")
        if q1 == "B) Buy an asset at the strike price":
            st.success("✅ Correct! A call option gives the right to BUY.")
            st.session_state.ch15_score += 1
        else:
            st.error("❌ Incorrect. Call = right to BUY, Put = right to SELL.")
    
    st.markdown("---")
    
    # Question 2
    st.markdown("### Question 2: Option Payoffs")
    st.markdown("For a long call with strike $50 and premium $5, if the stock is at $60 at expiration, the profit is:")
    
    q2 = st.radio("",
                 ["A) $10", "B) $5", "C) $15", "D) -$5"],
                 key="q2", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q2_btn") and "q2" not in st.session_state.ch15_submitted:
        st.session_state.ch15_submitted.add("q2")
        if q2 == "B) $5":
            st.success("✅ Correct! Profit = (60-50) - 5 = $5")
            st.session_state.ch15_score += 1
        else:
            st.error("❌ Incorrect. Profit = max(S-K, 0) - Premium = (60-50) - 5 = $5")
    
    st.markdown("---")
    
    # Question 3
    st.markdown("### Question 3: Protective Put")
    st.markdown("A protective put strategy consists of:")
    
    q3 = st.radio("",
                 ["A) Long stock + Long put", "B) Long stock + Short call",
                  "C) Short stock + Long call", "D) Long call + Long put"],
                 key="q3", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q3_btn") and "q3" not in st.session_state.ch15_submitted:
        st.session_state.ch15_submitted.add("q3")
        if q3 == "A) Long stock + Long put":
            st.success("✅ Correct! Protective put = Stock + Put for downside protection.")
            st.session_state.ch15_score += 1
        else:
            st.error("❌ Incorrect. Protective put = Long stock + Long put.")
    
    st.markdown("---")
    
    # Question 4
    st.markdown("### Question 4: Covered Call")
    st.markdown("The maximum profit on a covered call is:")
    
    q4 = st.radio("",
                 ["A) Unlimited", "B) Strike price - Stock price + Premium",
                  "C) Premium received", "D) Stock price - Strike price"],
                 key="q4", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q4_btn") and "q4" not in st.session_state.ch15_submitted:
        st.session_state.ch15_submitted.add("q4")
        if q4 == "B) Strike price - Stock price + Premium":
            st.success("✅ Correct! Max profit = (K - S₀) + Premium when S ≥ K")
            st.session_state.ch15_score += 1
        else:
            st.error("❌ Incorrect. Max profit = (Strike - Purchase Price) + Premium")
    
    st.markdown("---")
    
    # Question 5
    st.markdown("### Question 5: Straddle")
    st.markdown("A straddle profits when:")
    
    q5 = st.radio("",
                 ["A) Stock price stays stable", "B) Stock price moves significantly in either direction",
                  "C) Stock price increases", "D) Stock price decreases"],
                 key="q5", label_visibility="collapsed")
    
    if st.button("Submit Answer", key="q5_btn") and "q5" not in st.session_state.ch15_submitted:
        st.session_state.ch15_submitted.add("q5")
        if q5 == "B) Stock price moves significantly in either direction":
            st.success("✅ Correct! Straddles profit from large moves regardless of direction.")
            st.session_state.ch15_score += 1
        else:
            st.error("❌ Incorrect. Straddles = Long call + Long put, profits from volatility.")
    
    st.markdown("---")
    
    # Score Display
    if len(st.session_state.ch15_submitted) > 0:
        score_pct = (st.session_state.ch15_score / len(st.session_state.ch15_submitted)) * 100
        
        st.markdown(f"""
        <div class="concept-box">
        <h2>Your Score: {st.session_state.ch15_score} / {len(st.session_state.ch15_submitted)}</h2>
        <h3>{score_pct:.0f}%</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if score_pct >= 80:
            st.success("🎉 Excellent! You understand options markets very well.")
        elif score_pct >= 60:
            st.info("👍 Good work! Review payoff diagrams and strategies.")
        else:
            st.warning("📚 Keep studying! Review call/put basics and option strategies.")
    
    if st.button("Reset Quiz", key="reset_quiz"):
        st.session_state.ch15_score = 0
        st.session_state.ch15_submitted = set()
        st.rerun()

if __name__ == "__main__":
    main()
