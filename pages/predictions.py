# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd
import numpy as np

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ### Select the features below based on the item intended for listing.

            """,
        className='mb-4'),
        dcc.Markdown('##### ** Item Condition **'),
        dcc.RadioItems(
            id = 'item-condition',
            options = [
                {'label': 'New', 'value': 3},
                {'label': 'Like New', 'value': 1},
                {'label': 'Good', 'value': 2},
                {'label': 'Fair', 'value': 4},
                {'label': 'Poor', 'value': 5}
            ],
            value=1,
            className='mb-3',
        ),
        dcc.Markdown('##### ** Item Category **'),
        dcc.Dropdown(
            id = 'main-category',
            options = [
                {'label': 'Women', 'value': 1},
                {'label': 'Beauty', 'value': 3},
                {'label': 'Kids', 'value': 2},
                {'label': 'Electronics', 'value': 4},
                {'label': 'Men', 'value': 6},
                {'label': 'Home', 'value': 7},
                {'label': 'Vintage & Collectibles', 'value': 5},
                {'label': 'Sports & Outdoors', 'value': 8}
            ],
            value=4,
            className='mb-3',
        ),
        dcc.Markdown('##### ** Brand Name **'),
        dcc.Dropdown(
            id = 'brand-name',
            options = [
                {'label': 'PINK', 'value': 1},
                {'label': 'Old Navy', 'value': 2},
                {'label': 'Nike', 'value': 3},
                {'label': "Victoria's Secret", 'value': 4},
                {'label': 'Nintendo', 'value': 5},
                {'label': 'Anastasia Beverly Hills', 'value': 6},
                {'label': 'Forever 21', 'value': 7},
                {'label': 'Disney', 'value': 8},
                {'label': 'Kate Spade', 'value': 9},
                {'label': 'LuLaRoe', 'value': 10},
                {'label': 'Adidas', 'value': 11},
                {'label': 'Lululemon', 'value': 12},
                {'label': 'Betsey Johnson', 'value': 13},
                {'label': 'Gap', 'value': 14},
                {'label': 'Jordan', 'value': 15},
                {'label': 'NYX', 'value': 16},
                {'label': 'Samsumg', 'value': 17},
                {'label': 'Apple', 'value': 18},
                {'label': 'Sony', 'value': 19},
                {'label': 'Michael Kors', 'value': 20},
                {'label': 'Tommy Hilfiger', 'value': 21},
                {'label': 'Tory Burch', 'value': 22},
                {'label': 'Under Armour', 'value': 23},
                {'label': 'Sephora', 'value': 24},
                {'label': 'Coach', 'value': 25},
                {'label': 'Vera Bradley', 'value': 26},
                {'label': 'Funko', 'value': 27},
                {'label': 'Steve Madden', 'value': 28},
                {'label': 'Lily Pulitzer', 'value': 29},
                {'label': 'True Religion Brand Jeans', 'value': 30},
                {'label': 'Younique', 'value': 31},
                {'label': 'Target', 'value': 32},
                {'label': 'Gucci', 'value': 33},
                {'label': "Carter's", 'value': 34},
                {'label': 'Hollister', 'value': 35},
                {'label': 'Too Faced', 'value': 36},
                {'label': 'Mattel', 'value': 37},
                {'label': 'Tarte', 'value': 38},
                {'label': 'Rae Dunn', 'value': 39},
                {'label': 'Urban Decay', 'value': 40},
                {'label': 'Xbox', 'value': 41},
                {'label': 'Ralph Lauren', 'value': 42},
                {'label': 'Brandy Melville', 'value': 43},
                {'label': 'Fitbit', 'value': 44},
                {'label': 'SeneGence', 'value': 45},
                {'label': 'American Eagle', 'value': 46},
                {'label': 'The North Face', 'value': 47},
                {'label': 'Mary Kay', 'value': 48},
                {'label': 'MAC', 'value': 49},
                {'label': 'Xhilaration', 'value': 50},
                {'label': 'Independent', 'value': 51},
                {'label': 'Bebe', 'value': 52},
                {'label': 'American Boy & Girl', 'value': 53},
                {'label': 'Columbia', 'value': 54},
                {'label': 'Miss Me', 'value': 55},
                {'label': 'Scentsy', 'value': 56},
                {'label': 'Polo Ralph Lauren', 'value': 57},
                {'label': 'H&M', 'value': 58},
                {'label': 'Rock Revival', 'value': 59},
                {'label': 'Dooney & Bourke', 'value': 60},
                {'label': 'Louis Vuitton', 'value': 61},
                {'label': 'Benefit', 'value': 62},
                {'label': 'Bath & Body Works', 'value': 63},
                {'label': 'Juicy Couture', 'value': 64},
                {'label': 'Aeropostale', 'value': 65},
                {'label': 'Express', 'value': 66},
                {'label': 'Reebok', 'value': 67},
                {'label': 'Patagonia', 'value': 68},
                {'label': 'Vans', 'value': 69},
                {'label': 'Urban Outfitters', 'value': 70},
                {'label': 'Gymboree', 'value': 71},
                {'label': "Levi's", 'value': 72},
                {'label': 'Kat Von D', 'value': 73},
                {'label': 'Abercrombie & Fitch', 'value': 74},
                {'label': 'NFL', 'value': 75},
                {'label': 'GUESS', 'value': 76},
                {'label': 'American Girl', 'value': 77},
                {'label': 'Pokemon', 'value': 78},
                {'label': 'Vineyard Vines', 'value': 79},
                {'label': 'Chanel', 'value': 80},
                {'label': 'Pandora', 'value': 81},
                {'label': 'Ray Ban', 'value': 82},
                {'label': 'Torrid', 'value': 83},
                {'label': 'Converse', 'value': 84},
                {'label': 'PUMA', 'value': 85},
                {'label': 'Free People', 'value': 86},
                {'label': 'Hot Topic', 'value': 87},
                {'label': 'Charlotte Russe', 'value': 88},
                {'label': 'Kylie Cosmetics', 'value': 89},
                {'label': 'Kendra Scott', 'value': 90},
                {'label': 'Vintage', 'value': 91},
                {'label': 'Calvin Klein', 'value': 92},
                {'label': 'Maybelline', 'value': 93},
                {'label': 'UGG Australia', 'value': 94},
                {'label': 'Air Jordan', 'value': 95},
                {'label': 'Customized & Personalized', 'value': 96},
                {'label': 'Harley Davidson', 'value': 97},
                {'label': 'Mossimo', 'value': 98},
                {'label': 'ALEX AND ANI', 'value': 99},
                {'label': 'Clinique', 'value': 100}
            ],
            value=4,
            className='mb-3',
        ),
        dcc.Markdown('##### ** Item Sub Category **'),
        dcc.Dropdown(
            id = 'sub-category',
            options = [
                {'label': 'Athletic Apparel/Shirts & Tops', 'value': 1},
                {'label': 'Boys (4+)/Bottoms', 'value': 2},
                {'label': 'Boys (0-24 Months)/Shoes', 'value': 3},
                {'label': 'Sweaters/Full Zip', 'value': 4},
                {'label': 'Sweaters/Crewneck', 'value': 5},
                {'label': 'Athletic Apparel/Jackets', 'value': 6},
                {'label': 'Athletic Apparel/Shorts', 'value': 7},
                {'label': 'Athletic Apparel/Sports Bras', 'value': 8},
                {'label': 'Fragrance/Women', 'value': 9},
                {'label': 'Video Games & Consoles/Games', 'value': 10},
                {'label': 'Makeup/Eyes', 'value': 11},
                {'label': 'Coats & Jackets/Jean Jacket', 'value': 12},
                {'label': 'Accessories/Keychain', 'value': 13},
                {'label': 'Tops & Blouses/Tank, Cami', 'value': 14},
                {'label': "Women's Accessories/Wallets", 'value': 15},
                {'label': 'Dresses/Knee-Length', 'value': 16},
                {'label': 'Shoes/Fashion Sneakers', 'value': 17},
                {'label': 'Underwear/Bras', 'value': 18},
                {'label': 'Girls (2T-5T)/Shoes', 'value': 19},
                {'label': 'Sweaters/Hooded', 'value': 20},
                {'label': 'Girls (0-24 Months)/Dresses', 'value': 21},
                {'label': 'Shoes/Athletic', 'value': 22},
                {'label': 'Makeup/Lips', 'value': 23},
                {'label': 'Athletic Apparel/Pants, Tights, Leggings', 'value': 24},
                {'label': 'Cell Phones & Accessories/Cell Phones & Smartphones', 'value': 25},
                {'label': 'Underwear/Panties', 'value': 26},
                {'label': 'Dresses/Above Knee, Mini', 'value': 27},
                {'label': 'TV, Audio & Surveillance/Headphones', 'value': 28},
                {'label': 'Coats & Jackets/Trench', 'value': 29},
                {'label': 'Sweaters/Cowl Neck', 'value': 30},
                {'label': 'Coats & Jackets/Windbreaker', 'value': 31},
                {'label': "Women's Handbags/Shoulder Bag", 'value': 32},
                {'label': 'Makeup/Makeup Palettes', 'value': 33},
                {'label': 'Shoes/Flats', 'value': 34},
                {'label': 'Tops & Blouses/T-Shirts', 'value': 35},
                {'label': "Women's Handbags/Messenger & Crossbody", 'value': 36},
                {'label': 'Toys/Dolls & Accessories', 'value': 37},
                {'label': 'Cell Phones & Accessories/Cases, Covers & Skins', 'value': 38},
                {'label': 'Toys/Action Figures & Statues', 'value': 39},
                {'label': 'Cell Phones & Accessories/Cell Phone Accessories', 'value': 40},
                {'label': 'Athletic Apparel/Jerseys', 'value': 41},
                {'label': 'Tops & Blouses/Blouse', 'value': 42},
                {'label': 'Shoes/Sandals', 'value': 43},
                {'label': 'Jeans/Slim, Skinny', 'value': 44},
                {'label': 'Swimwear/Two-Piece', 'value': 45},
                {'label': "Women's Handbags/Totes & Shoppers", 'value': 46},
                {'label': "Men's Accessories/Sunglasses", 'value': 47},
                {'label': 'Other/Other', 'value': 48},
                {'label': 'Kitchen & Dining/Coffee & Tea Accessories', 'value': 49},
                {'label': 'Makeup/Face', 'value': 50},
                {'label': 'Tops/T-shirts', 'value': 51},
                {'label': 'Boys (4+)/Shoes', 'value': 52},
                {'label': 'Jeans/Leggings', 'value': 53},
                {'label': 'Underwear/Other', 'value': 54},
                {'label': 'Video Games & Consoles/Consoles', 'value': 55},
                {'label': 'Dresses/Full-Length', 'value': 56},
                {'label': 'Kitchen & Dining/Dining & Entertaining', 'value': 57},
                {'label': 'Boys (4+)/Top & T-shirts', 'value': 58},
                {'label': 'Cell Phones & Accessories/Cables & Adapters', 'value': 59},
                {'label': 'Exercise/Fitness Technology', 'value': 60},
                {'label': 'Makeup/Makeup Sets', 'value': 61},
                {'label': "Men's Accessories/Backpacks, Bags & Briefcases", 'value': 62},
                {'label': 'Boys (0-24 Months)/Tops & T-Shirts', 'value': 63},
                {'label': 'Apparel/Accessories', 'value': 64},
                {'label': 'Toys/Stuffed Animals & Plush', 'value': 65},
                {'label': 'Athletic Apparel/Socks', 'value': 66},
                {'label': 'Sweaters/Cardigan', 'value': 67},
                {'label': 'Skin Care/Face', 'value': 68},
                {'label': 'Exercise/Fitness Accessories', 'value': 69},
                {'label': 'Shoes/Pumps', 'value': 70},
                {'label': 'Dresses/Asymmetrical Hem', 'value': 71},
                {'label': 'Shorts/Casual Shorts', 'value': 72}, 
                {'label': 'Girls (0-24 Months)/Tops & T-Shirts', 'value': 73},
                {'label': 'Electronics/Video Game', 'value': 74},
                {'label': 'Sweats & Hoodies/Hoodie', 'value': 75},
                {'label': 'Jeans/Boot Cut', 'value': 76},
                {'label': 'Home Décor/Home Fragrance', 'value': 77},
                {'label': 'Girls (4+)/Dresses', 'value': 78},
                {'label': "Men's Accessories/Other", 'value': 79},
                {'label': "Women's Accessories/Watches", 'value': 80},
                {'label': 'Clothing/Sweater', 'value': 81},
                {'label': 'Jeans/Straight Leg', 'value': 82},
                {'label': "Women's Handbags/Satchel", 'value': 83},
                {'label': 'Tops/Button-Front', 'value': 84},
                {'label': 'Skin Care/Body', 'value': 85},
                {'label': 'Athletic Apparel/Tracksuits & Sweats', 'value': 86},
                {'label': 'Skirts/Mini', 'value': 87},
                {'label': 'Toy/Action Figure', 'value': 88},
                {'label': 'Shorts/Cargo', 'value': 89},
                {'label': "Men's Accessories/Hats", 'value': 90},
                {'label': 'Shoes/Boots', 'value': 91},
                {'label': 'Coats & Jackets/Fleece Jacket', 'value': 92},
                {'label': 'Boys (2T-5T)/Tops & T-Shirts', 'value': 93},
                {'label': 'Coats & Jackets/Vest', 'value': 94},
                {'label': 'Shoes/Loafers & Slip-Ons', 'value': 95},
                {'label': 'Girls (2T-5T)/Coats & Jackets', 'value': 96},
                {'label': 'Jewelry/Bracelets', 'value': 97},
                {'label': 'Girls (4+)/Accessories', 'value': 98},
                {'label': 'Trading Cards/Sports', 'value': 99},
                {'label': 'Swimwear/Cover-Ups', 'value': 100},
                {'label': "Women's Handbags/Backpack Style", 'value': 101},
                {'label': 'Coats & Jackets/Puffer', 'value': 102},
                {'label': 'Toys/Hobbies', 'value': 103},
                {'label': 'Trading Cards/Animation', 'value': 104},
                {'label': 'Jeans/Other', 'value': 105},
                {'label': 'Sweaters/Other', 'value': 106},
                {'label': 'Girls (0-24 Months)/Coats & Jackets', 'value': 107},
                {'label': 'Girls (2T-5T)/Tops & T-Shirts', 'value': 108},
                {'label': "Women's Accessories/Sunglasses", 'value': 109},
                {'label': 'Tops/Polo, Rugby', 'value': 110},
                {'label': 'Boys (0-24 Months)/One-Pieces', 'value': 111},
                {'label': 'Girls (4+)/Tops & T-Shirts', 'value': 112},
                {'label': 'Home Décor/Candles & Holders', 'value': 113},
                {'label': "Women's Handbags/Cosmetic Bags", 'value': 114},
                {'label': 'Boys (0-24 Months)/Bottoms', 'value': 115},
                {'label': 'Gear/Backpacks & Carriers', 'value': 116},
                {'label': 'Boys (4+)/Coats & Jackets', 'value': 117},
                {'label': 'Jeans/Boyfriend', 'value': 118},
                {'label': 'Seasonal Décor/Christmas', 'value': 119},
                {'label': 'Jewelry/Earrings', 'value': 120},
                {'label': 'Shoes/Other', 'value': 121},
                {'label': 'Boys (2T-5T)/Shoes', 'value': 122},
                {'label': 'Bath & Body/Bath', 'value': 123},
                {'label': 'Jewelry/Necklaces', 'value': 124},
                {'label': 'Hair Care/Styling Products', 'value': 125},
                {'label': 'Girls (0-24 Months)/One-Pieces', 'value': 126},
                {'label': 'Cell Phones & Accessories/Chargers & Cradles', 'value': 127},
                {'label': 'Sweats & Hoodies/Sweatshirt, Pullover', 'value': 128},
                {'label': 'Fragrance/Candles & Home Scents', 'value': 129},
                {'label': 'Pants/Casual Pants', 'value': 130},
                {'label': 'Team Sports/Football', 'value': 131},
                {'label': 'Girls (2T-5T)/Dresses', 'value': 132},
                {'label': 'Sweaters/Vest, Sleeveless', 'value': 133},
                {'label': 'Tops & Blouses/Button Down Shirt', 'value': 134},
                {'label': 'Girls (4+)/Shoes', 'value': 135},
                {'label': 'Girls (4+)/Other', 'value': 136},
                {'label': 'Sweats & Hoodies/Track & Sweat Pants', 'value': 137},
                {'label': 'Skirts/Straight, Pencil', 'value': 138},
                {'label': 'Tops & Blouses/Halter', 'value': 139},
                {'label': 'Sweaters/Turtleneck, Mock', 'value': 140},
                {'label': 'Maternity/Tops & Blouses', 'value': 141},
                {'label': 'Tops & Blouses/Tunic', 'value': 142},
                {'label': 'Computers & Tablets/iPad', 'value': 143},
                {'label': 'Jeans/Classic, Straight Leg', 'value': 144},
                {'label': 'Bags and Purses/Handbag', 'value': 145},
                {'label': 'Girls (0-24 Months)/Shoes', 'value': 146},
                {'label': "Women's Accessories/Hats", 'value': 147},
                {'label': 'Video Games & Consoles/Video Gaming Merchandise', 'value': 148},
                {'label': 'Seasonal Décor/Halloween', 'value': 149},
                {'label': 'Pants/Other', 'value': 150},
                {'label': 'Jewelry/Rings', 'value': 151},
                {'label': 'Coats & Jackets/Raincoat', 'value': 152},
                {'label': 'Home Décor/Home Décor Accents', 'value': 153},
                {'label': 'Tops & Blouses/Knit Top', 'value': 154},
                {'label': 'Skirts/Maxi', 'value': 155},
                {'label': 'Shoes/Slippers', 'value': 156},
                {'label': 'Athletic Apparel/Pants', 'value': 157},
                {'label': 'Coats & Jackets/Parka', 'value': 158},
                {'label': 'Bath & Body/Sets', 'value': 159},
                {'label': "Women's Accessories/Hair Accessories", 'value': 160},
                {'label': 'Girls (0-24 Months)/Other', 'value': 161},
                {'label': "Women's Accessories/Other", 'value': 162},
                {'label': 'Girls (4+)/Coats & Jackets', 'value': 163},
                {'label': 'Tops & Blouses/Other', 'value': 164},
                {'label': 'Sweaters/Collared', 'value': 165},
                {'label': 'Tools & Accessories/Makeup Brushes & Tools', 'value': 166},
                {'label': 'Underwear/G-Strings & Thongs', 'value': 167},
                {'label': 'Swimwear/One-Piece', 'value': 168},
                {'label': 'Skin Care/Hands & Nails', 'value': 169},
                {'label': 'Collectibles/Other', 'value': 170},
                {'label': "Women's Accessories/Belts", 'value': 171},
                {'label': 'Kitchen & Dining/Bakeware', 'value': 172},
                {'label': 'Bath & Body/Cleansers', 'value': 173},
                {'label': 'Tops & Blouses/Wrap', 'value': 174},
                {'label': 'Cell Phones & Accessories/Headsets', 'value': 175},
                {'label': 'Toys/Games', 'value': 176},
                {'label': 'Athletic Apparel/Skirts, Skorts & Dresses', 'value': 177},
                {'label': 'Maternity/Dresses', 'value': 178},
                {'label': 'Fragrance/Sets', 'value': 179},
                {'label': 'Fragrance/Men', 'value': 180},
                {'label': 'Pants/Khakis, Chinos', 'value': 181},
                {'label': 'Skirts/A-Line', 'value': 182},
                {'label': 'Hair Care/Shampoo & Conditioner Sets', 'value': 183},
                {'label': 'Collectibles/Doll', 'value': 184},
                {'label': 'Boys (2T-5T)/Coats & Jackets', 'value': 185},
                {'label': 'Boys (0-24 Months)/Coats & Jackets', 'value': 186},
                {'label': 'Coats & Jackets/Motorcycle', 'value': 187},
                {'label': 'Girls (2T-5T)/Bottoms', 'value': 188},
                {'label': 'Girls (2T-5T)/One-Pieces', 'value': 189},
                {'label': 'Pants/Capris, Cropped', 'value': 190},
                {'label': 'Video Games & Consoles/Accessories', 'value': 191},
                {'label': 'Boys (4+)/Other', 'value': 192},
                {'label': 'Jeans/Capri, Cropped', 'value': 193},
                {'label': 'Fan Shop/NCAA', 'value': 194},
                {'label': 'Fan Shop/NFL', 'value': 195},
                {'label': 'Sweaters/V-Neck', 'value': 196},
                {'label': 'Coats & Jackets/Other', 'value': 197},
                {'label': "Men's Accessories/Belts", 'value': 198},
                {'label': 'Apparel/Boys', 'value': 199},
                {'label': 'Suits & Blazers/Blazer', 'value': 200},
                {'label': 'Skin Care/Lips', 'value': 201},
                {'label': 'Boys (2T-5T)/Bottoms', 'value': 202},
                {'label': 'Skin Care/Eyes', 'value': 203},
                {'label': 'Swimwear/Swim Trunks', 'value': 204},
                {'label': 'Maternity/Jeans', 'value': 205},
                {'label': 'Tops/Tank', 'value': 206},
                {'label': 'Computers & Tablets/Components & Parts', 'value': 207},
                {'label': "Women's Accessories/Scarves & Wraps", 'value': 208},
                {'label': "Men's Accessories/Wallets", 'value': 209},
                {'label': 'Toys/Dress Up & Pretend Play', 'value': 210},
                {'label': 'Kitchen & Dining/Storage & Organization', 'value': 211},
                {'label': 'Dresses/Mid-Calf', 'value': 212},
                {'label': 'Tops/Dress Shirts', 'value': 213},
                {'label': 'Tools & Accessories/Bags & Cases', 'value': 214},
                {'label': 'Underwear/Thermal Underwear', 'value': 215},
                {'label': 'Tools & Accessories/Hair Styling Tools', 'value': 216},
                {'label': 'Collectibles/Souvenir', 'value': 217},
                {'label': 'Girls (0-24 Months)/Bottoms', 'value': 218},
                {'label': "Men's Accessories/Watches", 'value': 219},
                {'label': 'Bags and Purses/Luggage', 'value': 220},
                {'label': 'Cell Phones & Accessories/Screen Protectors', 'value': 221},
                {'label': 'TV, Audio & Surveillance/Portable Audio & Accessories', 'value': 222},
                {'label': 'Bags and Purses/Purse', 'value': 223},
                {'label': 'Bath & Body/Bathing Accessories', 'value': 224},
                {'label': 'Team Sports/Soccer', 'value': 225},
                {'label': 'Jeans/Relaxed', 'value': 226},
                {'label': 'Collectibles/Figurine', 'value': 227},
                {'label': 'Sweaters/Scoop Neck', 'value': 228},
                {'label': 'Pants/Dress Pants', 'value': 229},
                {'label': 'Jeans/Flare', 'value': 230},
                {'label': 'Makeup/Brushes & Applicators', 'value': 231},
                {'label': 'Boys (0-24 Months)/Accessories', 'value': 232},
                {'label': 'Apparel/Girls', 'value': 233},
                {'label': 'Girls (4+)/Jeans', 'value': 234},
                {'label': 'Coats & Jackets/Military', 'value': 235},
                {'label': 'Toy/Doll', 'value': 236},
                {'label': 'Boys (4+)/Accessories', 'value': 237},
                {'label': "Women's Handbags/Other", 'value': 238},
                {'label': 'Coats & Jackets/Flight', 'value': 239},
                {'label': 'Computers & Tablets/Laptops & Netbooks', 'value': 240},
                {'label': 'Makeup/Nails', 'value': 241},
                {'label': 'Storage & Organization/Jewelry Boxes & Organizers', 'value': 242},
                {'label': 'Skirts/Pleated', 'value': 243},
                {'label': 'Girls (0-24 Months)/Accessories', 'value': 244},
                {'label': 'Accessories/Eyewear', 'value': 245},
                {'label': 'Clothing/Shorts', 'value': 246},
                {'label': 'Footwear/Cleats', 'value': 247},
                {'label': 'Kitchen & Dining/Kitchen Utensils & Gadgets', 'value': 248},
                {'label': 'Fan Shop/NBA', 'value': 249},
                {'label': 'Jeans/Overalls', 'value': 250},
                {'label': 'Makeup/Makeup Remover', 'value': 251},
                {'label': 'Team Sports/Baseball & Softball', 'value': 252},
                {'label': 'Boys (0-24 Months)/Other', 'value': 253},
                {'label': 'Tops & Blouses/Polo Shirt', 'value': 254},
                {'label': 'Sweaters/Sweatercoat', 'value': 255},
                {'label': 'Skirts/Other', 'value': 256},
                {'label': 'Coats & Jackets/Peacoat', 'value': 257},
                {'label': 'Bags and Purses/Change Purse', 'value': 258},
                {'label': 'Boys (2T-5T)/Other', 'value': 259},
                {'label': "Women's Handbags/Hobo", 'value': 260},
                {'label': 'Dresses/Other', 'value': 261},
                {'label': 'Toys/Baby & Toddler Toys', 'value': 262},
                {'label': 'Athletic Apparel/Other', 'value': 263},
                {'label': 'Bath/Bathroom Accessories', 'value': 264},
                {'label': 'Bags and Purses/Clutch', 'value': 265},
                {'label': 'Girls (2T-5T)/Other', 'value': 266},
                {'label': 'Seasonal Décor/Thanksgiving', 'value': 267},
                {'label': 'Girls (2T-5T)/Swimwear', 'value': 268},
                {'label': 'Boys (2T-5T)/One-Pieces', 'value': 269},
                {'label': 'Cameras & Photography/Digital Cameras', 'value': 270},
                {'label': 'Skin Care/Sun', 'value': 271},
                {'label': 'Bedding/Blankets & Throws', 'value': 272},
                {'label': 'TV, Audio & Surveillance/Gadgets', 'value': 273},
                {'label': 'Shoes/Mules & Clogs', 'value': 274},
                {'label': 'Nursery/Bedding', 'value': 275}
            ],
            value=4,
            className='mb-3',
        ),
        dcc.Markdown('##### ** Who will be paying for shipping costs? **'),
        dcc.RadioItems(
            id = 'shipping',
            options = [
                {'label': 'Seller', 'value': 1},
                {'label': 'Buyer', 'value': 2}
            ],
            value=1,
            labelStyle = {'margin-right': '20px'},
            className='mb-3',
        ),
        dcc.Markdown('#### ** The suggested list price for this item is: **', className='mb-2'), html.Div( id='prediction-content')
    ],
)

# column2 = dbc.Col(
#     [

#     ]
# )

layout = dbc.Row([column1])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('item-condition', 'value'), 
    Input('main-category', 'value'), 
    Input('brand-name', 'value'),
    Input('sub-category', 'value'),
    Input('shipping', 'value')])

def predict(item_condition, brand_name, main_category, sub_category, shipping):
    df = pd.DataFrame(
        columns=['item_condition', 'brand_name', 'main_category',
        'sub_category', 'shipping'],
        data=[[item_condition, brand_name, main_category, sub_category, shipping]]
    )

    pipeline = load('notebooks/pipeline_a.joblib')
    y_pred_log = pipeline.predict(df)
    y_pred = np.expm1(y_pred_log)[0]
    return dcc.Markdown(f'#### ${y_pred:.2f} dollars')