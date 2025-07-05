from accounts import Account
import gradio as gr

# Create an instance of the Account for demonstration
account = Account(username="DemoUser", initial_deposit=1000.0)

def deposit_funds(amount):
    account.deposit(amount)
    return f"Deposited: {amount}, New Balance: {account.balance}"

def withdraw_funds(amount):
    try:
        account.withdraw(amount)
        return f"Withdrew: {amount}, New Balance: {account.balance}"
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        account.buy_shares(symbol, quantity)
        return f"Bought: {quantity} shares of {symbol}, New Holdings: {account.report_holdings()}"
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        account.sell_shares(symbol, quantity)
        return f"Sold: {quantity} shares of {symbol}, New Holdings: {account.report_holdings()}"
    except ValueError as e:
        return str(e)

def report_holdings():
    return account.report_holdings()

def report_profit_loss():
    return account.report_profit_loss()

def list_transactions():
    return account.list_transactions()

# Create Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Account Management System for Trading Simulation")
    
    with gr.Group():
        gr.Markdown("## Deposit Funds")
        deposit_amount = gr.Number(label="Deposit Amount")
        deposit_button = gr.Button("Deposit")
        deposit_output = gr.Textbox(label="Output")
        deposit_button.click(deposit_funds, inputs=deposit_amount, outputs=deposit_output)

    with gr.Group():
        gr.Markdown("## Withdraw Funds")
        withdraw_amount = gr.Number(label="Withdraw Amount")
        withdraw_button = gr.Button("Withdraw")
        withdraw_output = gr.Textbox(label="Output")
        withdraw_button.click(withdraw_funds, inputs=withdraw_amount, outputs=withdraw_output)

    with gr.Group():
        gr.Markdown("## Buy Shares")
        buy_symbol = gr.Textbox(label="Stock Symbol (e.g., AAPL)")
        buy_quantity = gr.Number(label="Quantity")
        buy_button = gr.Button("Buy Shares")
        buy_output = gr.Textbox(label="Output")
        buy_button.click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs=buy_output)

    with gr.Group():
        gr.Markdown("## Sell Shares")
        sell_symbol = gr.Textbox(label="Stock Symbol (e.g., AAPL)")
        sell_quantity = gr.Number(label="Quantity")
        sell_button = gr.Button("Sell Shares")
        sell_output = gr.Textbox(label="Output")
        sell_button.click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs=sell_output)

    with gr.Group():
        gr.Markdown("## Report Holdings")
        holdings_button = gr.Button("Report Holdings")
        holdings_output = gr.Textbox(label="Holdings")
        holdings_button.click(report_holdings, outputs=holdings_output)

    with gr.Group():
        gr.Markdown("## Report Profit/Loss")
        profit_loss_button = gr.Button("Report Profit/Loss")
        profit_loss_output = gr.Textbox(label="Profit/Loss")
        profit_loss_button.click(report_profit_loss, outputs=profit_loss_output)

    with gr.Group():
        gr.Markdown("## List Transactions")
        transactions_button = gr.Button("List Transactions")
        transactions_output = gr.Textbox(label="Transactions", lines=4)
        transactions_button.click(list_transactions, outputs=transactions_output)

demo.launch()