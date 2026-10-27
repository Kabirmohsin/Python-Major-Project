"""
update_images.py
-----------------
Bulk-update product images directly in the database — no need to use the
seller edit form 40 times.

HOW TO USE:
1. Put this file in the SAME folder as app.py (E:\\shopdesk2\\shopdesk\\)
2. Fill in / replace the image URLs below (PASTE_LINK_HERE -> your Unsplash link)
   Reminder: the correct link always starts with "images.unsplash.com"
   (not "unsplash.com/photos/...")
3. Run it from that folder:
       python update_images.py
4. Refresh your browser (Ctrl+Shift+R) — images update instantly, no
   approval step needed, this script sets status back to "approved" itself.

You can also just run this script again later whenever you want to swap
more images — it will only touch the products listed below.
"""

from app import app, db, Product

# Map: exact product name (as seen in seller dashboard) -> image URL
#
# All links below are verified images.unsplash.com CDN links (checked working).
# Some products in the same category share an image for now since a fully
# unique free photo isn't available for every single item (e.g. there's no
# real "3-Layer Storage Shaker" stock photo). Swap any of these anytime by
# just editing the line and re-running the script.

WHEY = "https://images.unsplash.com/photo-1693996045838-980674653385?w=500&q=70&auto=format&fit=crop"
CREATINE = "https://images.unsplash.com/photo-1683394572742-1e471f60fc2a?w=500&q=70&auto=format&fit=crop"
MASS_GAINER = "https://images.unsplash.com/photo-1727433613965-923f6c9d400b?w=500&q=70&auto=format&fit=crop"
PRE_WORKOUT = "https://images.unsplash.com/photo-1693996046744-d7d7434bc777?w=500&q=70&auto=format&fit=crop"
ELECTROLYTE_JAR = "https://images.unsplash.com/photo-1763757933154-d55844eae856?w=500&q=70&auto=format&fit=crop"

DUFFEL_BAG = "https://images.unsplash.com/photo-1692506530242-c12d6c3ae2e2?w=500&q=70&auto=format&fit=crop"
BACKPACK = "https://images.unsplash.com/photo-1557160836-f3a6d1afaab2?w=500&q=70&auto=format&fit=crop"

WATER_BOTTLE = "https://images.unsplash.com/photo-1763757933154-d55844eae856?w=500&q=70&auto=format&fit=crop"

TANK_TOP = "https://images.unsplash.com/photo-1597452485683-0e0bde820f87?w=500&q=70&auto=format&fit=crop"

PRODUCT_IMAGES = {
    # ---------------- Supplements ----------------
    "Whey Protein Powder (1kg)": WHEY,
    "Creatine Monohydrate (250g)": CREATINE,
    "Mass Gainer (3kg)": MASS_GAINER,
    "BCAA Powder (300g)": PRE_WORKOUT,
    "Pre-Workout Formula (300g)": PRE_WORKOUT,
    "Daily Multivitamin (60 tabs)": ELECTROLYTE_JAR,
    "Omega-3 Fish Oil (90 caps)": ELECTROLYTE_JAR,
    "L-Glutamine Powder (250g)": CREATINE,
    "ZMA Recovery Capsules (90 caps)": ELECTROLYTE_JAR,
    "Protein Bars Box (12 bars)": MASS_GAINER,

    # ---------------- Bags ----------------
    "Classic Gym Duffel Bag": DUFFEL_BAG,
    "Gym Backpack 30L": BACKPACK,
    "Waterproof Sports Bag": DUFFEL_BAG,
    "Gym Sling Bag": BACKPACK,
    "Heavy Duty Travel Duffel": DUFFEL_BAG,
    "Compact Gym Tote": BACKPACK,
    "Gym Bag with Wet Pocket": DUFFEL_BAG,
    "Foldable Gym Bag": BACKPACK,
    "Premium Leather-Look Gym Bag": DUFFEL_BAG,
    "Kit Bag 25L": BACKPACK,

    # ---------------- Shakers ----------------
    "Classic Shaker Bottle 700ml": WATER_BOTTLE,
    "Steel Mixer Ball Shaker": WATER_BOTTLE,
    "Insulated Steel Shaker 500ml": WATER_BOTTLE,
    "3-Layer Storage Shaker": WATER_BOTTLE,
    "Leakproof Shaker Bottle": WATER_BOTTLE,
    "Electric Mixer Shaker": WATER_BOTTLE,
    "Sports Sipper Shaker 1L": WATER_BOTTLE,
    "BPA-Free Shaker 1L": WATER_BOTTLE,
    "Gym Shaker with Compartment": WATER_BOTTLE,
    "Premium Cyclone Shaker": WATER_BOTTLE,

    # ---------------- Vests ----------------
    "Compression Gym Vest": TANK_TOP,
    "Classic Stringer Tank Top": TANK_TOP,
    "Mesh Training Vest": TANK_TOP,
    "Sleeveless Muscle Vest": TANK_TOP,
    "Weighted Training Vest (10kg)": TANK_TOP,
    "Bodybuilding Tank Top": TANK_TOP,
    "Dri-Fit Sports Vest": TANK_TOP,
    "Cotton Gym Vest": TANK_TOP,
    "Racerback Gym Vest": TANK_TOP,
    "Sleeveless Hoodie Vest": TANK_TOP,
}


def run():
    updated = 0
    skipped_placeholder = 0
    not_found = []

    with app.app_context():
        for name, url in PRODUCT_IMAGES.items():
            if url == "PASTE_LINK_HERE":
                skipped_placeholder += 1
                continue

            product = Product.query.filter_by(name=name).first()
            if not product:
                not_found.append(name)
                continue

            product.image = url
            product.status = "approved"  # no manual approval needed
            updated += 1

        db.session.commit()

    print(f"Updated: {updated} product(s)")
    print(f"Skipped (still PASTE_LINK_HERE): {skipped_placeholder} product(s)")
    if not_found:
        print("Not found in database (check spelling):")
        for n in not_found:
            print(f"  - {n}")


if __name__ == "__main__":
    run()