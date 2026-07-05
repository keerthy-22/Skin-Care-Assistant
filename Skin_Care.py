import os 
skin_care = {

    "Dry Skin": {

        "Tight Skin": {

            "explanation":
            "Your skin doesn't have enough moisture and natural oils. This makes it feel tight, especially after washing.",

            "ingredients": [
                "Glycerin",
                "Hyaluronic Acid",
                "Ceramides",
                "Panthenol"
            ],

            "products": [
                "Hydrating Cleanser",
                "Hydrating Serum",
                "Ceramide Moisturizer"
            ],

            "morning": [
                "Hydrating Cleanser",
                "Hyaluronic Acid Serum",
                "Ceramide Moisturizer",
                "Sunscreen SPF 30+"
            ],

            "night": [
                "Hydrating Cleanser",
                "Ceramide Moisturizer"
            ],

            "tips": [
                "Avoid hot water",
                "Apply moisturizer on damp skin",
                "Drink enough water",
                "Use a humidifier if possible"
            ]

        },

        "Flaky Skin": {

            "explanation":
            "Dry skin loses moisture quickly, causing the outer layer to peel and flake.",

            "ingredients": [
                "Ceramides",
                "Shea Butter",
                "Squalane",
                "Glycerin"
            ],

            "products": [
                "Barrier Repair Cream",
                "Rich Moisturizer"
            ],

            "morning": [
                "Gentle Cleanser",
                "Rich Moisturizer",
                "Sunscreen"
            ],

            "night": [
                "Gentle Cleanser",
                "Barrier Repair Cream"
            ],

            "tips": [
                "Do not scrub flaky skin",
                "Avoid harsh face washes",
                "Moisturize twice daily"
            ]

        },

        "Dull Skin": {

            "explanation":
            "Dry skin reflects less light, making it appear dull and tired.",

            "ingredients": [
                "Vitamin C",
                "Niacinamide",
                "Hyaluronic Acid"
            ],

            "products": [
                "Vitamin C Serum",
                "Hydrating Moisturizer"
            ],

            "morning": [
                "Gentle Cleanser",
                "Vitamin C Serum",
                "Moisturizer",
                "Sunscreen"
            ],

            "night": [
                "Gentle Cleanser",
                "Hydrating Moisturizer"
            ],

            "tips": [
                "Sleep well",
                "Drink water",
                "Use sunscreen daily"
            ]

        },

        "Small Dry Bumps": {

            "explanation":
            "Dead skin builds up due to lack of moisture, creating rough bumps.",

            "ingredients": [
                "Lactic Acid",
                "PHA",
                "Ceramides",
                "Urea"
            ],

            "products": [
                "Gentle Exfoliating Serum",
                "Ceramide Moisturizer"
            ],

            "morning": [
                "Gentle Cleanser",
                "Moisturizer",
                "Sunscreen"
            ],

            "night": [
                "Exfoliating Serum (Once Weekly)",
                "Ceramide Moisturizer"
            ],

            "tips": [
                "Exfoliate only once a week",
                "Avoid picking bumps",
                "Keep skin hydrated"
            ]

        },

        "Fine Lines": {

            "explanation":
            "Dry skin loses water, making fine lines appear more visible.",

            "ingredients": [
                "Hyaluronic Acid",
                "Peptides",
                "Ceramides",
                "Squalane"
            ],

            "products": [
                "Hydrating Serum",
                "Rich Moisturizer"
            ],

            "morning": [
                "Hydrating Cleanser",
                "Hydrating Serum",
                "Moisturizer",
                "Sunscreen"
            ],

            "night": [
                "Hydrating Serum",
                "Rich Moisturizer"
            ],

            "tips": [
                "Sleep 7–8 hours",
                "Stay hydrated",
                "Always use sunscreen"
            ]

        },

        "Redness": {

            "explanation":
            "A damaged skin barrier allows irritants to enter the skin easily.",

            "ingredients": [
                "Centella Asiatica",
                "Ceramides",
                "Panthenol",
                "Allantoin"
            ],

            "products": [
                "Barrier Cream",
                "Soothing Moisturizer"
            ],

            "morning": [
                "Gentle Cleanser",
                "Barrier Cream",
                "Sunscreen"
            ],

            "night": [
                "Gentle Cleanser",
                "Soothing Moisturizer"
            ],

            "tips": [
                "Avoid fragrance",
                "Avoid hot showers",
                "Use gentle skincare"
            ]

        },

        "Itchy Skin": {

            "explanation":
            "Dry skin lacks moisture, leading to itching and discomfort.",

            "ingredients": [
                "Colloidal Oatmeal",
                "Ceramides",
                "Panthenol",
                "Shea Butter"
            ],

            "products": [
                "Soothing Cream",
                "Rich Moisturizer"
            ],

            "morning": [
                "Gentle Cleanser",
                "Moisturizer",
                "Sunscreen"
            ],

            "night": [
                "Soothing Cream",
                "Barrier Cream"
            ],

            "tips": [
                "Avoid scratching",
                "Use lukewarm water",
                "Moisturize twice daily"
            ]

        }

    },
    "Oily Skin": {

    "Excess Oil": {

        "explanation":
        "Your skin produces more oil (sebum) than needed, making it look shiny and greasy throughout the day.",

        "ingredients": [
            "Niacinamide",
            "Zinc PCA",
            "Green Tea Extract"
        ],

        "products": [
            "Foaming Cleanser",
            "Oil Control Serum",
            "Gel Moisturizer"
        ],

        "morning": [
            "Foaming Cleanser",
            "Niacinamide Serum",
            "Gel Moisturizer",
            "Oil-Free Sunscreen SPF 30+"
        ],

        "night": [
            "Foaming Cleanser",
            "Niacinamide Serum",
            "Gel Moisturizer"
        ],

        "tips": [
            "Don't wash your face more than twice a day.",
            "Use oil-free skincare products.",
            "Avoid harsh cleansers that over-dry the skin."
        ]

    },

    "Enlarged Pores": {

        "explanation":
        "Excess oil and dead skin can stretch pores, making them appear larger.",

        "ingredients": [
            "Niacinamide",
            "Salicylic Acid",
            "Zinc PCA"
        ],

        "products": [
            "Pore Refining Serum",
            "BHA Exfoliant"
        ],

        "morning": [
            "Foaming Cleanser",
            "Niacinamide Serum",
            "Gel Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Foaming Cleanser",
            "Salicylic Acid Serum (2–3 times/week)",
            "Gel Moisturizer"
        ],

        "tips": [
            "Exfoliate gently.",
            "Don't squeeze pores.",
            "Always remove makeup before sleeping."
        ]

    },

    "Blackheads & Whiteheads": {

        "explanation":
        "Oil, dead skin cells, and dirt clog pores, forming blackheads and whiteheads.",

        "ingredients": [
            "Salicylic Acid",
            "LHA",
            "Niacinamide"
        ],

        "products": [
            "BHA Exfoliant",
            "Foaming Cleanser"
        ],

        "morning": [
            "Foaming Cleanser",
            "Gel Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Foaming Cleanser",
            "Salicylic Acid Exfoliant",
            "Gel Moisturizer"
        ],

        "tips": [
            "Don't squeeze blackheads.",
            "Use BHA 2–3 times a week.",
            "Keep your skin clean."
        ]

    },

    "Acne & Pimples": {

        "explanation":
        "Clogged pores, excess oil, and bacteria can lead to acne and pimples.",

        "ingredients": [
            "Salicylic Acid",
            "Benzoyl Peroxide",
            "Azelaic Acid",
            "Niacinamide"
        ],

        "products": [
            "Acne Treatment Serum",
            "Spot Treatment",
            "Oil-Free Moisturizer"
        ],

        "morning": [
            "Foaming Cleanser",
            "Niacinamide Serum",
            "Gel Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Foaming Cleanser",
            "Salicylic Acid or Benzoyl Peroxide",
            "Gel Moisturizer"
        ],

        "tips": [
            "Don't pick pimples.",
            "Change pillowcases regularly.",
            "Be consistent with treatment."
        ]

    },

    "Acne Marks": {

        "explanation":
        "After pimples heal, they can leave dark spots called post-inflammatory hyperpigmentation.",

        "ingredients": [
            "Niacinamide",
            "Alpha Arbutin",
            "Tranexamic Acid",
            "Azelaic Acid"
        ],

        "products": [
            "Brightening Serum",
            "Lightweight Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Vitamin C Serum",
            "Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Alpha Arbutin Serum",
            "Moisturizer"
        ],

        "tips": [
            "Never skip sunscreen.",
            "Avoid picking acne.",
            "Results take time."
        ]

    },

    "Dull Skin": {

        "explanation":
        "Oil buildup and dead skin cells can make the skin look dull and tired.",

        "ingredients": [
            "Vitamin C",
            "Niacinamide"
        ],

        "products": [
            "Vitamin C Serum",
            "Gel Moisturizer"
        ],

        "morning": [
            "Foaming Cleanser",
            "Vitamin C Serum",
            "Gel Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Foaming Cleanser",
            "Gel Moisturizer"
        ],

        "tips": [
            "Exfoliate once or twice a week.",
            "Stay hydrated.",
            "Protect your skin from the sun."
        ]

    },

    "Dehydrated Oily Skin": {

        "explanation":
        "Your skin can be oily but still lack water, making it feel tight while looking shiny.",

        "ingredients": [
            "Hyaluronic Acid",
            "Glycerin",
            "Panthenol"
        ],

        "products": [
            "Hydrating Serum",
            "Gel Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Hydrating Serum",
            "Gel Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Hydrating Serum",
            "Gel Moisturizer"
        ],

        "tips": [
            "Don't skip moisturizer.",
            "Use hydrating products instead of harsh cleansers.",
            "Drink enough water."
        ]
   }
},
     "Combination Skin": {

        "Oily T-Zone & Dry Cheeks": {

        "explanation":
        "Combination skin has an oily forehead, nose, and chin (T-zone) while the cheeks are normal or dry.",

        "ingredients": [
            "Niacinamide",
            "Hyaluronic Acid",
            "Ceramides",
            "Glycerin"
        ],

        "products": [
            "Gentle Cleanser",
            "Niacinamide Serum",
            "Lightweight Gel Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Niacinamide Serum",
            "Gel Moisturizer",
            "Sunscreen SPF 30+"
        ],

        "night": [
            "Gentle Cleanser",
            "Hydrating Gel Moisturizer"
        ],

        "tips": [
            "Use lightweight moisturizers.",
            "Don't skip moisturizer on dry cheeks.",
            "Avoid harsh cleansers."
        ]

    },

    "Enlarged Pores": {

        "explanation":
        "The oily T-zone produces excess sebum, making pores look larger.",

        "ingredients": [
            "Niacinamide",
            "Salicylic Acid",
            "Zinc PCA"
        ],

        "products": [
            "Pore Refining Serum",
            "Salicylic Acid Serum"
        ],

        "morning": [
            "Gentle Cleanser",
            "Niacinamide Serum",
            "Gel Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Salicylic Acid Serum (2–3 times/week)",
            "Gel Moisturizer"
        ],

        "tips": [
            "Keep pores clean.",
            "Avoid over-exfoliating.",
            "Use non-comedogenic products."
        ]

    },

    "Blackheads & Whiteheads": {

        "explanation":
        "Excess oil in the T-zone can clog pores and lead to blackheads and whiteheads.",

        "ingredients": [
            "Salicylic Acid",
            "Niacinamide",
            "LHA"
        ],

        "products": [
            "BHA Exfoliant",
            "Foaming Cleanser"
        ],

        "morning": [
            "Foaming Cleanser",
            "Gel Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Foaming Cleanser",
            "Salicylic Acid Serum",
            "Gel Moisturizer"
        ],

        "tips": [
            "Exfoliate 2 times a week.",
            "Don't squeeze blackheads.",
            "Keep the T-zone clean."
        ]

    },

    "Dry or Flaky Cheeks": {

        "explanation":
        "Although the T-zone is oily, the cheeks may lose moisture and become dry or flaky.",

        "ingredients": [
            "Ceramides",
            "Shea Butter",
            "Squalane",
            "Glycerin"
        ],

        "products": [
            "Barrier Repair Cream",
            "Rich Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Moisturizer (extra on cheeks)",
            "Sunscreen"
        ],

        "night": [
            "Barrier Repair Cream",
            "Rich Moisturizer"
        ],

        "tips": [
            "Apply extra moisturizer to dry areas.",
            "Avoid hot water.",
            "Don't over-cleanse."
        ]

    },
        "Dull Skin": {

        "explanation":
        "Dead skin cells and uneven hydration can make combination skin look dull, especially if the skin isn't moisturized properly.",

        "ingredients": [
            "Vitamin C",
            "Niacinamide",
            "Hyaluronic Acid"
        ],

        "products": [
            "Vitamin C Serum",
            "Lightweight Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Vitamin C Serum",
            "Lightweight Moisturizer",
            "Sunscreen SPF 30+"
        ],

        "night": [
            "Gentle Cleanser",
            "Hydrating Moisturizer"
        ],

        "tips": [
            "Use sunscreen every day.",
            "Stay hydrated.",
            "Exfoliate once a week."
        ]

    },

    "Acne & Pimples": {

        "explanation":
        "Excess oil in the T-zone can clog pores and cause acne, while the cheeks may remain dry.",

        "ingredients": [
            "Salicylic Acid",
            "Niacinamide",
            "Azelaic Acid"
        ],

        "products": [
            "Acne Treatment Serum",
            "Oil-Free Gel Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Niacinamide Serum",
            "Gel Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Salicylic Acid Serum",
            "Gel Moisturizer"
        ],

        "tips": [
            "Don't pick pimples.",
            "Use non-comedogenic skincare.",
            "Wash your face twice daily."
        ]

    },

    "Uneven Texture & Small Bumps": {

        "explanation":
        "Dead skin cells and clogged pores can create rough skin texture and small bumps, especially around the forehead and chin.",

        "ingredients": [
            "PHA",
            "Lactic Acid",
            "Salicylic Acid",
            "Ceramides"
        ],

        "products": [
            "Gentle Exfoliating Serum",
            "Hydrating Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "PHA or Lactic Acid Serum (1–2 times/week)",
            "Moisturizer"
        ],

        "tips": [
            "Avoid harsh scrubs.",
            "Exfoliate only once or twice a week.",
            "Keep the skin hydrated."
        ]

    }

},
"Normal Skin": {

    "Dehydration": {

        "explanation":
        "Even normal skin can lose water, making it feel slightly tight or tired. This is called dehydration and is different from dry skin.",

        "ingredients": [
            "Hyaluronic Acid",
            "Glycerin",
            "Panthenol"
        ],

        "products": [
            "Hydrating Serum",
            "Lightweight Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Hydrating Serum",
            "Lightweight Moisturizer",
            "Sunscreen SPF 30+"
        ],

        "night": [
            "Gentle Cleanser",
            "Hydrating Serum",
            "Moisturizer"
        ],

        "tips": [
            "Drink enough water.",
            "Don't skip moisturizer.",
            "Avoid very hot water."
        ]

    },

    "Dull Skin": {

        "explanation":
        "Dead skin cells and environmental damage can make normal skin lose its natural glow.",

        "ingredients": [
            "Vitamin C",
            "Niacinamide",
            "Hyaluronic Acid"
        ],

        "products": [
            "Vitamin C Serum",
            "Daily Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Vitamin C Serum",
            "Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Hydrating Moisturizer"
        ],

        "tips": [
            "Use sunscreen daily.",
            "Eat fruits rich in antioxidants.",
            "Exfoliate once a week."
        ]

    },

    "Uneven Skin Tone": {

        "explanation":
        "Sun exposure, acne marks, and aging can cause uneven skin tone or pigmentation.",

        "ingredients": [
            "Niacinamide",
            "Vitamin C",
            "Alpha Arbutin",
            "Tranexamic Acid"
        ],

        "products": [
            "Brightening Serum",
            "Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Vitamin C Serum",
            "Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Alpha Arbutin Serum",
            "Moisturizer"
        ],

        "tips": [
            "Wear sunscreen every day.",
            "Avoid excessive sun exposure.",
            "Be patient; pigmentation fades gradually."
        ]

    },

    "Small Bumps & Rough Texture": {

        "explanation":
        "Dead skin buildup and clogged pores can make the skin feel rough or develop small bumps.",

        "ingredients": [
            "PHA",
            "Lactic Acid",
            "Salicylic Acid"
        ],

        "products": [
            "Gentle Exfoliating Serum",
            "Hydrating Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "PHA or Lactic Acid Serum (1–2 times/week)",
            "Moisturizer"
        ],

        "tips": [
            "Avoid harsh scrubs.",
            "Exfoliate only once or twice a week.",
            "Keep skin hydrated."
        ]

    },

    "Fine Lines": {

        "explanation":
        "As skin ages or becomes dehydrated, fine lines may become more visible.",

        "ingredients": [
            "Hyaluronic Acid",
            "Peptides",
            "Ceramides"
        ],

        "products": [
            "Hydrating Serum",
            "Anti-Aging Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Hydrating Serum",
            "Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Peptide Serum",
            "Moisturizer"
        ],

        "tips": [
            "Sleep well.",
            "Stay hydrated.",
            "Use sunscreen daily."
        ]

    },

    "Sensitive or Irritated Skin": {

        "explanation":
        "Even normal skin can occasionally become irritated due to weather changes or new skincare products.",

        "ingredients": [
            "Panthenol",
            "Centella Asiatica",
            "Allantoin",
            "Ceramides"
        ],

        "products": [
            "Soothing Moisturizer",
            "Barrier Repair Cream"
        ],

        "morning": [
            "Gentle Cleanser",
            "Barrier Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Barrier Repair Cream"
        ],

        "tips": [
            "Avoid fragrance if your skin feels irritated.",
            "Patch test new products.",
            "Keep your routine simple."
        ]

    },

    "Sun Damage & Premature Aging": {

        "explanation":
        "UV rays can damage collagen, causing wrinkles, pigmentation, and early signs of aging.",

        "ingredients": [
            "Vitamin C",
            "Vitamin E",
            "Niacinamide",
            "Sunscreen"
        ],

        "products": [
            "Antioxidant Serum",
            "Broad-Spectrum Sunscreen"
        ],

        "morning": [
            "Gentle Cleanser",
            "Vitamin C Serum",
            "Moisturizer",
            "Sunscreen SPF 50"
        ],

        "night": [
            "Gentle Cleanser",
            "Hydrating Moisturizer"
        ],

        "tips": [
            "Apply sunscreen every morning.",
            "Reapply sunscreen every 2–3 hours when outdoors.",
            "Wear hats or seek shade during peak sunlight."
        ]

    }

},
     "Sensitive Skin": {

    "Redness & Irritation": {

        "explanation":
        "Sensitive skin reacts easily to weather, skincare products, or environmental triggers, causing redness and irritation.",

        "ingredients": [
            "Centella Asiatica",
            "Panthenol",
            "Allantoin",
            "Bisabolol"
        ],

        "products": [
            "Soothing Serum",
            "Barrier Repair Moisturizer"
        ],

        "morning": [
            "Gentle Fragrance-Free Cleanser",
            "Centella Serum",
            "Ceramide Moisturizer",
            "Mineral Sunscreen SPF 30+"
        ],

        "night": [
            "Gentle Cleanser",
            "Barrier Repair Moisturizer"
        ],

        "tips": [
            "Avoid fragrance.",
            "Avoid harsh scrubs.",
            "Use lukewarm water."
        ]

    },

    "Burning or Stinging": {

        "explanation":
        "A damaged skin barrier allows products to penetrate too deeply, causing a burning or stinging sensation.",

        "ingredients": [
            "Ceramides",
            "Panthenol",
            "Glycerin"
        ],

        "products": [
            "Barrier Cream",
            "Hydrating Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Barrier Cream",
            "Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Barrier Repair Cream"
        ],

        "tips": [
            "Stop using irritating products temporarily.",
            "Choose fragrance-free skincare.",
            "Patch test new products."
        ]

    },

    "Dryness & Weak Skin Barrier": {

        "explanation":
        "Sensitive skin often loses moisture easily because its protective barrier is weakened.",

        "ingredients": [
            "Ceramides",
            "Cholesterol",
            "Fatty Acids",
            "Squalane"
        ],

        "products": [
            "Barrier Repair Cream",
            "Rich Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Barrier Cream",
            "Mineral Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Rich Moisturizer"
        ],

        "tips": [
            "Moisturize twice daily.",
            "Avoid long hot showers.",
            "Keep your skincare routine simple."
        ]

    },

    "Itchy Skin": {

        "explanation":
        "Sensitive skin may become itchy due to dryness, irritation, or exposure to allergens.",

        "ingredients": [
            "Colloidal Oatmeal",
            "Panthenol",
            "Ceramides",
            "Shea Butter"
        ],

        "products": [
            "Soothing Cream",
            "Rich Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Soothing Cream",
            "Barrier Repair Cream"
        ],

        "tips": [
            "Don't scratch your skin.",
            "Use fragrance-free products.",
            "Keep skin moisturized."
        ]

    },

    "Reacts to Skincare Products": {

        "explanation":
        "Sensitive skin may react to fragrances, alcohol, or strong active ingredients with redness or discomfort.",

        "ingredients": [
            "Glycerin",
            "Hyaluronic Acid",
            "Ceramides"
        ],

        "products": [
            "Gentle Cleanser",
            "Fragrance-Free Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Hydrating Moisturizer",
            "Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Ceramide Moisturizer"
        ],

        "tips": [
            "Introduce one new product at a time.",
            "Always patch test.",
            "Avoid alcohol-based toners."
        ]

    },

    "Sun-Induced Redness": {

        "explanation":
        "Sensitive skin can become red and inflamed after sun exposure because UV rays weaken the skin barrier.",

        "ingredients": [
            "Aloe Vera",
            "Centella Asiatica",
            "Panthenol"
        ],

        "products": [
            "Soothing Gel",
            "Mineral Sunscreen"
        ],

        "morning": [
            "Gentle Cleanser",
            "Ceramide Moisturizer",
            "Mineral Sunscreen SPF 50"
        ],

        "night": [
            "Aloe Vera Gel",
            "Barrier Repair Cream"
        ],

        "tips": [
            "Wear sunscreen every day.",
            "Avoid direct midday sun.",
            "Reapply sunscreen every 2–3 hours outdoors."
        ]

    },

    "Weather Sensitivity": {

        "explanation":
        "Cold weather, wind, or heat can trigger redness, dryness, and irritation in sensitive skin.",

        "ingredients": [
            "Ceramides",
            "Squalane",
            "Glycerin"
        ],

        "products": [
            "Barrier Cream",
            "Rich Moisturizer"
        ],

        "morning": [
            "Gentle Cleanser",
            "Barrier Cream",
            "Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Rich Moisturizer"
        ],

        "tips": [
            "Protect your skin from extreme weather.",
            "Use a humidifier in dry environments.",
            "Avoid very hot water."
        ]

    }

}

}
def display_options(options):
    count = 1 
    for problem in options.keys():
        print(f"{count}. {problem}")
        count += 1 
def display_data(data,key):
    print(key.title()+":")
    print("-----------------")
    for item in data:
        print(item)

while True:
    # this is to display major skin problems 
    display_options(skin_care)
    choice = input("choose the type of problem: ")
    problem = skin_care[choice]
    
    # This is to display skin concern 
    display_options(problem)
    choice = input("choose your problem problem: ")
    problem = problem[choice]
    
    while True:
        # This is to display available data about that skin concern
        display_options(problem)
        choice = input("choose your problem problem: ")
        data = problem[choice]
        if choice == "explanation":
            print(data)
        else:
            display_data(data,choice)
        
        choice = input("Do you want to coninue? (y/n): ")
        if choice == "y":
            os.system("clear") #"cls"
            continue
        else:
            break 
    os.system("clear")
    
