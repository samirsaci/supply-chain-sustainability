"""
Supply Chain Sustainability - CO2 Emissions Reporting

This script calculates CO2 emissions for transportation
based on shipment data and emission factors.
"""

import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# Emission factors (kg CO2 per ton.km)
EMISSION_FACTORS = {
    "road": 0.062,    # Truck
    "rail": 0.022,    # Train
    "sea": 0.016,     # Container ship
    "air": 0.602,     # Air freight
}


def calculate_emissions(weight_kg, distance_km, mode):
    """
    Calculate CO2 emissions for a shipment.

    Formula: CO2 (kg) = Weight (tons) × Distance (km) × Emission Factor
    """
    weight_tons = weight_kg / 1000
    factor = EMISSION_FACTORS.get(mode.lower(), 0)
    return weight_tons * distance_km * factor


def load_shipment_data(filepath):
    """Load shipment data from CSV."""
    df = pd.read_csv(filepath)
    return df


def create_sample_data():
    """Create sample shipment data."""
    data = {
        "shipment_id": range(1, 21),
        "origin": ["Warehouse_A"] * 10 + ["Warehouse_B"] * 10,
        "destination": [
            "Customer_1", "Customer_2", "Customer_3", "Customer_4", "Customer_5",
            "Customer_6", "Customer_7", "Customer_8", "Customer_9", "Customer_10",
            "Customer_11", "Customer_12", "Customer_13", "Customer_14", "Customer_15",
            "Customer_16", "Customer_17", "Customer_18", "Customer_19", "Customer_20",
        ],
        "weight_kg": [500, 1200, 800, 2500, 1500, 3000, 900, 1800, 2200, 700,
                      1100, 2800, 600, 1900, 2400, 1300, 850, 2100, 1600, 950],
        "distance_road": [120, 0, 350, 200, 0, 180, 450, 0, 280, 160,
                         220, 0, 380, 140, 0, 260, 320, 0, 190, 410],
        "distance_sea": [0, 4500, 0, 0, 6200, 0, 0, 3800, 0, 0,
                        0, 5100, 0, 0, 4800, 0, 0, 5500, 0, 0],
        "distance_air": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 1200, 0, 0, 0, 0, 0, 800, 0],
        "distance_rail": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 600, 0, 0, 0, 0, 0, 500],
    }
    return pd.DataFrame(data)


def calculate_shipment_emissions(df):
    """Calculate CO2 emissions for all shipments."""
    df = df.copy()

    # Calculate emissions by mode
    df["co2_road"] = df.apply(
        lambda row: calculate_emissions(row["weight_kg"], row.get("distance_road", 0), "road"),
        axis=1
    )
    df["co2_sea"] = df.apply(
        lambda row: calculate_emissions(row["weight_kg"], row.get("distance_sea", 0), "sea"),
        axis=1
    )
    df["co2_air"] = df.apply(
        lambda row: calculate_emissions(row["weight_kg"], row.get("distance_air", 0), "air"),
        axis=1
    )
    df["co2_rail"] = df.apply(
        lambda row: calculate_emissions(row["weight_kg"], row.get("distance_rail", 0), "rail"),
        axis=1
    )

    # Total emissions
    df["co2_total"] = df["co2_road"] + df["co2_sea"] + df["co2_air"] + df["co2_rail"]

    return df


