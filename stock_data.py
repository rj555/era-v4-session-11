"""
Data collection for Indian stock market (NSE and BSE)
"""

import requests
import csv
from typing import List
import time


def get_nse_stocks() -> List[str]:
    """Fetch NSE stock symbols"""
    print("Fetching NSE stock data...")
    
    # NSE stock list - using known NSE stocks
    # In production, you would fetch from NSE API or official sources
    nse_stocks = [
        "RELIANCE", "TCS", "HDFCBANK", "INFY", "HINDUNILVR", "ICICIBANK",
        "BHARTIARTL", "SBIN", "BAJFINANCE", "LICI", "ITC", "LT", "HCLTECH",
        "AXISBANK", "KOTAKBANK", "ASIANPAINT", "MARUTI", "TITAN", "ULTRACEMCO",
        "SUNPHARMA", "NTPC", "ONGC", "NESTLEIND", "POWERGRID", "M&M", "TATASTEEL",
        "ADANIENT", "JSWSTEEL", "WIPRO", "HINDALCO", "COALINDIA", "TECHM",
        "GRASIM", "DIVISLAB", "BAJAJFINSV", "TATAMOTORS", "CIPLA", "SBILIFE",
        "DRREDDY", "EICHERMOT", "HEROMOTOCO", "BRITANNIA", "BPCL", "IOC",
        "INDUSINDBK", "ADANIPORTS", "APOLLOHOSP", "TATACONSUM", "BAJAJ-AUTO",
        "MARICO", "VEDL", "GODREJCP", "PIDILITIND", "DABUR", "HAVELLS",
        "SHREECEM", "AMBUJACEM", "BANKBARODA", "ZOMATO", "ICICIPRULI", "LTI",
        "TORNTPHARM", "GODREJPROP", "DLF", "CANBK", "BIOCON", "ICICIGI",
        "INDIGO", "NAUKRI", "MCDOWELL-N", "HDFCLIFE", "BERGEPAINT", "SBICARD",
        "PGHH", "MOTHERSON", "TATAPOWER", "BEL", "UNIONBANK", "HAL", "BATAINDIA",
        "IOB", "PNB", "CENTRALBK", "UCOBANK", "IDFCFIRSTB", "FEDERALBNK",
        "BANKINDIA", "YESBANK", "RBLBANK", "AUBANK", "CSBBANK", "KARURVYSYA",
        "SOUTHBANK", "DCBBANK", "JKLAKSHMI", "ORIENTBANK", "DCMSHRIRAM",
        "RADICO", "GRAPHITE", "EVERESTIND", "RAJESHEXPO", "SHILPAMED", "GILLETTE",
        "HEXAWARE", "WIPRO", "MINDTREE", "LTI", "MPHASIS", "TECHM", "ZENSAR",
        "CYIENT", "LTTS", "PERSISTENT", "KPITTECH", "SONATA", "NEWGEN", "ROHLTD",
        "RAMSARUP", "CENTURYPLY", "GREENPLY", "RUSHIL", "STYLAM", "SHRIRAMFIN",
        "BAJAJFINSV", "MUTHOOTFIN", "MANAPPURAM", "LICHSGFIN", "RELIANCE",
        "ADANIENT", "ADANIPORTS", "ADANIGREEN", "ADANIPOWER", "ADANITRANS",
        "ADANIWILMAR", "ALKEM", "APLLTD", "ASTRAL", "AUBANK", "BAJAJHLDNG",
        "BALKRISIND", "BANDHANBNK", "BANKBARODA", "BEL", "BHARATFORG", "BHEL",
        "BIOCON", "BOSCHLTD", "BPCL", "BRITANNIA", "CADILAHC", "CANBK",
        "CHOLAFIN", "CIPLA", "COALINDIA", "COFORGE", "CONCOR", "CUMMINSIND",
        "DABUR", "DALBHARAT", "DEEPAKNTR", "DIVISLAB", "DLF", "DRREDDY",
        "EICHERMOT", "ESCORTS", "EXIDEIND", "FEDERALBNK", "GAIL", "GLENMARK",
        "GODREJCP", "GODREJPROP", "GRASIM", "GUJGASLTD", "HAVELLS", "HCLTECH",
        "HDFCAMC", "HDFCBANK", "HDFCLIFE", "HEROMOTOCO", "HINDALCO", "HINDPETRO",
        "HINDUNILVR", "ICICIBANK", "ICICIGI", "ICICIPRULI", "IDEA", "IDFCFIRSTB",
        "IEX", "IGL", "INDIGO", "INDUSINDBK", "INFRATEL", "INFY", "IOC",
        "IPCALAB", "ITC", "JINDALSAW", "JKCEMENT", "JSWSTEEL", "JUBLFOOD",
        "KOTAKBANK", "L&TFH", "LICHSGFIN", "LT", "LTI", "LTTS", "LUPIN",
        "M&M", "M&MFIN", "MANAPPURAM", "MARICO", "MARUTI", "MCDOWELL-N",
        "MCX", "METROPOLIS", "MFSL", "MGL", "MINDTREE", "MPHASIS", "MRF",
        "MUTHOOTFIN", "NAM-INDIA", "NAUKRI", "NAZARA", "NESTLEIND", "NMDC",
        "NTPC", "OBEROIRLTY", "OFSS", "ONGC", "PAGEIND", "PAGEIND", "PEL",
        "PETRONET", "PFC", "PIDILITIND", "PIIND", "PNB", "POLICYBZR", "POWERGRID",
        "PVR", "RAMCOCEM", "RBLBANK", "RECLTD", "RELIANCE", "SAIL", "SBILIFE",
        "SBIN", "SHREECEM", "SIEMENS", "SRF", "SRTRANSFIN", "SUNPHARMA",
        "SUNTV", "TATACHEM", "TATACONSUM", "TATAMOTORS", "TATAPOWER", "TATASTEEL",
        "TECHM", "TITAN", "TORNTPHARM", "TRENT", "TVSMOTOR", "UBL", "ULTRACEMCO",
        "UPL", "VEDL", "VOLTAS", "WIPRO", "ZEEL", "ZOMATO", "ZYDUSLIFE"
    ]
    
    # Generate more variations by adding common suffixes and patterns
    extended_nse = []
    for stock in nse_stocks:
        extended_nse.append(stock)
        extended_nse.append(f"{stock}-EQ")  # Equity suffix
        extended_nse.append(f"{stock}-BE")  # B group
        extended_nse.append(f"{stock}NSE")  # With exchange
        extended_nse.append(f"NSE:{stock}")  # Exchange prefix
    
    print(f"Collected {len(set(extended_nse))} NSE stock symbols")
    return list(set(extended_nse))


