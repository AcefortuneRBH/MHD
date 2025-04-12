def regulate_mhd_supply(current_supply, market_demand):
    target_supply = 9000000000000
    if market_demand < 0.8:
        burn_amount = (target_supply - current_supply) * 0.01
        return f"🔥 Burning {burn_amount} MHD to stabilize value"
    elif market_demand > 1.2:
        return "✅ Market demand is high, holding supply steady"
    else:
        return "⚖️ Supply is stable, no action needed"

market_demand = 1.05
print(regulate_mhd_supply(9000000000000, market_demand))