def generate_report(df):
    """Generate CO2 emissions report."""
    print("=" * 60)
    print("CO2 EMISSIONS REPORT - TRANSPORTATION")
    print("=" * 60)

    # Overall statistics
    total_weight = df["weight_kg"].sum() / 1000  # in tons
    total_emissions = df["co2_total"].sum()

    print(f"\n--- SUMMARY ---")
    print(f"Total Shipments: {len(df)}")
    print(f"Total Weight: {total_weight:,.2f} tons")
    print(f"Total CO2 Emissions: {total_emissions:,.2f} kg")
    print(f"Emissions per ton shipped: {total_emissions/total_weight:.2f} kg CO2/ton")

    # Emissions by mode
    print(f"\n--- EMISSIONS BY MODE ---")
    modes = ["road", "sea", "air", "rail"]
    print(f"{'Mode':<10} {'CO2 (kg)':<15} {'Share (%)':<12}")
    print("-" * 40)

    for mode in modes:
        col = f"co2_{mode}"
        mode_total = df[col].sum()
        share = (mode_total / total_emissions * 100) if total_emissions > 0 else 0
        print(f"{mode.capitalize():<10} {mode_total:<15,.2f} {share:<12.1f}")

    # Emissions by origin
    print(f"\n--- EMISSIONS BY ORIGIN ---")
    by_origin = df.groupby("origin").agg({
        "weight_kg": "sum",
        "co2_total": "sum"
    })
    print(by_origin.round(2))

    # Top 5 highest emission shipments
    print(f"\n--- TOP 5 HIGHEST EMISSION SHIPMENTS ---")
    top5 = df.nlargest(5, "co2_total")[
        ["shipment_id", "destination", "weight_kg", "co2_total"]
    ]
    print(top5.to_string(index=False))

    # Emission factors used
    print(f"\n--- EMISSION FACTORS USED ---")
    print(f"{'Mode':<10} {'Factor (kg CO2/ton.km)':<25}")
    print("-" * 35)
    for mode, factor in EMISSION_FACTORS.items():
        print(f"{mode.capitalize():<10} {factor:<25}")

    return df


def export_results(df, filepath="co2_emissions_report.csv"):
    """Export results to CSV."""
    df.to_csv(filepath, index=False)
    print(f"\nResults exported to: {filepath}")


def load_real_data():
    """Load real data from the data folder (matching the notebook)."""
    # Load order lines
    df_lines = pd.read_csv('data/order_lines.csv', index_col=0)

    # Load UOM conversions
    df_uom = pd.read_csv('data/uom_conversions.csv', index_col=0)

    # Join
    df_join = df_lines.copy()
    df_join = pd.merge(df_join, df_uom, on=['Item Code'], how='left')

    # Load distances
    df_dist = pd.read_csv('data/distances.csv', index_col=0)
    df_dist['Location'] = df_dist['Customer Country'].astype(str) + ', ' + df_dist['Customer City'].astype(str)

    # Load GPS locations
    df_gps = pd.read_csv('data/gps_locations.csv', index_col=0)
    df_dist = pd.merge(df_dist, df_gps, on='Location', how='left')

    # Final join
    df_join = pd.merge(df_join, df_dist, on=['Warehouse Code', 'Customer Code'], how='left')

    # Calculate weight in KG
    df_join['KG'] = df_join['Units'] * df_join['Conversion Ratio']

    return df_join


def main():
    """Main function for CO2 emissions reporting."""
    # Load or create sample data
    try:
        df = load_real_data()
        print(f"Loaded {len(df):,} order lines from data folder.")

        # Calculate CO2 emissions using real data
        dict_co2e = {'Air': 2.1, 'Sea': 0.01, 'Road': 0.096, 'Rail': 0.028}
        modes = ['Road', 'Rail', 'Sea', 'Air']

        for mode in modes:
            df[f'CO2 {mode}'] = df['KG'].astype(float) / 1000 * df[mode].astype(float) * dict_co2e[mode]
        df['CO2 Total'] = df[[f'CO2 {mode}' for mode in modes]].sum(axis=1)

        # Generate summary report
        print("=" * 60)
        print("CO2 EMISSIONS REPORT - TRANSPORTATION")
        print("=" * 60)

        total_weight = df['KG'].sum() / 1000  # in tons
        total_emissions = df['CO2 Total'].sum()

        print(f"\n--- SUMMARY ---")
        print(f"Total Order Lines: {len(df):,}")
        print(f"Total Weight: {total_weight:,.2f} tons")
        print(f"Total CO2 Emissions: {total_emissions:,.2f} kg")

        print(f"\n--- EMISSIONS BY MODE ---")
        for mode in modes:
            mode_total = df[f'CO2 {mode}'].sum()
            share = (mode_total / total_emissions * 100) if total_emissions > 0 else 0
            print(f"{mode:<10} {mode_total:>12,.2f} kg ({share:.1f}%)")

        # Save detailed report
        df.to_csv('data/detailed_report.csv')
        print(f"\nDetailed report saved to: data/detailed_report.csv")

    except FileNotFoundError:
        print("Data files not found. Using sample data.")
        df = create_sample_data()

        # Calculate emissions
        df = calculate_shipment_emissions(df)

        # Generate report
        generate_report(df)

        # Export results
        export_results(df)


if __name__ == "__main__":
    main()