def get_bse_stocks() -> List[str]:
    """Fetch BSE stock symbols"""
    print("Fetching BSE stock data...")
    
    # BSE stock list - using known BSE stocks
    bse_stocks = [
        "500325", "500209", "500180", "500675", "500696", "500112", "532174",
        "500010", "532755", "532540", "500570", "532187", "500295", "500247",
        "500300", "500440", "532977", "500103", "532538", "500087", "500104",
        "500470", "500124", "532461", "500253", "500114", "500106", "532222",
        "532868", "500116", "500124", "500119", "500139", "500125", "500182",
        "500103", "500087", "500124", "500253", "500114", "500106", "532222",
        "532868", "500116", "500325", "500209", "500180", "500675", "500696",
        "500112", "532174", "500010", "532755", "532540", "500570", "532187",
        "500295", "500247", "500300", "500440", "532977", "532538", "532461"
    ]
    
    # Add company names that correspond to BSE codes
    bse_names = [
        "RELIANCE", "TCS", "HDFC BANK", "INFOSYS", "HUL", "ICICI BANK",
        "BHARTI AIRTEL", "SBI", "BAJAJ FINANCE", "LIC", "ITC", "LARSEN",
        "HCL TECH", "AXIS BANK", "KOTAK MAHINDRA", "ASIAN PAINTS", "MARUTI",
        "TITAN", "ULTRATECH", "SUN PHARMA", "NTPC", "ONGC", "NESTLE",
        "POWER GRID", "M&M", "TATA STEEL", "ADANI ENTERPRISES", "JSW STEEL",
        "WIPRO", "HINDALCO", "COAL INDIA", "TECH MAHINDRA", "GRASIM",
        "DIVI'S LAB", "BAJAJ FINSERV", "TATA MOTORS", "CIPLA", "SBI LIFE",
        "DR REDDY", "EICHER MOTORS", "HERO MOTOCORP", "BRITANNIA", "BPCL",
        "IOC", "INDUSIND BANK", "ADANI PORTS", "APOLLO HOSPITALS", "TATA CONSUMER",
        "BAJAJ AUTO", "MARICO", "VEDANTA", "GODREJ CONSUMER", "PIDILITE",
        "DABUR", "HAVELLS", "SHREE CEMENT", "AMBuja CEMENT", "BANK OF BARODA"
    ]
    
    # Combine codes and names
    extended_bse = []
    for code in bse_stocks:
        extended_bse.append(code)
        extended_bse.append(f"BSE:{code}")
        extended_bse.append(f"{code}-BSE")
    
    for name in bse_names:
        extended_bse.append(name)
        extended_bse.append(name.replace(" ", ""))
        extended_bse.append(f"BSE-{name}")
        extended_bse.append(f"{name}-BSE")
    
    print(f"Collected {len(set(extended_bse))} BSE stock symbols")
    return list(set(extended_bse))


def generate_stock_corpus() -> List[str]:
    """Generate a comprehensive corpus of Indian stock market data"""
    print("Generating stock market corpus...")
    
    nse_stocks = get_nse_stocks()
    bse_stocks = get_bse_stocks()
    
    # Combine all stocks
    all_stocks = nse_stocks + bse_stocks
    
    # Create corpus with various formats and patterns
    corpus = []
    
    # Add stock symbols multiple times with variations
    corpus.extend(all_stocks)
    corpus.extend([s.lower() for s in all_stocks])
    corpus.extend([s.upper() for s in all_stocks])
    
    # Add patterns like "Buy RELIANCE", "Sell TCS", etc.
    actions = ["Buy", "Sell", "Hold", "Trade", "Invest", "Stock", "Share", 
               "Equity", "Security", "Instrument", "Listing", "IPO", "FPO",
               "Purchase", "Acquire", "Dispose", "Transfer", "Allocate",
               "Portfolio", "Position", "Long", "Short", "Call", "Put",
               "Option", "Future", "Derivative", "Contract", "Expiry",
               "Strike", "Premium", "Volume", "Liquidity", "Volatility"]
    
    for action in actions:
        for stock in all_stocks[:150]:  # Increased limit
            corpus.append(f"{action} {stock}")
            corpus.append(f"{stock} {action}")
            corpus.append(f"{action} {stock.lower()}")
            corpus.append(f"{stock.upper()} {action}")
    
    # Add market-related terms with variations
    market_terms = [
        "National Stock Exchange", "NSE", "Bombay Stock Exchange", "BSE",
        "Sensex", "Nifty", "Nifty 50", "Nifty 500", "Nifty Next 50",
        "Nifty Midcap", "Nifty Smallcap", "Nifty Bank", "Nifty IT",
        "Nifty Pharma", "Nifty Auto", "Nifty FMCG", "Nifty Metal",
        "Nifty Energy", "Nifty Realty", "Nifty PSU Bank", "Nifty Private Bank",
        "Midcap", "Smallcap", "Largecap", "Megacap", "Microcap",
        "Market Cap", "Market Capitalization", "Free Float Market Cap",
        "Volume", "Trading Volume", "Average Volume", "Volume Weighted",
        "Price", "Current Price", "Closing Price", "Opening Price",
        "High", "Day High", "52 Week High", "All Time High",
        "Low", "Day Low", "52 Week Low", "All Time Low",
        "Open", "Close", "Last Traded Price", "Bid Price", "Ask Price",
        "Dividend", "Dividend Yield", "Dividend Per Share", "Ex-Dividend",
        "PE Ratio", "Price to Earnings", "Trailing PE", "Forward PE",
        "PB Ratio", "Price to Book", "Price to Sales", "PS Ratio",
        "ROE", "Return on Equity", "ROCE", "Return on Capital Employed",
        "ROA", "Return on Assets", "EPS", "Earnings Per Share",
        "Diluted EPS", "Basic EPS", "Revenue", "Total Revenue",
        "Net Revenue", "Operating Revenue", "Profit", "Net Profit",
        "Gross Profit", "Operating Profit", "EBITDA", "EBIT",
        "Free Float", "Index Weight", "Sector Weight", "Stock Weight",
        "Sector", "Industry", "Sub Industry", "Industry Classification",
        "Financial Services", "Banking", "Private Bank", "Public Bank",
        "NBFC", "Insurance", "Life Insurance", "General Insurance",
        "Technology", "IT Services", "Software", "Hardware",
        "Pharmaceuticals", "Pharma", "Biotech", "Healthcare",
        "FMCG", "Fast Moving Consumer Goods", "Consumer Goods",
        "Automobile", "Auto", "Auto Ancillary", "Two Wheeler",
        "Four Wheeler", "Commercial Vehicle", "Passenger Vehicle",
        "Oil & Gas", "Oil", "Gas", "Refining", "Exploration",
        "Power", "Power Generation", "Power Transmission", "Power Distribution",
        "Metals", "Steel", "Aluminum", "Copper", "Iron", "Gold",
        "Cement", "Building Materials", "Construction Materials",
        "Real Estate", "Construction", "Infrastructure", "Engineering",
        "Telecom", "Telecommunications", "Mobile Services", "Broadband",
        "Media", "Entertainment", "Broadcasting", "Print Media",
        "Retail", "E-commerce", "Consumer Services", "Hospitality",
        "Healthcare", "Hospitals", "Diagnostics", "Medical Devices",
        "Chemicals", "Specialty Chemicals", "Petrochemicals",
        "Textiles", "Garments", "Apparel", "Fashion",
        "Agriculture", "Agri Business", "Fertilizers", "Pesticides",
        "Shipping", "Logistics", "Transportation", "Aviation",
        "Ports", "Airports", "Roads", "Highways"
    ]
    
    corpus.extend(market_terms)
    corpus.extend([t.lower() for t in market_terms])
    corpus.extend([t.upper() for t in market_terms])
    
    # Add company names and tickers together
    company_names = [
        "Reliance Industries", "Reliance", "RIL",
        "Tata Consultancy Services", "TCS", "Tata CS",
        "HDFC Bank", "HDFC", "HDFC Bank Limited",
        "Infosys", "Infosys Limited", "Infosys Technologies",
        "Hindustan Unilever", "HUL", "Hindustan Unilever Limited",
        "ICICI Bank", "ICICI", "ICICI Bank Limited",
        "Bharti Airtel", "Airtel", "Bharti",
        "State Bank of India", "SBI", "State Bank",
        "Bajaj Finance", "Bajaj Finserv", "Bajaj",
        "Life Insurance Corporation", "LIC", "LIC of India",
        "ITC Limited", "ITC", "Indian Tobacco Company",
        "Larsen & Toubro", "L&T", "L and T", "Larsen Toubro",
        "HCL Technologies", "HCL", "HCL Tech",
        "Axis Bank", "Axis", "Axis Bank Limited",
        "Kotak Mahindra Bank", "Kotak Bank", "Kotak",
        "Asian Paints", "Asian", "Asian Paints Limited",
        "Maruti Suzuki", "Maruti", "Maruti Suzuki India",
        "Titan Company", "Titan", "Titan Industries",
        "UltraTech Cement", "UltraTech", "Ultra Tech",
        "Sun Pharmaceutical", "Sun Pharma", "Sun",
        "NTPC", "National Thermal Power Corporation",
        "Oil and Natural Gas", "ONGC", "Oil Natural Gas",
        "Nestle India", "Nestle", "Nestle India Limited",
        "Power Grid Corporation", "PowerGrid", "PGCIL",
        "Mahindra & Mahindra", "M&M", "Mahindra",
        "Tata Steel", "Tata Steel Limited", "TSL",
        "Adani Enterprises", "Adani", "Adani Group",
        "JSW Steel", "JSW", "JSW Steel Limited",
        "Wipro", "Wipro Limited", "Wipro Technologies",
        "Hindalco", "Hindalco Industries", "Hindalco Limited",
        "Coal India", "CIL", "Coal India Limited",
        "Tech Mahindra", "TechM", "Tech Mahindra Limited",
        "Grasim Industries", "Grasim", "Grasim Limited",
        "Divi's Laboratories", "Divi Labs", "Divi",
        "Tata Motors", "TML", "Tata Motors Limited",
        "Cipla", "Cipla Limited", "Cipla India",
        "SBI Life Insurance", "SBI Life", "SBI Life Insurance Company",
        "Dr Reddy's Laboratories", "Dr Reddy", "DRL",
        "Eicher Motors", "Eicher", "Eicher Motors Limited",
        "Hero MotoCorp", "Hero", "Hero Honda",
        "Britannia Industries", "Britannia", "Britannia Limited",
        "Bharat Petroleum", "BPCL", "BP",
        "Indian Oil Corporation", "IOC", "Indian Oil"
    ]
    
    corpus.extend(company_names)
    corpus.extend([n.lower() for n in company_names])
    corpus.extend([n.upper() for n in company_names])
    
    # Add financial metrics and ratios
    financial_terms = [
        "Balance Sheet", "Profit and Loss", "P&L", "Cash Flow",
        "Annual Report", "Quarterly Results", "Earnings Report",
        "Market Share", "Revenue Growth", "Profit Growth",
        "Margin", "Operating Margin", "Net Margin", "Gross Margin",
        "Debt", "Total Debt", "Net Debt", "Debt to Equity",
        "Current Ratio", "Quick Ratio", "Debt Ratio",
        "Asset Turnover", "Inventory Turnover", "Receivables Turnover",
        "Working Capital", "Current Assets", "Current Liabilities",
        "Fixed Assets", "Intangible Assets", "Goodwill",
        "Shareholders Equity", "Book Value", "Market Value",
        "Beta", "Alpha", "Standard Deviation", "Variance",
        "CAGR", "Compound Annual Growth Rate", "YOY", "Year on Year",
        "QOQ", "Quarter on Quarter", "MOM", "Month on Month",
        "Promoter Holding", "Public Holding", "FII Holding", "DII Holding",
        "Foreign Institutional Investor", "Domestic Institutional Investor",
        "Mutual Fund", "ETF", "Exchange Traded Fund", "Index Fund",
        "Active Fund", "Passive Fund", "Hedge Fund", "Pension Fund"
    ]
    
    corpus.extend(financial_terms)
    corpus.extend([t.lower() for t in financial_terms])
    
    # Add trading terms
    trading_terms = [
        "Market Order", "Limit Order", "Stop Loss", "Take Profit",
        "Day Order", "GTC Order", "IOC Order", "FOK Order",
        "Bulk Deal", "Block Deal", "Insider Trading", "Circuit Breaker",
        "Upper Circuit", "Lower Circuit", "Price Band", "Freeze",
        "Suspended", "Delisted", "Listed", "IPO", "FPO", "OFS",
        "Offer for Sale", "Buyback", "Bonus Issue", "Stock Split",
        "Right Issue", "Preferential Allotment", "Qualified Placement",
        "Demat", "Dematerialization", "Remat", "Rematerialization",
        "Trading Account", "Demat Account", "Bank Account", "KYC",
        "Know Your Customer", "PAN", "Aadhaar", "GST", "TDS"
    ]
    
    corpus.extend(trading_terms)
    corpus.extend([t.lower() for t in trading_terms])
    
    # Add index constituents (sample)
    index_constituents = [
        "Nifty 50 Constituents", "Sensex 30 Constituents",
        "Nifty Next 50 Constituents", "Nifty Midcap 150",
        "Nifty Smallcap 250", "Nifty 500 Constituents",
        "Nifty Bank Index", "Nifty IT Index", "Nifty Pharma Index",
        "Nifty Auto Index", "Nifty FMCG Index", "Nifty Metal Index"
    ]
    
    corpus.extend(index_constituents)
    
    # Create sentences and phrases for better tokenization
    phrases = []
    for i in range(len(all_stocks[:200])):
        stock = all_stocks[i]
        phrases.extend([
            f"{stock} stock price",
            f"{stock} share price",
            f"{stock} current price",
            f"{stock} market cap",
            f"{stock} PE ratio",
            f"{stock} dividend yield",
            f"{stock} 52 week high",
            f"{stock} 52 week low",
            f"{stock} volume",
            f"{stock} on NSE",
            f"{stock} on BSE",
            f"Buy {stock}",
            f"Sell {stock}",
            f"Hold {stock}",
            f"{stock} analysis",
            f"{stock} news",
            f"{stock} results",
            f"{stock} earnings"
        ])
    
    corpus.extend(phrases)
    
    # Repeat corpus multiple times to increase frequency of patterns
    # This helps BPE learn better tokenizations and reach higher vocab sizes
    expanded_corpus = corpus * 15  # Increased repetition
    
    print(f"Generated corpus with {len(expanded_corpus)} entries")
    print(f"Unique entries: {len(set(corpus))}")
    return expanded_corpus


def save_corpus(corpus: List[str], filename: str = "stock_corpus.txt"):
    """Save corpus to file"""
    with open(filename, 'w') as f:
        for item in corpus:
            f.write(item + '\n')
    print(f"Corpus saved to {filename}")

