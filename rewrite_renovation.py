#!/usr/bin/env python3
"""Generate the redesigned build-your-renovation.html single-file app."""
import json

OUT = '/home/runner/work/Master/Master/build-your-renovation.html'

# ---------------------------------------------------------------------------
# DATA (mirrors original objects, enriched with premium-card metadata)
# ---------------------------------------------------------------------------

def pkg(id, name, low, high, detail, suppliers, image, brand, collection, finish, material, description,
        warranty, cleaning, country, install, availability, premium=False, recommended=False, tags=None):
    return {
        'id': id, 'name': name, 'low': low, 'high': high, 'detail': detail, 'suppliers': suppliers,
        'image': image, 'brand': brand, 'collection': collection, 'finish': finish, 'material': material,
        'description': description, 'warranty': warranty, 'cleaning': cleaning, 'country': country,
        'installNotes': install, 'availability': availability, 'premium': premium, 'recommended': recommended,
        'tags': tags or []
    }

kitchen_packages = [
    pkg('essential','Essentials',18000,28000,'Laminate benchtop, standard cabinetry',['Kaboodle','Laminex','Chef'],
        'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=800&q=80','Kaboodle','Essentials','Matt','Melamine',
        'A practical, clean-lined kitchen package with durable laminate benchtop and reliable standard cabinetry.',
        '10 years structural','Warm soapy water, no abrasive pads','Australia','Flat-pack, standard install','2–3 weeks',
        False,False,['Australian Made','Best Seller']),
    pkg('premium','Premium',35000,55000,'Engineered stone, soft-close cabinetry',['Kinsman','Caesarstone','Bosch'],
        'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800&q=80','Kinsman','Designer','Satin','2-Pack / Stone',
        'Step-up finishes with engineered stone benchtops, soft-close drawers and integrated appliances.',
        '15 years cabinetry, lifetime stone','pH-neutral cleaner','Australia / Italy','Installed by licensed trades','4–5 weeks',
        False,True,['Premium','Australian Made']),
    pkg('luxury','Luxury',65000,110000,'Premium stone, custom handles',['Freedom Kitchens','Dekton','Miele'],
        'https://images.unsplash.com/photo-1600210492493-0946911123ea?w=800&q=80','Freedom Kitchens','Bespoke','Natural','Porcelain / Timber',
        'Fully customised layout with premium stone surfaces, integrated Miele appliances and architectural hardware.',
        '25 years joinery, lifetime benchtop','Stone-safe cleaner','Italy / Australia','Custom joinery & stone install','6–8 weeks',
        True,False,['Luxury','New Arrival'])
]

kitchen_layouts = [
    {'id':'ushape','name':'U-Shape','desc':'3 walls, versatile','image':'https://images.unsplash.com/photo-1565538810643-b5bdb714032a?w=600&q=80'},
    {'id':'lshape','name':'L-Shape','desc':'2 walls, efficient','image':'https://images.unsplash.com/photo-1556911220-bff31c812dba?w=600&q=80'},
    {'id':'galley','name':'Galley','desc':'Parallel counters, narrow','image':'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80'},
    {'id':'island','name':'Island','desc':'Central prep area','image':'https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=600&q=80'}
]

door_styles = [
    {'id':'flat','name':'Flat / Slab','mod':0,'image':'https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=600&q=80','brand':'Polytec','collection':'Modern','finish':'Matt','material':'Melamine','description':'Sleek, handle-ready slab door for contemporary kitchens.','warranty':'7 years','country':'Australia'},
    {'id':'shaker','name':'Shaker','mod':600,'image':'https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=600&q=80','brand':'Hampton','collection':'Classic','finish':'Satin','material':'2-Pack','description':'Timeless recessed-panel profile that suits coastal and heritage homes.','warranty':'10 years','country':'Australia'},
    {'id':'raised','name':'Raised Panel','mod':1200,'image':'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80','brand':'Heritage','collection':'Traditional','finish':'Gloss','material':'2-Pack','description':'Ornate profile for formal, traditional kitchen schemes.','warranty':'10 years','country':'Australia'},
    {'id':'handleless','name':'Handleless','mod':1500,'image':'https://images.unsplash.com/photo-1600607687644-c7171b42498f?w=600&q=80','brand':'J-Pull','collection':'Architect','finish':'Matt','material':'Laminate','description':'Streamlined J-grip channels for a minimal European look.','warranty':'10 years','country':'Germany / Australia'}
]

cabinet_colors = [
    {'id':'white','name':'Alpine White','hex':'#F4F2ED','image':'https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=600&q=80','brand':'Polytec','collection':'Essentials','finish':'Matt','material':'Melamine','description':'Crisp warm white that brightens compact kitchens.','warranty':'7 years','country':'Australia'},
    {'id':'black','name':'Matte Black','hex':'#26282A','image':'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80','brand':'Polytec','collection':'Designer','finish':'Super Matt','material':'Melamine','description':'Dramatic matte black for bold, modern spaces.','warranty':'7 years','country':'Australia'},
    {'id':'sage','name':'Sage Green','hex':'#8A9A80','image':'https://images.unsplash.com/photo-1600210491899-8c180fff5d28?w=600&q=80','brand':'Laminex','collection':'Natural','finish':'Satin','material':'Laminate','description':'Soft sage green inspired by Australian bush tones.','warranty':'10 years','country':'Australia'},
    {'id':'navy','name':'Deep Navy','hex':'#1C2B33','image':'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80','brand':'Laminex','collection':'Designer','finish':'Satin','material':'2-Pack','description':'Rich navy that pairs beautifully with brass hardware.','warranty':'10 years','country':'Australia'},
    {'id':'oak','name':'Natural Oak','hex':'#C9A876','image':'https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=600&q=80','brand':'Egger','collection':'Woodmatt','finish':'Woodgrain','material':'Melamine','description':'Warm natural oak grain for a Scandinavian feel.','warranty':'10 years','country':'Austria'},
    {'id':'charcoal','name':'Charcoal','hex':'#4A4E52','image':'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=600&q=80','brand':'Polytec','collection':'Essentials','finish':'Matt','material':'Melamine','description':'Neutral charcoal that hides everyday wear.','warranty':'7 years','country':'Australia'}
]

benchtops = [
    {'id':'laminex','brand':'Laminex','name':'Bianco Marble','hex':'#EDEAE3','mod':0,'image':'https://images.unsplash.com/photo-1600210492493-0946911123ea?w=600&q=80','collection':'Essentials','finish':'Matt','material':'Laminate','description':'Budget-friendly marble-look laminate with easy care.','warranty':'7 years','cleaning':'Mild detergent','country':'Australia','installNotes':'Seamless join on straight runs','availability':'In stock'},
    {'id':'essastone','brand':'Essastone','name':'Georgian Bluestone','hex':'#9BA0A3','mod':1200,'image':'https://images.unsplash.com/photo-1600607687644-c7171b42498f?w=600&q=80','collection':'Earth','finish':'Honed','material':'Engineered Stone','description':'Moody blue-grey engineered stone with subtle movement.','warranty':'Lifetime','cleaning':'pH-neutral stone cleaner','country':'Australia','installNotes':'Template & install by stonemason','availability':'3–4 weeks'},
    {'id':'caesarstone','brand':'Caesarstone','name':'Calacatta Nuvo','hex':'#EDE7DD','mod':1800,'image':'https://images.unsplash.com/photo-1600566752355-35792bedcfea?w=600&q=80','collection':'Luxury','finish':'Polished','material':'Engineered Quartz','description':'Elegant white base with soft grey veining.','warranty':'Lifetime','cleaning':'Warm water & mild soap','country':'Israel / Australia','installNotes':'Professional install required','availability':'4–5 weeks','premium':True},
    {'id':'smartstone','brand':'Smartstone','name':'Symphony Grey','hex':'#B8B2A7','mod':2200,'image':'https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=600&q=80','collection':'Designer','finish':'Satin','material':'Engineered Quartz','description':'Soft greige tone with refined texture.','warranty':'Lifetime','cleaning':'pH-neutral cleaner','country':'Australia','installNotes':'Template by stonemason','availability':'3–4 weeks','premium':True},
    {'id':'dekton','brand':'Dekton','name':'Sirocco','hex':'#8C8378','mod':3200,'image':'https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=600&q=80','collection':'Ultracompact','finish':'Matte','material':'Sintered Stone','description':'Ultracompact surface: heat, scratch & UV resistant.','warranty':'25 years','cleaning':'General cleaner','country':'Spain','installNotes':'Certified installer recommended','availability':'5–6 weeks','premium':True}
]

splashbacks = [
    {'id':'ceramic','name':'Ceramic (Classic)','mod':400,'hex':'#F4F1EA','patterns':['Warm White','Ivory Gloss','Cloud Grey'],'image':'https://images.unsplash.com/photo-1581857273668-1a3b1e9b9d24?w=600&q=80','brand':'Beaumont','collection':'Classic','finish':'Gloss','material':'Ceramic','description':'Affordable gloss ceramic tiles in neutral tones.','warranty':'10 years','cleaning':'Glass cleaner on gloss','country':'Australia','installNotes':'Standard tiling','availability':'In stock'},
    {'id':'subway','name':'Subway (Timeless)','mod':0,'hex':'#F7F6F2','patterns':['Gloss White Brick','Sage Herringbone','Matte Greige'],'image':'https://images.unsplash.com/photo-1600573472556-e636f15f4605?w=600&q=80','brand':'National Tiles','collection':'Metro','finish':'Gloss / Matt','material':'Ceramic','description':'Iconic rectangular subway tile with versatile laying patterns.','warranty':'10 years','cleaning':'Mild detergent','country':'Australia','installNotes':'Brick or herringbone pattern','availability':'In stock','recommended':True},
    {'id':'mosaic','name':'Mosaic (Decorative)','mod':800,'hex':'#DCD3C2','patterns':['Stone Blend','Ocean Glass','Pearl Hex'],'image':'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=600&q=80','brand':'Signorino','collection':'Artisan','finish':'Mixed','material':'Stone / Glass','description':'Decorative mosaic feature splashback for visual impact.','warranty':'10 years','cleaning':'Soft cloth','country':'Italy','installNotes':'Feature area only','availability':'3–4 weeks','premium':True},
    {'id':'large','name':'Large Format (Luxury)','mod':1200,'hex':'#EAE6DC','patterns':['Calacatta Vein','Concrete Silk','Travertine Tone'],'image':'https://images.unsplash.com/photo-1600566752355-35792bedcfea?w=600&q=80','brand':'Artedomus','collection':'Slab','finish':'Polished / Silk','material':'Porcelain','description':'Minimal grout lines with dramatic slab-look tiles.','warranty':'10 years','cleaning':'pH-neutral cleaner','country':'Italy','installNotes':'Professional tiling, epoxy grout','availability':'4–5 weeks','premium':True}
]

microwaves = [
    {'id':'chef','brand':'Chef','mod':0,'image':'https://images.unsplash.com/photo-1584269600519-112d071b35e6?w=600&q=80','name':'Built-In Microwave','model':'CME624','material':'Stainless Steel','finish':'Brushed','description':'Reliable built-in microwave with sensor cooking.','warranty':'2 years','country':'Australia'},
    {'id':'bosch','brand':'Bosch','mod':350,'image':'https://images.unsplash.com/photo-1584622650111-883a2c6b8c91?w=600&q=80','name':'Series 4 Microwave','model':'BFL524MS0A','material':'Stainless Steel','finish':'Anti-fingerprint','description':'Quiet, efficient microwave with LED display.','warranty':'2 years','country':'Germany'},
    {'id':'miele','brand':'Miele','mod':900,'image':'https://images.unsplash.com/photo-1556912173-3db996ea0622?w=600&q=80','name':'M 7240 TC','model':'M7240TC','material':'Stainless Steel','finish':'Clean Steel','description':'German-engineered built-in microwave with automatic programmes.','warranty':'2 years','country':'Germany','premium':True}
]
ovens = [
    {'id':'westinghouse','brand':'Westinghouse','mod':0,'image':'https://images.unsplash.com/photo-1584269600519-112d071b35e6?w=600&q=80','name':'60cm Electric Oven','model':'WVE615SC','material':'Stainless Steel','finish':'Fingerprint Resistant','description':'Family-sized oven with fan-forced cooking.','warranty':'2 years','country':'Australia'},
    {'id':'fp','brand':'Fisher & Paykel','mod':600,'image':'https://images.unsplash.com/photo-1556912173-3db996ea0622?w=600&q=80','name':'60cm Built-In Oven','model':'OB60SC9DEPX3','material':'Stainless Steel','finish':'Pyrolytic','description':'Self-cleaning pyrolytic oven with 85L capacity.','warranty':'2 years','country':'New Zealand'},
    {'id':'ilve','brand':'ILVE','mod':1800,'image':'https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=600&q=80','name':'60cm Pro Series','model':'P-60N-MP','material':'Stainless Steel','finish':'Matt Black','description':'Italian-built oven with precise temperature control.','warranty':'2 years','country':'Italy','premium':True},
    {'id':'miele','brand':'Miele','mod':2600,'image':'https://images.unsplash.com/photo-1556912173-3db996ea0622?w=600&q=80','name':'H 7464 BP','model':'H7464BP','material':'Stainless Steel','finish':'Obsidian Black','description':'Miele convection oven with Moisture Plus.','warranty':'2 years','country':'Germany','premium':True}
]
cooktops = [
    {'id':'chef','brand':'Chef','mod':0,'image':'https://images.unsplash.com/photo-1574269909862-7e1d70bb807f?w=600&q=80','name':'Gas Cooktop 60cm','model':'GHC615','material':'Enamel / Cast Iron','finish':'Black','description':'Reliable four-burner gas cooktop.','warranty':'2 years','country':'Australia'},
    {'id':'bosch','brand':'Bosch','mod':500,'image':'https://images.unsplash.com/photo-1574269909862-7e1d70bb807f?w=600&q=80','name':'Series 4 Gas Cooktop','model':'PPH6A6B20A','material':'Tempered Glass','finish':'Black','description':'FlameSelect gas cooktop for precise heat control.','warranty':'2 years','country':'Germany'},
    {'id':'miele','brand':'Miele','mod':1400,'image':'https://images.unsplash.com/photo-1574269909862-7e1d70bb807f?w=600&q=80','name':'KM 7464 FL','model':'KM7464FL','material':'Ceramic Glass','finish':'Black','description':'Induction cooktop with PowerFlex cooking zone.','warranty':'2 years','country':'Germany','premium':True}
]
rangehoods = [
    {'id':'chef','brand':'Chef','mod':0,'image':'https://images.unsplash.com/photo-1584622650111-883a2c6b8c91?w=600&q=80','name':'Fixed Rangehood','model':'CRF610','material':'Stainless Steel','finish':'Silver','description':'Basic fixed rangehood with extraction or recirculation.','warranty':'2 years','country':'Australia'},
    {'id':'fp','brand':'Fisher & Paykel','mod':450,'image':'https://images.unsplash.com/photo-1584622650111-883a2c6b8c91?w=600&q=80','name':'Box Rangehood 60cm','model':'HC60BCXB2','material':'Stainless Steel','finish':'Box','description':'Powerful box-style rangehood with LED lighting.','warranty':'2 years','country':'New Zealand'},
    {'id':'miele','brand':'Miele','mod':750,'image':'https://images.unsplash.com/photo-1584622650111-883a2c6b8c91?w=600&q=80','name':'DA 6698 W','model':'DA6698W','material':'Stainless Steel','finish':'PureLine','description':'Wall-mounted chimney rangehood with silence package.','warranty':'2 years','country':'Germany','premium':True}
]

kitchen_upgrades = [
    {'id':'led','title':'LED Under-Cabinet Lighting','desc':'Ambient task lighting under wall cabinetry.','mod':1200,'image':'https://images.unsplash.com/photo-1565814329452-e1efa11c5b89?w=600&q=80','brand':'Clipsal','collection':'Iconic','finish':'Warm White','material':'LED Strip','description':'Dimmable LED strip lighting for task and ambience.','warranty':'3 years','country':'Australia','category':'lighting'},
    {'id':'utility','title':'Electrical & Plumbing Upgrade','desc':'Additional circuits and service repositioning.','mod':2400,'image':'https://images.unsplash.com/photo-1621905251189-08b45d6a269e?w=600&q=80','brand':'Licensed Trades','collection':'Trade','finish':'N/A','material':'N/A','description':'Extra power points, USB outlets, plumbing relocation and water isolation.','warranty':'6 years workmanship','country':'Australia','category':'trade'},
    {'id':'handles','title':'Premium Handles Set','desc':'Architectural brass or matte-black hardware package.','mod':800,'image':'https://images.unsplash.com/photo-1584622050111-993a426fbf0a?w=600&q=80','brand':'Hafele','collection':'Architect','finish':'Brass / Black','material':'Solid Brass','description':'Designer handles and knobs to elevate cabinetry detailing.','warranty':'10 years','country':'Germany','category':'hardware'},
    {'id':'softClose','title':'Soft-Close Drawers','desc':'Premium drawer runners and dampers.','mod':600,'image':'https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=600&q=80','brand':'Blum','collection':'Legrabox','finish':'Orion Grey','material':'Steel','description':'Full-extension soft-close drawer systems for every base cabinet.','warranty':'Lifetime','country':'Austria','category':'hardware'},
    {'id':'pantry','title':'Pantry Organisation System','desc':'Pull-out storage and modular pantry accessories.','mod':1400,'image':'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80','brand':'Hafele','collection':'Maxi','finish':'White / Chrome','material':'Steel / Plastic','description':'Pull-out baskets, spice racks and internal drawers for pantry cabinets.','warranty':'10 years','country':'Germany','category':'storage'}
]

bathroom_packages = [
    {'id':'essential','theme':'Sydney Essentials','name':'Essential Bathroom','badge':None,'low':18000,'high':26000,
     'items':['Full strip-out & re-waterproofing','Ceramic wall & floor tiles','Standard vanity','Caroma tapware, semi-frameless screen'],
     'suppliers':['Bunnings / Caroma','Beaumont Tiles','Methven Tapware'],
     'image':'https://images.unsplash.com/photo-1620626012053-cdf8b500e7ef?w=800&q=80','brand':'Caroma','collection':'Essentials','finish':'Gloss','material':'Ceramic / MFC',
     'description':'A fresh, functional bathroom renovation with quality entry-level fittings and classic white tiling.','warranty':'6 years','cleaning':'Mild bathroom cleaner','country':'Australia','installNotes':'Standard wet-area re-sheet & waterproof','availability':'3–4 weeks','premium':False,'recommended':False,'tags':['Best Seller']},
    {'id':'premium','theme':'Sydney Premium','name':'Premium Bathroom','badge':'MOST POPULAR','low':28000,'high':45000,
     'items':['Full strip-out & re-waterproofing','Large-format porcelain tiles','Floating vanity','Phoenix tapware, frameless screen'],
     'suppliers':['Reece','National Tiles','Phoenix Tapware'],
     'image':'https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=800&q=80','brand':'Phoenix','collection':'Designer','finish':'Matt / Chrome','material':'Porcelain / Stone-look',
     'description':'Modern floating vanity, large-format tiles and sleek frameless shower screen.','warranty':'10 years','cleaning':'pH-neutral bathroom cleaner','country':'Australia','installNotes':'Full strip-out with screed if required','availability':'4–5 weeks','premium':False,'recommended':True,'tags':['Premium','Most Popular']},
    {'id':'luxury','theme':'Sydney Signature','name':'Luxury Bathroom','badge':'FULL CUSTOM','low':50000,'high':80000,
     'items':['Full strip-out, re-waterproof & re-plumb','Natural stone-look porcelain','Freestanding bath','Brushed brass/black tapware, LED mirror'],
     'suppliers':['Custom Joinery','Signorino / Artedomus','Nero / Sussex Taps'],
     'image':'https://images.unsplash.com/photo-1584622050111-993a426fbf0a?w=800&q=80','brand':'Nero / Sussex','collection':'Bespoke','finish':'Brushed Brass','material':'Stone-look Porcelain / Solid Brass',
     'description':'Resort-style bathroom with freestanding bath, brushed brass tapware and custom joinery.','warranty':'15 years','cleaning':'Stone-safe cleaner','country':'Italy / Australia','installNotes':'Custom joinery & stone install','availability':'6–8 weeks','premium':True,'recommended':False,'tags':['Luxury','New Arrival']}
]

vanity_styles = [
    {'id':'wallhung','name':'Wall-Hung','mod':0,'image':'https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=600&q=80','brand':'Custom','collection':'Modern','finish':'Satin','material':'MFC / Stone','description':'Floating vanity creates a sense of space and easy cleaning.','warranty':'10 years','country':'Australia'},
    {'id':'freestanding','name':'Freestanding','mod':900,'image':'https://images.unsplash.com/photo-1620626012053-cdf8b500e7ef?w=600&q=80','brand':'Custom','collection':'Traditional','finish':'Matt','material':'Timber / MFC','description':'Leg-mounted vanity with classic detailing and ample storage.','warranty':'10 years','country':'Australia'},
    {'id':'timber','name':'Timber Vanity','mod':1400,'image':'https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=600&q=80','brand':'Custom','collection':'Organic','finish':'Oiled','material':'Solid Timber','description':'Natural timber vanity for warmth and texture.','warranty':'10 years','country':'Australia','premium':True}
]
vanity_colors = [
    {'id':'white','name':'Matte White','hex':'#F4F2ED','image':'https://images.unsplash.com/photo-1620626012053-cdf8b500e7ef?w=600&q=80','brand':'Laminex','collection':'Essentials','finish':'Matt','material':'MFC','description':'Clean white vanity finish.','warranty':'7 years','country':'Australia'},
    {'id':'oak','name':'Natural Oak','hex':'#C9A876','image':'https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=600&q=80','brand':'Egger','collection':'Woodmatt','finish':'Woodgrain','material':'MFC','description':'Warm oak vanity finish.','warranty':'10 years','country':'Austria'},
    {'id':'black','name':'Matte Black','hex':'#26282A','image':'https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=600&q=80','brand':'Laminex','collection':'Designer','finish':'Super Matt','material':'MFC','description':'Bold black vanity finish.','warranty':'10 years','country':'Australia'},
    {'id':'sage','name':'Sage Green','hex':'#8A9A80','image':'https://images.unsplash.com/photo-1600210491899-8c180fff5d28?w=600&q=80','brand':'Laminex','collection':'Natural','finish':'Satin','material':'MFC','description':'Soft sage vanity finish.','warranty':'10 years','country':'Australia'}
]
floor_tiles = [
    {'id':'subway','name':'Matte Porcelain — Grey','hex':'#D8D2C4','image':'https://images.unsplash.com/photo-1600573472556-e636f15f4605?w=600&q=80','brand':'National Tiles','collection':'Concrete','finish':'Matt','material':'Porcelain','description':'Hard-wearing grey porcelain floor tile.','warranty':'10 years','country':'Australia'},
    {'id':'stone','name':'Stone-Look Porcelain','hex':'#C8C2B4','image':'https://images.unsplash.com/photo-1600566752355-35792bedcfea?w=600&q=80','brand':'Beaumont','collection':'Pietra','finish':'Matt','material':'Porcelain','description':'Natural stone-look porcelain for a seamless floor.','warranty':'10 years','country':'Italy'},
    {'id':'terrazzo','name':'Terrazzo Blend','hex':'#DCD3C2','image':'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=600&q=80','brand':'Signorino','collection':'Terrazzo','finish':'Honed','material':'Porcelain','description':'Playful terrazzo pattern for feature floors.','warranty':'10 years','country':'Italy','premium':True},
    {'id':'charcoal','name':'Charcoal Matte','hex':'#3A3D40','image':'https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=600&q=80','brand':'National Tiles','collection':'Dark','finish':'Matt','material':'Porcelain','description':'Dramatic charcoal floor tile.','warranty':'10 years','country':'Australia'}
]
wall_tiles = [
    {'id':'subway','name':'Subway Tile — White','hex':'#F7F6F2','image':'https://images.unsplash.com/photo-1600573472556-e636f15f4605?w=600&q=80','brand':'Beaumont','collection':'Metro','finish':'Gloss','material':'Ceramic','description':'Classic white subway wall tile.','warranty':'10 years','country':'Australia'},
    {'id':'marble','name':'Marble-Look Large Format','hex':'#EAE6DC','image':'https://images.unsplash.com/photo-1600566752355-35792bedcfea?w=600&q=80','brand':'National Tiles','collection':'Marble','finish':'Polished','material':'Porcelain','description':'Large-format marble-look wall tile.','warranty':'10 years','country':'Italy'},
    {'id':'terrazzo','name':'Terrazzo Blend','hex':'#DCD3C2','image':'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=600&q=80','brand':'Signorino','collection':'Terrazzo','finish':'Honed','material':'Porcelain','description':'Terrazzo-look wall tile.','warranty':'10 years','country':'Italy','premium':True},
    {'id':'black','name':'Matte Black Large Format','hex':'#2B2C2E','image':'https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=600&q=80','brand':'Artedomus','collection':'Dark','finish':'Matt','material':'Porcelain','description':'Bold black large-format wall tile.','warranty':'10 years','country':'Italy','premium':True}
]
tapware = [
    {'id':'chrome','brand':'Caroma','name':'Chrome','hex':'#C7CBCE','mod':0,'image':'https://images.unsplash.com/photo-1584622050111-993a426fbf0a?w=600&q=80','model':'Luna','material':'Brass / Chrome','finish':'Polished Chrome','description':'Classic polished chrome tapware with 5-star WELS rating.','warranty':'7 years','country':'Australia'},
    {'id':'black','brand':'Nero','name':'Matte Black','hex':'#26282A','mod':250,'image':'https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=600&q=80','model':'Mecca','material':'Brass','finish':'Matte Black','description':'Trending matte black tapware with clean lines.','warranty':'10 years','country':'Australia'},
    {'id':'brass','brand':'Sussex','name':'Brushed Brass','hex':'#C9A24B','mod':350,'image':'https://images.unsplash.com/photo-1584622050111-993a426fbf0a?w=600&q=80','model':'Scala','material':'Solid Brass','finish':'Brushed Brass','description':'Warm brushed brass tapware for luxury bathrooms.','warranty':'15 years','country':'Australia','premium':True},
    {'id':'nickel','brand':'Phoenix','name':'Brushed Nickel','hex':'#A9ACAE','mod':300,'image':'https://images.unsplash.com/photo-1584622050111-993a426fbf0a?w=600&q=80','model':'Vivid','material':'Brass','finish':'Brushed Nickel','description':'Subtle brushed nickel with fingerprint resistance.','warranty':'10 years','country':'Australia'}
]
shower_screens = [
    {'id':'framed','name':'Framed','mod':0,'image':'https://images.unsplash.com/photo-1620626012053-cdf8b500e7ef?w=600&q=80','brand':'Bunnings','collection':'Standard','finish':'Chrome','material':'Aluminium / Glass','description':'Durable framed shower screen with clear glass.','warranty':'5 years','country':'Australia'},
    {'id':'semi','name':'Semi-Frameless','mod':400,'image':'https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=600&q=80','brand':'Reece','collection':'Designer','finish':'Chrome / Black','material':'Stainless Steel / Glass','description':'Semi-frameless screen for a modern look.','warranty':'10 years','country':'Australia'},
    {'id':'frameless','name':'Frameless','mod':900,'image':'https://images.unsplash.com/photo-1584622050111-993a426fbf0a?w=600&q=80','brand':'Reece','collection':'Luxury','finish':'Chrome / Black','material':'Tempered Glass','description':'Minimal frameless glass for a spacious feel.','warranty':'10 years','country':'Australia','premium':True}
]

# ---------------------------------------------------------------------------
# Helpers to generate JS arrays
# ---------------------------------------------------------------------------
def js_array(name, items):
    return f"const {name} = {json.dumps(items, ensure_ascii=False)};\n"

js_data = ""
js_data += js_array('kitchenPackages', kitchen_packages)
js_data += js_array('kitchenLayouts', kitchen_layouts)
js_data += js_array('doorStyles', door_styles)
js_data += js_array('cabinetColors', cabinet_colors)
js_data += js_array('benchtops', benchtops)
js_data += js_array('splashbacks', splashbacks)
js_data += js_array('microwaves', microwaves)
js_data += js_array('ovens', ovens)
js_data += js_array('cooktops', cooktops)
js_data += js_array('rangehoods', rangehoods)
js_data += js_array('kitchenUpgradeOptions', kitchen_upgrades)
js_data += js_array('bathroomPackages', bathroom_packages)
js_data += js_array('vanityStyles', vanity_styles)
js_data += js_array('vanityColors', vanity_colors)
js_data += js_array('floorTiles', floor_tiles)
js_data += js_array('wallTiles', wall_tiles)
js_data += js_array('tapware', tapware)
js_data += js_array('showerScreens', shower_screens)

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
CSS = r'''
:root{
  --navy:#15171A; --navy-2:#233933;
  --gold:#A9812F; --gold-dark:#8a6a26; --gold-light:#C9A24B;
  --off:#EFEAE1; --gray:#3A3F44; --line:#E1D9C8;
  --sage:#2F4A42; --cream:#FAF8F3;
  --white:#FFFFFF; --text-primary:#1A1D21; --text-secondary:#5C626A;
  --border:#E8E4DB;
  --shadow-sm:0 2px 8px rgba(21,23,26,.06);
  --shadow-md:0 8px 24px rgba(21,23,26,.10);
  --shadow-lg:0 18px 48px rgba(21,23,26,.14);
  --radius-sm:10px; --radius-md:16px; --radius-lg:24px;
  --transition:all .22s cubic-bezier(.25,.46,.45,.94);
  --focus-ring:0 0 0 3px rgba(169,129,47,.35);
}
*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{margin:0;font-family:'Work Sans','Segoe UI',Arial,sans-serif;background:var(--off);color:var(--gray);font-size:15px;line-height:1.55;}
img{max-width:100%;height:auto;display:block;}
button{font:inherit;cursor:pointer;}

/* Header */
.site-header{background:var(--navy);color:#fff;padding:16px 24px;position:sticky;top:0;z-index:100;box-shadow:var(--shadow-sm);}
.header-inner{max-width:1400px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;}
.brand img{height:34px;filter:brightness(0) invert(1);}
.brand-text h1{font-family:'Fraunces',Georgia,serif;font-size:20px;margin:0;font-weight:600;color:#fff;}
.brand-text span{font-size:11px;color:var(--gold);letter-spacing:1.2px;text-transform:uppercase;}
.header-actions{display:flex;align-items:center;gap:10px;}
.btn-pill{min-height:44px;display:inline-flex;align-items:center;justify-content:center;padding:10px 20px;border-radius:999px;border:1.5px solid rgba(255,255,255,.35);background:transparent;color:#ece5d6;font-weight:600;font-size:13px;text-decoration:none;transition:var(--transition);}
.btn-pill:hover{border-color:var(--gold);color:var(--gold);}
.btn-pill-primary{background:linear-gradient(120deg,var(--gold),var(--gold-dark));border-color:var(--gold-dark);color:#fff;box-shadow:var(--shadow-sm);}
.btn-pill-primary:hover{filter:brightness(1.08);transform:translateY(-1px);}

/* Wrap & tabs */
.wrap{max-width:1400px;margin:0 auto;padding:28px 20px 80px;}
.tabs{display:flex;gap:12px;margin-bottom:28px;}
.tab{flex:1;text-align:center;padding:16px 14px;background:var(--cream);border:1.5px solid var(--border);border-radius:var(--radius-md);cursor:pointer;font-weight:700;font-size:15px;min-height:52px;display:flex;align-items:center;justify-content:center;transition:var(--transition);}
.tab:hover{border-color:var(--gold);transform:translateY(-2px);}
.tab.active{background:var(--navy);color:#fff;border-color:var(--navy);box-shadow:var(--shadow-md);}

/* Wizard layout */
.wizard-layout{display:grid;grid-template-columns:260px minmax(0,1fr) 360px;gap:24px;align-items:start;}
@media(max-width:1199px){.wizard-layout{grid-template-columns:1fr;}}

/* Sidebar */
.wizard-sidebar{position:sticky;top:86px;background:var(--cream);border:1.5px solid var(--border);border-radius:var(--radius-md);padding:22px;box-shadow:var(--shadow-sm);}
.wizard-sidebar h2{margin:0 0 18px;color:var(--navy);font-family:'Fraunces',Georgia,serif;font-size:22px;line-height:1.2;}
.steps-list{display:flex;flex-direction:column;gap:8px;}
.step-item{display:flex;gap:12px;padding:12px;border:1.5px solid transparent;border-radius:var(--radius-sm);cursor:pointer;transition:var(--transition);}
.step-item:hover{border-color:var(--gold);background:#fff;box-shadow:var(--shadow-sm);}
.step-item.active{background:#fff7e7;border-color:var(--gold);box-shadow:var(--shadow-sm);}
.step-item.completed{background:#f7f6f1;}
.step-index{width:30px;height:30px;flex:0 0 30px;border-radius:50%;border:1.5px solid var(--line);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:var(--navy);background:#fff;}
.step-item.active .step-index,.step-item.completed .step-index{border-color:var(--gold);background:var(--gold);color:#fff;}
.step-meta strong{display:block;color:var(--navy);font-size:13.5px;margin-bottom:2px;}
.step-meta span{display:block;font-size:12px;color:var(--text-secondary);line-height:1.35;}

/* Stage */
.wizard-stage{background:var(--white);border:1.5px solid var(--border);border-radius:var(--radius-md);padding:26px;box-shadow:var(--shadow-sm);min-width:0;}
.step-head{display:flex;justify-content:space-between;align-items:flex-start;gap:16px;margin-bottom:22px;}
.step-head h3{margin:0;color:var(--navy);font-family:'Fraunces',Georgia,serif;font-size:26px;}
.step-head p{margin:8px 0 0;color:var(--text-secondary);font-size:14px;line-height:1.5;max-width:680px;}
.completed-badge{border:1.5px solid #7da281;color:var(--sage);background:#edf7ee;border-radius:999px;font-size:11px;font-weight:700;letter-spacing:.4px;padding:6px 12px;text-transform:uppercase;white-space:nowrap;}

/* Search / filter */
.sf-bar{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-bottom:18px;padding:14px;background:var(--cream);border:1.5px solid var(--border);border-radius:var(--radius-sm);}
.sf-search{flex:1 1 220px;min-width:220px;min-height:44px;padding:10px 14px;border:1.5px solid var(--border);border-radius:999px;background:#fff;font-size:14px;}
.sf-search:focus{outline:none;border-color:var(--gold);box-shadow:var(--focus-ring);}
.sf-filters{display:flex;flex-wrap:wrap;gap:8px;}
.sf-chip{min-height:36px;padding:8px 14px;border-radius:999px;border:1.5px solid var(--border);background:#fff;color:var(--text-secondary);font-size:12px;font-weight:600;cursor:pointer;transition:var(--transition);}
.sf-chip:hover{border-color:var(--gold);color:var(--navy);}
.sf-chip.active{background:var(--navy);color:#fff;border-color:var(--navy);}

/* Product cards */
.cards-grid{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));}
.cards-grid.cols-2{grid-template-columns:repeat(2,minmax(0,1fr));}
.cards-grid.cols-3{grid-template-columns:repeat(3,minmax(0,1fr));}
@media(max-width:767px){.cards-grid,.cards-grid.cols-2,.cards-grid.cols-3{grid-template-columns:1fr;}}

.product-card{position:relative;border:1.5px solid var(--border);background:var(--cream);border-radius:var(--radius-md);overflow:hidden;cursor:pointer;transition:var(--transition);display:flex;flex-direction:column;}
.product-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:var(--gold-light);}
.product-card.selected{border-color:var(--gold);box-shadow:0 0 0 1px rgba(169,129,47,.5) inset,0 8px 28px rgba(169,129,47,.18);background:linear-gradient(145deg,#fffaf1,#f7edd8);}
.product-card:focus-visible{outline:none;box-shadow:var(--focus-ring);}
.card-badges{position:absolute;top:12px;left:12px;z-index:2;display:flex;flex-wrap:wrap;gap:6px;}
.badge{font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.5px;padding:5px 9px;border-radius:999px;color:#fff;}
.badge-premium{background:linear-gradient(120deg,#B88A3D,var(--gold-dark));}
.badge-recommended{background:var(--sage);}
.badge-selected{background:var(--navy);}
.card-media{position:relative;margin:0;width:100%;aspect-ratio:4/3;overflow:hidden;background:#e8e4db;}
.card-media img{width:100%;height:100%;object-fit:cover;transition:transform .5s ease;}
.product-card:hover .card-media img{transform:scale(1.06);}
.gallery-trigger{position:absolute;bottom:10px;right:10px;width:34px;height:34px;border-radius:50%;border:none;background:rgba(21,23,26,.72);color:#fff;display:flex;align-items:center;justify-content:center;font-size:16px;opacity:0;transform:translateY(6px);transition:var(--transition);}
.product-card:hover .gallery-trigger{opacity:1;transform:translateY(0);}
.gallery-trigger:hover{background:var(--gold);}
.card-body{padding:16px;flex:1;display:flex;flex-direction:column;}
.card-meta{display:flex;flex-wrap:wrap;gap:6px 10px;margin-bottom:6px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;color:var(--gold-dark);}
.card-title{margin:0 0 6px;color:var(--navy);font-family:'Fraunces',Georgia,serif;font-size:16px;font-weight:600;}
.card-desc{margin:0 0 10px;font-size:12.5px;color:var(--text-secondary);line-height:1.45;flex:1;}
.card-specs{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px;}
.card-specs span{font-size:11px;background:var(--off);border:1px solid var(--border);padding:4px 8px;border-radius:999px;color:#6b6555;}
.card-price{margin-top:auto;font-size:14px;font-weight:700;color:var(--navy);}
.card-price.positive{color:var(--gold-dark);}
.card-suppliers{display:flex;flex-wrap:wrap;gap:5px;margin-top:10px;}
.card-suppliers span{font-size:10px;border:1px solid var(--border);border-radius:999px;padding:3px 8px;background:#f8f4eb;color:#6c6351;}

/* Layout card */
.layout-icon{background:var(--off);border-radius:var(--radius-sm);padding:14px;margin-bottom:10px;}
.layout-icon svg{width:100%;height:70px;display:block;}

/* Colour swatch */
.color-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:14px;}
.color-card{position:relative;border:1.5px solid var(--border);border-radius:var(--radius-md);padding:12px;background:var(--cream);cursor:pointer;transition:var(--transition);}
.color-card:hover{border-color:var(--gold-light);transform:translateY(-3px);box-shadow:var(--shadow-sm);}
.color-card.selected{border-color:var(--gold);box-shadow:0 0 0 1px rgba(169,129,47,.5) inset,0 6px 18px rgba(169,129,47,.14);}
.color-swatch{width:100%;aspect-ratio:1;border-radius:var(--radius-sm);margin-bottom:10px;border:1px solid rgba(0,0,0,.08);position:relative;}
.color-card.selected .color-swatch::after{content:"✓";position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:22px;color:#fff;text-shadow:0 1px 3px rgba(0,0,0,.4);}
.color-card h4{margin:0 0 2px;font-size:14px;color:var(--navy);}
.color-card span{font-size:11px;color:var(--text-secondary);}

/* Stepper box */
.stepper-box{border:1.5px solid var(--border);background:var(--cream);border-radius:var(--radius-md);padding:18px;}
.stepper-box h5{margin:0 0 12px;color:var(--navy);font-size:13px;text-transform:uppercase;letter-spacing:.45px;}
.stepper{display:flex;align-items:center;gap:10px;}
.stepper button{width:48px;height:48px;border-radius:var(--radius-sm);border:1.5px solid var(--border);background:#fff;color:var(--navy);font-size:24px;cursor:pointer;line-height:1;transition:var(--transition);}
.stepper button:hover{border-color:var(--gold);background:#fff8ea;}
.stepper button:active{transform:scale(.95);}
.stepper span{font-size:24px;font-weight:700;color:var(--navy);width:48px;text-align:center;}
.stepper-mod{margin-top:10px;font-size:13px;font-weight:700;color:var(--gold-dark);}

/* Toggle cards */
.toggle-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;}
@media(max-width:767px){.toggle-grid{grid-template-columns:1fr;}}
.toggle-card{display:flex;justify-content:space-between;gap:14px;align-items:center;border:1.5px solid var(--border);background:var(--cream);border-radius:var(--radius-md);padding:16px;cursor:pointer;transition:var(--transition);}
.toggle-card:hover{border-color:var(--gold-light);box-shadow:var(--shadow-sm);}
.toggle-card.on{border-color:var(--gold);background:#fff8ea;}
.toggle-card h4{margin:0 0 4px;color:var(--navy);font-size:15px;}
.toggle-card p{margin:0;color:var(--text-secondary);font-size:13px;}
.toggle-check{width:28px;height:28px;border-radius:50%;border:2px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:16px;color:#fff;background:#d3c7ae;transition:var(--transition);flex-shrink:0;}
.toggle-card.on .toggle-check{border-color:var(--gold);background:var(--gold);}

/* Preview panel */
.wizard-preview{position:relative;}
.preview-panel{position:sticky;top:86px;background:var(--white);border:1.5px solid var(--border);border-radius:var(--radius-md);padding:20px;box-shadow:var(--shadow-sm);display:flex;flex-direction:column;gap:18px;}
.preview-header{display:flex;justify-content:space-between;align-items:center;}
.preview-header h4{margin:0;font-family:'Fraunces',Georgia,serif;font-size:18px;color:var(--navy);}
.view-toggle{display:flex;gap:8px;background:var(--cream);padding:4px;border-radius:999px;border:1.5px solid var(--border);}
.view-toggle button{flex:1;padding:8px 14px;border-radius:999px;border:none;background:transparent;color:var(--text-secondary);font-weight:700;font-size:12px;cursor:pointer;transition:var(--transition);}
.view-toggle button.active{background:var(--navy);color:#fff;}
.preview-frame{background:#f2efe8;border-radius:var(--radius-sm);overflow:hidden;border:1.5px solid var(--border);min-height:220px;}
.preview-frame svg{display:block;width:100%;height:auto;}
.preview-note{font-size:11px;color:var(--text-secondary);line-height:1.5;margin-top:-8px;}

/* Product info panel */
.info-panel{border:1.5px solid var(--border);border-radius:var(--radius-md);padding:16px;background:var(--cream);}
.info-panel h5{margin:0 0 10px;font-family:'Fraunces',Georgia,serif;font-size:15px;color:var(--navy);display:flex;align-items:center;gap:8px;}
.info-panel h5::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--gold);}
.info-empty{text-align:center;color:var(--text-secondary);font-size:13px;padding:14px;}
.info-media{border-radius:var(--radius-sm);overflow:hidden;margin-bottom:12px;aspect-ratio:16/10;background:#e8e4db;}
.info-media img{width:100%;height:100%;object-fit:cover;}
.info-title{margin:0 0 2px;font-size:16px;font-weight:700;color:var(--navy);}
.info-sub{margin:0 0 10px;font-size:12px;color:var(--gold-dark);font-weight:700;text-transform:uppercase;letter-spacing:.5px;}
.info-desc{font-size:13px;color:var(--text-secondary);line-height:1.5;margin-bottom:12px;}
.info-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px 12px;font-size:12px;margin-bottom:12px;}
.info-grid div{display:flex;flex-direction:column;}
.info-grid dt{color:var(--text-secondary);font-size:11px;text-transform:uppercase;letter-spacing:.4px;}
.info-grid dd{margin:2px 0 0;color:var(--navy);font-weight:600;}
.info-cost{font-size:14px;font-weight:700;color:var(--navy);padding-top:10px;border-top:1px solid var(--border);}

/* Summary panel */
.summary-panel{border:1.5px solid var(--border);border-radius:var(--radius-md);padding:16px;background:var(--navy);color:#fff;}
.summary-panel h5{margin:0 0 12px;font-family:'Fraunces',Georgia,serif;font-size:16px;color:var(--gold);}
.summary-line{display:flex;justify-content:space-between;font-size:12px;padding:6px 0;border-bottom:1px solid rgba(255,255,255,.12);color:#dcd9d2;}
.summary-line span:last-child{color:#fff;font-weight:600;}
.summary-total{font-size:24px;font-weight:700;margin:12px 0 4px;color:#fff;}
.summary-meta{font-size:11px;color:#a9a49a;line-height:1.6;}
.summary-products{max-height:140px;overflow:auto;margin:8px 0;padding-right:4px;}
.summary-products li{font-size:12px;color:#ece5d6;margin-bottom:4px;}

/* Running total */
.running-total{margin-top:18px;background:var(--navy);color:#fff;padding:12px 16px;border-radius:var(--radius-sm);font-size:14px;font-weight:600;display:flex;justify-content:space-between;align-items:center;}
.running-total .amount{font-size:22px;animation:pricePop .24s ease;}
@keyframes pricePop{0%{transform:scale(.95);}55%{transform:scale(1.05);}100%{transform:scale(1);}}

/* Step actions */
.step-actions{margin-top:24px;display:flex;justify-content:space-between;gap:12px;}
.nav-btn{min-height:48px;display:inline-flex;align-items:center;justify-content:center;padding:12px 22px;border-radius:999px;border:1.5px solid var(--border);background:#fff;color:var(--navy);font-size:14px;font-weight:700;cursor:pointer;text-decoration:none;transition:var(--transition);position:relative;overflow:hidden;}
.nav-btn:hover:not(:disabled){border-color:var(--gold);background:#fff8ea;}
.nav-btn.primary{background:linear-gradient(120deg,var(--gold),var(--gold-dark));border-color:var(--gold-dark);color:#fff;box-shadow:var(--shadow-sm);}
.nav-btn.primary:hover:not(:disabled){filter:brightness(1.08);transform:translateY(-1px);}
.nav-btn:disabled{opacity:.45;cursor:not-allowed;}

/* Review step */
.review-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:20px;}
.review-summary{background:var(--cream);border:1.5px solid var(--border);border-radius:var(--radius-md);padding:16px;}
.review-summary pre{margin:0;font-family:'Work Sans','Segoe UI',Arial,sans-serif;font-size:12.5px;line-height:1.65;color:#4b463d;white-space:pre-wrap;}
.price-breakdown{border:1.5px solid var(--border);background:var(--cream);border-radius:var(--radius-md);padding:16px;}
.price-breakdown .line{display:flex;justify-content:space-between;border-bottom:1px solid #e9dfca;padding:8px 0;font-size:13px;color:#524a3f;}
.price-breakdown .line strong{font-size:14px;color:var(--navy);}
.request-btn{width:100%;margin-top:12px;}

/* Modal base */
.modal{position:fixed;inset:0;background:rgba(21,23,26,.72);display:none;align-items:center;justify-content:center;padding:20px;z-index:500;}
.modal.open,.modal.show{display:flex;}
.modal-card{width:min(100%,720px);background:var(--cream);border-radius:var(--radius-md);padding:24px;position:relative;box-shadow:var(--shadow-lg);max-height:90vh;overflow:auto;}
.modal-card h3{margin:0 0 8px;font-family:'Fraunces',Georgia,serif;color:var(--navy);font-size:24px;}
.modal-close{position:absolute;right:14px;top:14px;border:1.5px solid var(--border);background:#fff;border-radius:var(--radius-sm);width:38px;height:38px;cursor:pointer;color:var(--navy);font-size:18px;transition:var(--transition);}
.modal-close:hover{border-color:var(--gold);color:var(--gold);}

/* Quote modal */
.quote-modal-card{width:min(100%,460px);}
.quote-modal-card p{margin:0 0 16px;font-size:13px;color:#6b6555;line-height:1.6;}
.quote-modal-card label{display:block;font-size:11px;font-weight:700;color:#7a7460;text-transform:uppercase;letter-spacing:.5px;margin:14px 0 6px;}
.quote-modal-card input{width:100%;padding:12px;border:1.5px solid var(--border);border-radius:var(--radius-sm);font:inherit;background:#fff;color:var(--gray);}
.quote-modal-card input:focus{outline:none;border-color:var(--gold);box-shadow:var(--focus-ring);}
.quote-status{min-height:18px;margin-top:14px;font-size:13px;color:var(--sage);}
.quote-status.error{color:#9b2c2c;}
.modal-actions{display:flex;gap:10px;justify-content:flex-end;margin-top:20px;}
.modal-actions button{border:none;border-radius:999px;padding:12px 22px;font:inherit;font-weight:700;cursor:pointer;min-height:44px;}
.btn-secondary{background:#e8e0d0;color:var(--navy);}
.btn-primary{background:var(--navy);color:#fff;}
.btn-primary:disabled{opacity:.7;cursor:wait;}

/* Gallery modal */
.gallery-modal-card{width:min(100%,900px);padding:0;background:var(--navy);color:#fff;border-radius:var(--radius-md);overflow:hidden;}
.gallery-main{position:relative;background:#111;}
.gallery-main img{width:100%;max-height:60vh;object-fit:contain;display:block;}
.gallery-thumb-row{display:flex;gap:10px;padding:14px;overflow:auto;background:#1c1f24;}
.gallery-thumb{width:72px;height:54px;object-fit:cover;border-radius:6px;border:2px solid transparent;cursor:pointer;opacity:.7;transition:var(--transition);}
.gallery-thumb:hover,.gallery-thumb.active{opacity:1;border-color:var(--gold);}
.gallery-info{padding:16px 20px;background:var(--cream);color:var(--gray);}
.gallery-info h4{margin:0 0 4px;color:var(--navy);font-family:'Fraunces',Georgia,serif;}
.gallery-caption{font-size:13px;color:var(--text-secondary);margin:0;}
.gallery-nav{position:absolute;top:50%;transform:translateY(-50%);width:44px;height:44px;border-radius:50%;border:none;background:rgba(255,255,255,.15);color:#fff;font-size:20px;cursor:pointer;backdrop-filter:blur(4px);}
.gallery-nav:hover{background:rgba(255,255,255,.3);}
.gallery-nav.prev{left:14px;}
.gallery-nav.next{right:14px;}

/* Footer */
.site-footer{background:var(--navy);color:#c9c2b3;padding:48px 20px 26px;margin-top:30px;}
.footer-inner{max-width:1400px;margin:0 auto;display:flex;justify-content:space-between;flex-wrap:wrap;gap:20px;align-items:center;}
.footer-inner img{height:34px;filter:brightness(0) invert(1);margin-bottom:10px;}
.footer-inner p{font-size:12.5px;color:#a89f8e;max-width:360px;margin:0;}
.footer-links{font-size:13px;display:flex;gap:12px;flex-wrap:wrap;}
.footer-links a{color:#ece5d6;text-decoration:none;}
.footer-links a:hover{color:var(--gold);}

/* WhatsApp */
.whatsapp-btn{position:fixed;bottom:26px;right:26px;z-index:250;background:#25D366;color:#fff;width:58px;height:58px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:26px;box-shadow:var(--shadow-md);transition:var(--transition);text-decoration:none;}
.whatsapp-btn:hover{transform:scale(1.08);}

/* Disclaimer */
.disclaimer{font-size:11px;color:#8a8478;line-height:1.65;max-width:1400px;margin:30px auto 0;padding:0 20px;}

/* Animations */
@keyframes fadeIn{from{opacity:0;transform:translateY(8px);}to{opacity:1;transform:translateY(0);}}
.fade-in{animation:fadeIn .35s ease both;}

/* Ripple */
.ripple{position:absolute;border-radius:50%;transform:scale(0);animation:ripple .55s linear;background:rgba(255,255,255,.35);pointer-events:none;}
@keyframes ripple{to{transform:scale(4);opacity:0;}}

/* Mobile bottom nav */
@media(max-width:1199px){
  .wizard-sidebar{position:static;}
  .wizard-preview{order:-1;}
  .preview-panel{position:static;display:grid;grid-template-columns:1fr 1fr;gap:16px;}
  .preview-frame{grid-column:1 / -1;}
  .info-panel{grid-column:1 / -1;}
  .summary-panel{grid-column:1 / -1;}
  .steps-list{flex-direction:row;overflow:auto;padding-bottom:4px;}
  .step-item{min-width:200px;}
}
@media(max-width:767px){
  .preview-panel{display:flex;}
  .site-header{padding:14px 16px;}
  .brand-text h1{font-size:17px;}
  .wizard-stage{padding:18px;}
  .step-head h3{font-size:22px;}
  .step-actions{position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1.5px solid var(--border);padding:12px 16px;z-index:90;box-shadow:0 -4px 18px rgba(21,23,26,.08);margin:0;}
  .wrap{padding-bottom:110px;}
  .cards-grid{gap:14px;}
  .sf-bar{flex-direction:column;align-items:stretch;}
  .review-grid{grid-template-columns:1fr;}
}
@media(max-width:480px){
  .tabs{flex-direction:column;}
  .product-card{flex-direction:row;align-items:stretch;}
  .product-card .card-media{width:120px;flex-shrink:0;aspect-ratio:1;}
  .product-card .card-body{padding:12px;}
  .color-grid{grid-template-columns:repeat(2,1fr);}
}
'''

# ---------------------------------------------------------------------------
# Body HTML (static structure)
# ---------------------------------------------------------------------------
BODY_HTML = r'''
<header class="site-header">
  <div class="header-inner">
    <a href="index.html" class="brand" aria-label="MIC NSW home">
      <img src="https://mic-nsw.com.au/front/images/logo2.png" alt="MIC NSW">
      <div class="brand-text">
        <h1>Kitchen & Bathroom Design Studio</h1>
        <span>Packages · 2D/3D Live Preview · Sydney Suppliers</span>
      </div>
    </a>
    <div class="header-actions">
      <a href="index.html" class="btn-pill">← Back to MIC NSW</a>
      <a href="index.html#contact" class="btn-pill btn-pill-primary">Get a Quote</a>
    </div>
  </div>
</header>

<main class="wrap">
  <nav class="tabs" role="tablist" aria-label="Renovation type">
    <div class="tab active" role="tab" aria-selected="true" tabindex="0" data-tab="kitchen">Kitchen Renovation</div>
    <div class="tab" role="tab" aria-selected="false" tabindex="0" data-tab="bathroom">Bathroom Renovation</div>
  </nav>

  <!-- ============ KITCHEN ============ -->
  <section id="kitchen-tab" aria-label="Kitchen renovation configurator">
    <div class="wizard-layout" id="kitchenWizard">
      <aside class="wizard-sidebar" aria-label="Kitchen design steps">
        <h2>Design Your Kitchen</h2>
        <div id="kitchenStepsList" class="steps-list"></div>
        <div id="kitchenRunningTotal" class="running-total" style="display:none;" aria-live="polite"></div>
      </aside>

      <section class="wizard-stage">
        <div id="kitchenStepContent" class="step-content fade-in" aria-live="polite"></div>
        <div class="step-actions">
          <button id="kitchenBackBtn" class="nav-btn" type="button" aria-label="Go to previous step">← Back</button>
          <button id="kitchenNextBtn" class="nav-btn primary" type="button" aria-label="Go to next step">Next →</button>
        </div>
      </section>

      <aside class="wizard-preview" aria-label="Kitchen live preview and summary">
        <div class="preview-panel">
          <div class="preview-header">
            <h4>Live Preview</h4>
            <div class="view-toggle" role="group" aria-label="Preview view">
              <button type="button" class="active" data-kview="2d" aria-pressed="true">2D Plan</button>
              <button type="button" data-kview="3d" aria-pressed="false">3D View</button>
            </div>
          </div>
          <div class="preview-frame" id="kitchenPreviewSvg"></div>
          <p class="preview-note">Illustrative preview. Cabinet colour, doors, handles, stone, tiles, lighting and appliances update instantly.</p>

          <div id="kitchenProductInfoPanel" class="info-panel" aria-live="polite">
            <h5>Product Information</h5>
            <div class="info-empty">Select a product to see details.</div>
          </div>

          <div id="kitchenSummaryPanel" class="summary-panel" aria-live="polite"></div>
        </div>
      </aside>
    </div>

    <div class="modal" id="kitchenRequestModal" aria-hidden="true" role="dialog" aria-labelledby="kitchenModalTitle">
      <div class="modal-card quote-modal-card">
        <button type="button" class="modal-close" id="kitchenModalClose" aria-label="Close design request modal">✕</button>
        <h3 id="kitchenModalTitle">Request This Design</h3>
        <p>Please include this summary when you contact MIC NSW for your free consultation.</p>
        <textarea id="kitchenSummaryText" readonly style="width:100%;min-height:220px;border:1.5px solid var(--border);border-radius:var(--radius-sm);padding:12px;font-size:13px;font-family:'Work Sans','Segoe UI',Arial,sans-serif;color:#2f2a24;background:#fffdf7;"></textarea>
        <div class="modal-actions">
          <a href="index.html#contact" class="nav-btn primary">Go to Contact Form</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ============ BATHROOM ============ -->
  <section id="bathroom-tab" style="display:none;" aria-label="Bathroom renovation configurator">
    <div class="wizard-layout" id="bathroomWizard">
      <aside class="wizard-sidebar" aria-label="Bathroom design steps">
        <h2>Design Your Bathroom</h2>
        <div id="bathroomStepsList" class="steps-list"></div>
        <div id="bathroomRunningTotal" class="running-total" style="display:none;" aria-live="polite"></div>
      </aside>

      <section class="wizard-stage">
        <div id="bathroomStepContent" class="step-content fade-in" aria-live="polite"></div>
        <div class="step-actions">
          <button id="bathroomBackBtn" class="nav-btn" type="button" aria-label="Go to previous step">← Back</button>
          <button id="bathroomNextBtn" class="nav-btn primary" type="button" aria-label="Go to next step">Next →</button>
        </div>
      </section>

      <aside class="wizard-preview" aria-label="Bathroom live preview and summary">
        <div class="preview-panel">
          <div class="preview-header">
            <h4>Live Preview</h4>
            <div class="view-toggle" role="group" aria-label="Preview view">
              <button type="button" class="active" data-bview="2d" aria-pressed="true">2D Elevation</button>
              <button type="button" data-bview="3d" aria-pressed="false">3D Isometric</button>
            </div>
          </div>
          <div class="preview-frame" id="bathroomPreviewSvg"></div>
          <p class="preview-note">Illustrative preview. Vanity, tiles, tapware, screen, mirror and lighting update instantly.</p>

          <div id="bathroomProductInfoPanel" class="info-panel" aria-live="polite">
            <h5>Product Information</h5>
            <div class="info-empty">Select a product to see details.</div>
          </div>

          <div id="bathroomSummaryPanel" class="summary-panel" aria-live="polite"></div>
        </div>
      </aside>
    </div>
  </section>
</main>

<p class="disclaimer">
  * All prices are indicative ranges for standard-size Sydney metro rooms, based on typical retail/trade pricing from the suppliers named. They exclude structural work, asbestos removal, council approvals and site-access surcharges. A fixed written quote follows your free site consultation. Brand names (Kaboodle, Kinsman, Freedom Kitchens, IKEA, Laminex, Caesarstone, Essastone, Smartstone, Dekton, Beaumont Tiles, National Tiles, Signorino, Reece, Caroma, Methven, Phoenix, Nero, Sussex Taps, Chef, Westinghouse, Bosch, Fisher &amp; Paykel, ILVE, Smeg, Miele, Blum, Hettich, Clipsal) are examples of Australian-available suppliers MIC NSW can source and install — availability and current pricing confirmed at consultation.
</p>

<div class="modal quote-modal" id="quoteModal" role="dialog" aria-modal="true" aria-labelledby="quoteModalTitle" aria-hidden="true">
  <div class="modal-card quote-modal-card">
    <button type="button" class="modal-close" id="quoteModalClose" aria-label="Close quote request modal">✕</button>
    <h3 id="quoteModalTitle">Request This Quote</h3>
    <p>Enter your contact details and MIC NSW will receive your selected package and live estimate.</p>
    <form id="quoteRequestForm">
      <label for="quoteName">Full Name</label>
      <input id="quoteName" name="from_name" type="text" autocomplete="name" required>

      <label for="quoteEmail">Email Address</label>
      <input id="quoteEmail" name="email" type="email" autocomplete="email" required>

      <label for="quotePhone">Phone Number</label>
      <input id="quotePhone" name="phone" type="tel" autocomplete="tel" pattern="[0-9+() -]{8,20}" maxlength="20" title="Phone number with 8-20 digits, spaces, or +()- characters" required>

      <p class="quote-status" id="quoteFormStatus" role="status" aria-live="polite"></p>

      <div class="modal-actions">
        <button type="button" class="btn-secondary" id="quoteCancelBtn">Cancel</button>
        <button type="submit" class="btn-primary" id="quoteSubmitBtn">Send Quote Request</button>
      </div>
    </form>
  </div>
</div>

<!-- Product Gallery Modal -->
<div class="modal gallery-modal" id="productGalleryModal" role="dialog" aria-modal="true" aria-labelledby="galleryTitle" aria-hidden="true">
  <div class="modal-card gallery-modal-card" role="document">
    <div class="gallery-main">
      <img id="galleryMainImage" src="" alt="">
      <button type="button" class="gallery-nav prev" id="galleryPrev" aria-label="Previous image">‹</button>
      <button type="button" class="gallery-nav next" id="galleryNext" aria-label="Next image">›</button>
      <button type="button" class="modal-close" id="galleryClose" style="top:10px;right:10px;background:rgba(0,0,0,.5);color:#fff;border:none;" aria-label="Close gallery">✕</button>
    </div>
    <div class="gallery-thumb-row" id="galleryThumbs"></div>
    <div class="gallery-info">
      <h4 id="galleryTitle">Product Gallery</h4>
      <p class="gallery-caption" id="galleryCaption"></p>
    </div>
  </div>
</div>

<footer class="site-footer">
  <div class="footer-inner">
    <div>
      <img src="https://mic-nsw.com.au/front/images/logo2.png" alt="MIC NSW">
      <p>MIC NSW PTY LTD — ABN: 51 665 533 282 — Contractor Licence: 393630C</p>
    </div>
    <div class="footer-links">
      <a href="index.html">← Back to Homepage</a>
      <a href="index.html#contact" style="color:var(--gold);">Contact Us</a>
      <a href="https://wa.me/+61470640083?text=Hello">WhatsApp</a>
    </div>
  </div>
</footer>
<a href="https://wa.me/+61470640083?text=Hello" class="whatsapp-btn" aria-label="Chat on WhatsApp">💬</a>
'''

# ---------------------------------------------------------------------------
# JavaScript (logic preserved; render strings rebuilt; new helpers added)
# ---------------------------------------------------------------------------
JS_LOGIC = r'''
<script>
/* ============================================================
   DATA
============================================================ */
const WEB3FORMS_ACCESS_KEY = 'fc340379-cc05-4c4b-a7f0-47d2e0cfab53';
const MIC_CONTACT_EMAIL = 'info@mic-nsw.com.au';
const QUOTE_REQUEST_TIMEOUT_MS = 10000;
''' + js_data + r'''
const kitchenStepDefinitions = [
  {step:1, title:'Choose Package', short:'Package', description:'Select the renovation package that matches your desired level of finish, benchtop quality and supplier direction.'},
  {step:2, title:'Choose Layout', short:'Layout', description:'Pick the floorplan that best suits your room footprint and how you want to move through the space.'},
  {step:3, title:'Cabinet Style', short:'Style & Quantity', description:'Set cabinet quantities and choose the door profile that defines the kitchen character.'},
  {step:4, title:'Cabinet Colour', short:'Finish', description:'Lock in a cabinet finish that suits your package and palette.'},
  {step:5, title:'Benchtops', short:'Stone surface', description:'Compare benchtop surfaces, brands and upgrades to refine the look and durability.'},
  {step:6, title:'Splashback', short:'Tiles & pattern', description:'Select the splashback style and pattern direction to complement your cabinetry and benchtop.'},
  {step:7, title:'Appliances', short:'Appliance suite', description:'Choose the appliance brands and performance tier for each key cooking zone.'},
  {step:8, title:'Lighting & Final Touches', short:'Lighting & upgrades', description:'Add LED lighting and premium upgrades to elevate usability, storage and final detailing.'},
  {step:9, title:'Review & Quote', short:'Preview and request', description:'Review the visual concept, check the itemised pricing summary and request this exact kitchen design.'}
];
const kitchenSteps = kitchenStepDefinitions.map(s=>({id:s.step, title:s.title, desc:s.short}));
const KITCHEN_FIRST_STEP = 1;
const KITCHEN_TOTAL_STEPS = kitchenSteps.length;
const KITCHEN_REVIEW_STEP = KITCHEN_TOTAL_STEPS;
const KITCHEN_CONFIG_LAST_STEP = KITCHEN_REVIEW_STEP - 1;
const BASE_CABINET_MIN = 2, BASE_CABINET_MAX = 8, BASE_CABINET_DEFAULT = 5, BASE_CABINET_MOD = 450;
const WALL_CABINET_MIN = 2, WALL_CABINET_MAX = 6, WALL_CABINET_DEFAULT = 3, WALL_CABINET_MOD = 380;

const BATHROOM_FIRST_STEP = 1;
const BATHROOM_TOTAL_STEPS = 6;
const BATHROOM_REVIEW_STEP = 6;
const bathroomSteps = [
  {id:1, title:'Package', desc:'Essential, Premium or Luxury'},
  {id:2, title:'Vanity', desc:'Style & colour'},
  {id:3, title:'Tiling', desc:'Floor & wall tiles'},
  {id:4, title:'Fixtures', desc:'Tapware & shower screen'},
  {id:5, title:'Extras', desc:'Optional upgrades'},
  {id:6, title:'Review', desc:'Summary & request quote'}
];

/* ============================================================
   STATE
============================================================ */
let kState = {
  step:1, pkg:'essential', layout:'ushape', baseCount:5, wallCount:3, door:'flat', color:'white',
  benchtop:'laminex', splash:'subway', splashPattern:'Gloss White Brick',
  splashPatterns:{ceramic:'Warm White', subway:'Gloss White Brick', mosaic:'Stone Blend', large:'Calacatta Vein'},
  microwave:'chef', oven:'westinghouse', cooktop:'chef', rangehood:'chef',
  upgrades:{led:false, utility:false, handles:false, softClose:false, pantry:false},
  completed:{}, view:'2d'
};
let bState = {step:1, pkg:null, vanityStyle:'wallhung', vanityColor:'white', floorTile:'subway', wallTile:'subway',
  tap:'chrome', screen:'semi', ledMirror:false, elecPlumb:false, view:'2d', completed:{}};

let lastKitchenSelection = null;
let lastBathroomSelection = null;

/* ============================================================
   HELPERS
============================================================ */
function money(value){
  if(value===0) return '$0';
  return (value>0?'+$':'-$') + Math.abs(value).toLocaleString();
}
function clampValue(value, min, max){ return Math.max(min, Math.min(max, value)); }
function escapeHtml(text){ return String(text).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }

function packageById(){ return kitchenPackages.find(p=>p.id===kState.pkg) || kitchenPackages[0]; }
function benchtopById(){ return benchtops.find(b=>b.id===kState.benchtop) || benchtops[0]; }
function splashById(){ return splashbacks.find(s=>s.id===kState.splash) || splashbacks[0]; }
function doorById(){ return doorStyles.find(d=>d.id===kState.door) || doorStyles[0]; }
function colorById(){ return cabinetColors.find(c=>c.id===kState.color) || cabinetColors[0]; }
function layoutById(){ return kitchenLayouts.find(l=>l.id===kState.layout) || kitchenLayouts[0]; }
function applianceModFor(list, id){ return list.find(item=>item.id===id)?.mod ?? 0; }

function calcKitchenTotals(){
  const pkg = packageById();
  const cabinetAdjustment = ((kState.baseCount-BASE_CABINET_DEFAULT)*BASE_CABINET_MOD) + ((kState.wallCount-WALL_CABINET_DEFAULT)*WALL_CABINET_MOD);
  const benchtopMod = benchtopById().mod;
  const splashbackMod = splashById().mod;
  const applianceMod = applianceModFor(microwaves, kState.microwave) + applianceModFor(ovens, kState.oven)
                     + applianceModFor(cooktops, kState.cooktop) + applianceModFor(rangehoods, kState.rangehood);
  const upgradesMod = kitchenUpgradeOptions.reduce((sum, opt)=>sum + (kState.upgrades[opt.id] ? opt.mod : 0), 0);
  const total = pkg.low + cabinetAdjustment + benchtopMod + splashbackMod + applianceMod + upgradesMod;
  return {pkg, cabinetAdjustment, benchtopMod, splashbackMod, applianceMod, upgradesMod, total};
}
function calcBathroomTotals(){
  const pkg = bathroomPackages.find(p=>p.id===bState.pkg);
  if(!pkg) return null;
  const vMod = vanityStyles.find(v=>v.id===bState.vanityStyle).mod;
  const tMod = tapware.find(t=>t.id===bState.tap).mod;
  const sMod = showerScreens.find(s=>s.id===bState.screen).mod;
  const ledMod = bState.ledMirror?550:0;
  const elecMod = bState.elecPlumb?1500:0;
  const addOn = vMod+tMod+sMod+ledMod+elecMod;
  return {pkg, low:pkg.low+addOn, high:pkg.high+addOn, vMod, tMod, sMod, ledMod, elecMod};
}

function markKitchenStep(step){ kState.completed[step] = true; }
function isKitchenStepComplete(step){ return !!kState.completed[step]; }
function areKitchenStepsComplete(){ for(let i=KITCHEN_FIRST_STEP;i<=KITCHEN_CONFIG_LAST_STEP;i++) if(!isKitchenStepComplete(i)) return false; return true; }

function getSelectionName(options, id){ const m = options.find(o=>o.id===id); return m ? m.name : 'Not selected'; }

/* ============================================================
   RIPPLE
============================================================ */
function createRipple(e){
  const btn = e.currentTarget;
  const circle = document.createElement('span');
  const d = Math.max(btn.clientWidth, btn.clientHeight);
  const rect = btn.getBoundingClientRect();
  circle.style.width = circle.style.height = d + 'px';
  circle.style.left = (e.clientX - rect.left - d/2) + 'px';
  circle.style.top = (e.clientY - rect.top - d/2) + 'px';
  circle.classList.add('ripple');
  const existing = btn.getElementsByClassName('ripple')[0];
  if(existing) existing.remove();
  btn.appendChild(circle);
  setTimeout(()=>circle.remove(),600);
}
function bindRipple(root){ root.querySelectorAll('.nav-btn, .product-card, .toggle-card, .step-item, .color-card, .gallery-trigger, .view-toggle button').forEach(el=>{
  el.style.position = 'relative';
  el.style.overflow = 'hidden';
  el.addEventListener('click', createRipple);
}); }

/* ============================================================
   SEARCH / FILTER
============================================================ */
function searchFilterBarHTML(category, filters){
  const chips = (filters||[]).map(f=>`<button type="button" class="sf-chip" data-filter="${f.key}" aria-pressed="false">${f.label}</button>`).join('');
  return `<div class="sf-bar" data-sf-category="${escapeHtml(category)}">
    <input type="search" class="sf-search" placeholder="Search ${escapeHtml(category)}..." aria-label="Search ${escapeHtml(category)}">
    <div class="sf-filters" role="group" aria-label="Filter ${escapeHtml(category)}">
      <button type="button" class="sf-chip active" data-filter="all" aria-pressed="true">All</button>
      ${chips}
    </div>
  </div>`;
}
function bindSearchFilter(container){
  const bar = container.querySelector('.sf-bar');
  if(!bar) return;
  const search = bar.querySelector('.sf-search');
  const chips = [...bar.querySelectorAll('.sf-chip')];
  function apply(){
    const term = search.value.toLowerCase();
    const active = chips.filter(c=>c.classList.contains('active')).map(c=>c.dataset.filter);
    const cards = container.querySelectorAll('[data-search-text]');
    cards.forEach(card=>{
      const text = (card.dataset.searchText||'').toLowerCase();
      const tags = (card.dataset.tags||'').toLowerCase().split(',');
      const isPremium = card.dataset.premium==='true';
      const isRecommended = card.dataset.recommended==='true';
      let show = text.includes(term);
      active.forEach(f=>{
        if(!show) return;
        if(f==='premium') show = show && isPremium;
        else if(f==='recommended') show = show && isRecommended;
        else if(f==='australian') show = show && tags.includes('australian made');
        else if(f==='bestseller') show = show && tags.includes('best seller');
        else if(f==='new') show = show && tags.includes('new arrival');
        else if(f==='luxury') show = show && tags.includes('luxury');
      });
      card.style.display = show ? '' : 'none';
    });
  }
  search.addEventListener('input', apply);
  chips.forEach(chip=>{
    chip.addEventListener('click', ()=>{
      if(chip.dataset.filter==='all'){
        chips.forEach(c=>{c.classList.remove('active');c.setAttribute('aria-pressed','false');});
        chip.classList.add('active'); chip.setAttribute('aria-pressed','true');
      } else {
        const allChip = chips.find(c=>c.dataset.filter==='all');
        if(allChip){ allChip.classList.remove('active'); allChip.setAttribute('aria-pressed','false'); }
        chip.classList.toggle('active');
        chip.setAttribute('aria-pressed', chip.classList.contains('active')?'true':'false');
        if(!chips.some(c=>c.classList.contains('active'))){ allChip.classList.add('active'); allChip.setAttribute('aria-pressed','true'); }
      }
      apply();
    });
  });
}

/* ============================================================
   GALLERY / LIGHTBOX
============================================================ */
let galleryImages = [], galleryIndex = 0, galleryProduct = null;
function galleryFor(product){
  const base = product.image || 'https://placehold.co/800x600?text=Product';
  const lifestyle = product.lifestyle || 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=900&q=80';
  const installed = product.installed || 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=900&q=80';
  return [base, lifestyle, installed];
}
function openGallery(product, category){
  galleryProduct = product;
  galleryImages = galleryFor(product);
  galleryIndex = 0;
  const modal = document.getElementById('productGalleryModal');
  modal.classList.add('show');
  modal.setAttribute('aria-hidden','false');
  updateGallery();
  document.getElementById('galleryClose').focus();
}
function updateGallery(){
  const main = document.getElementById('galleryMainImage');
  const thumbs = document.getElementById('galleryThumbs');
  const title = document.getElementById('galleryTitle');
  const cap = document.getElementById('galleryCaption');
  main.src = galleryImages[galleryIndex];
  main.alt = galleryProduct.name + ' image ' + (galleryIndex+1);
  thumbs.innerHTML = galleryImages.map((src,i)=>`<img src="${src}" class="gallery-thumb ${i===galleryIndex?'active':''}" data-idx="${i}" alt="Thumbnail ${i+1}" role="button" tabindex="0">`).join('');
  title.textContent = galleryProduct.brand ? `${galleryProduct.brand} ${galleryProduct.name}` : galleryProduct.name;
  const captions = ['Product detail','Lifestyle setting','Installed example'];
  cap.textContent = captions[galleryIndex] + (galleryProduct.description ? ' — ' + galleryProduct.description : '');
}
function closeGallery(){
  const modal = document.getElementById('productGalleryModal');
  modal.classList.remove('show');
  modal.setAttribute('aria-hidden','true');
}
function initGalleryModal(){
  document.getElementById('galleryClose').addEventListener('click', closeGallery);
  document.getElementById('galleryPrev').addEventListener('click', ()=>{ galleryIndex = (galleryIndex-1+galleryImages.length)%galleryImages.length; updateGallery(); });
  document.getElementById('galleryNext').addEventListener('click', ()=>{ galleryIndex = (galleryIndex+1)%galleryImages.length; updateGallery(); });
  document.getElementById('galleryThumbs').addEventListener('click', e=>{ const t=e.target.closest('[data-idx]'); if(t){ galleryIndex=Number(t.dataset.idx); updateGallery(); }});
  document.getElementById('productGalleryModal').addEventListener('click', e=>{ if(e.target===e.currentTarget) closeGallery(); });
  document.addEventListener('keydown', e=>{ if(!document.getElementById('productGalleryModal').classList.contains('show')) return; if(e.key==='Escape') closeGallery(); if(e.key==='ArrowRight'){ galleryIndex=(galleryIndex+1)%galleryImages.length; updateGallery(); } if(e.key==='ArrowLeft'){ galleryIndex=(galleryIndex-1+galleryImages.length)%galleryImages.length; updateGallery(); } });
}

/* ============================================================
   PRODUCT INFO PANEL
============================================================ */
function showKitchenInfo(product, category){
  lastKitchenSelection = {product, category};
  const panel = document.getElementById('kitchenProductInfoPanel');
  if(!product){ panel.innerHTML='<h5>Product Information</h5><div class="info-empty">Select a product to see details.</div>'; return; }
  const cost = product.mod!==undefined ? money(product.mod) : '';
  const tags = (product.tags||[]).map(t=>`<span class="badge ${t==='Luxury'?'badge-premium':t==='Most Popular'?'badge-recommended':'badge-selected'}" style="font-size:9px;padding:3px 7px;">${t}</span>`).join('');
  panel.innerHTML = `
    <h5>${escapeHtml(category)}</h5>
    <figure class="info-media"><img src="${product.image||'https://placehold.co/600x400?text=No+Image'}" alt="${escapeHtml(product.name)}"></figure>
    <div class="card-badges" style="position:static;margin-bottom:8px;">${tags}</div>
    <p class="info-title">${escapeHtml(product.name)}</p>
    <p class="info-sub">${escapeHtml(product.brand||'MIC NSW')} ${product.collection?'· '+escapeHtml(product.collection):''}</p>
    <p class="info-desc">${escapeHtml(product.description||'')}</p>
    <dl class="info-grid">
      ${product.material?`<div><dt>Material</dt><dd>${escapeHtml(product.material)}</dd></div>`:''}
      ${product.finish?`<div><dt>Finish</dt><dd>${escapeHtml(product.finish)}</dd></div>`:''}
      ${product.warranty?`<div><dt>Warranty</dt><dd>${escapeHtml(product.warranty)}</dd></div>`:''}
      ${product.country?`<div><dt>Origin</dt><dd>${escapeHtml(product.country)}</dd></div>`:''}
      ${product.cleaning?`<div><dt>Cleaning</dt><dd>${escapeHtml(product.cleaning)}</dd></div>`:''}
      ${product.installNotes?`<div><dt>Install Notes</dt><dd>${escapeHtml(product.installNotes)}</dd></div>`:''}
      ${product.availability?`<div><dt>Availability</dt><dd>${escapeHtml(product.availability)}</dd></div>`:''}
    </dl>
    ${cost?`<div class="info-cost">Upgrade cost: ${cost}</div>`:''}
    <button type="button" class="nav-btn primary" style="width:100%;margin-top:12px;" data-gallery-open>View Gallery</button>
  `;
  panel.querySelector('[data-gallery-open]').addEventListener('click', ()=>openGallery(product, category));
}
function showBathroomInfo(product, category){
  lastBathroomSelection = {product, category};
  const panel = document.getElementById('bathroomProductInfoPanel');
  if(!product){ panel.innerHTML='<h5>Product Information</h5><div class="info-empty">Select a product to see details.</div>'; return; }
  const cost = product.mod!==undefined ? money(product.mod) : '';
  const tags = (product.tags||[]).map(t=>`<span class="badge ${t==='Luxury'?'badge-premium':t==='Most Popular'?'badge-recommended':'badge-selected'}" style="font-size:9px;padding:3px 7px;">${t}</span>`).join('');
  panel.innerHTML = `
    <h5>${escapeHtml(category)}</h5>
    <figure class="info-media"><img src="${product.image||'https://placehold.co/600x400?text=No+Image'}" alt="${escapeHtml(product.name)}"></figure>
    <div class="card-badges" style="position:static;margin-bottom:8px;">${tags}</div>
    <p class="info-title">${escapeHtml(product.name)}</p>
    <p class="info-sub">${escapeHtml(product.brand||'MIC NSW')} ${product.collection?'· '+escapeHtml(product.collection):''}</p>
    <p class="info-desc">${escapeHtml(product.description||'')}</p>
    <dl class="info-grid">
      ${product.material?`<div><dt>Material</dt><dd>${escapeHtml(product.material)}</dd></div>`:''}
      ${product.finish?`<div><dt>Finish</dt><dd>${escapeHtml(product.finish)}</dd></div>`:''}
      ${product.warranty?`<div><dt>Warranty</dt><dd>${escapeHtml(product.warranty)}</dd></div>`:''}
      ${product.country?`<div><dt>Origin</dt><dd>${escapeHtml(product.country)}</dd></div>`:''}
      ${product.cleaning?`<div><dt>Cleaning</dt><dd>${escapeHtml(product.cleaning)}</dd></div>`:''}
      ${product.installNotes?`<div><dt>Install Notes</dt><dd>${escapeHtml(product.installNotes)}</dd></div>`:''}
      ${product.availability?`<div><dt>Availability</dt><dd>${escapeHtml(product.availability)}</dd></div>`:''}
    </dl>
    ${cost?`<div class="info-cost">Upgrade cost: ${cost}</div>`:''}
    <button type="button" class="nav-btn primary" style="width:100%;margin-top:12px;" data-gallery-open>View Gallery</button>
  `;
  panel.querySelector('[data-gallery-open]').addEventListener('click', ()=>openGallery(product, category));
}

/* ============================================================
   SUMMARY PANELS
============================================================ */
function renderKitchenSummaryPanel(){
  const panel = document.getElementById('kitchenSummaryPanel');
  const t = calcKitchenTotals();
  const items = [];
  items.push({label:'Package', value:t.pkg.name});
  items.push({label:'Layout', value:layoutById().name});
  items.push({label:'Cabinets', value:`${kState.baseCount} base + ${kState.wallCount} wall`});
  items.push({label:'Door style', value:doorById().name});
  items.push({label:'Cabinet colour', value:colorById().name});
  items.push({label:'Benchtop', value:`${benchtopById().brand} ${benchtopById().name}`});
  items.push({label:'Splashback', value:splashById().name});
  const upgrades = kitchenUpgradeOptions.filter(o=>kState.upgrades[o.id]);
  items.push({label:'Upgrades', value:upgrades.length?upgrades.map(u=>u.title).join(', '):'None'});
  const gst = Math.round(t.total * 0.1);
  const deposit = Math.round(t.total * 0.2);
  const finance = Math.round(t.total / 60);
  panel.innerHTML = `
    <h5>Estimate Summary</h5>
    <div class="summary-products"><ul style="margin:0;padding-left:16px;">${items.map(i=>`<li><strong>${i.label}:</strong> ${escapeHtml(i.value)}</li>`).join('')}</ul></div>
    <div class="summary-line"><span>Estimated Price</span><span>$${t.total.toLocaleString()}+</span></div>
    <div class="summary-line"><span>Upgrade Costs</span><span>${money(t.benchtopMod+t.splashbackMod+t.applianceMod+t.upgradesMod+t.cabinetAdjustment)}</span></div>
    <div class="summary-line"><span>GST included</span><span>~$${gst.toLocaleString()}</span></div>
    <div class="summary-line"><span>20% Deposit</span><span>~$${deposit.toLocaleString()}</span></div>
    <div class="summary-total">$${t.total.toLocaleString()}+</div>
    <div class="summary-meta">
      Est. build time: 4–8 weeks · Install duration: 2–3 weeks<br>
      Finance estimate: ~$${finance.toLocaleString()}/mo over 5 yrs*
    </div>
  `;
}
function renderBathroomSummaryPanel(){
  const panel = document.getElementById('bathroomSummaryPanel');
  const t = calcBathroomTotals();
  if(!t){ panel.innerHTML='<h5>Estimate Summary</h5><p class="summary-meta">Select a package to see pricing.</p>'; return; }
  const items = [
    {label:'Package', value:t.pkg.name},
    {label:'Vanity', value:`${getSelectionName(vanityStyles,bState.vanityStyle)} / ${getSelectionName(vanityColors,bState.vanityColor)}`},
    {label:'Floor tile', value:getSelectionName(floorTiles,bState.floorTile)},
    {label:'Wall tile', value:getSelectionName(wallTiles,bState.wallTile)},
    {label:'Tapware', value:getSelectionName(tapware,bState.tap)},
    {label:'Shower screen', value:getSelectionName(showerScreens,bState.screen)},
    {label:'LED mirror', value:bState.ledMirror?'Yes':'No'},
    {label:'Elec & plumbing', value:bState.elecPlumb?'Yes':'No'}
  ];
  const total = t.low;
  const gst = Math.round(total * 0.1);
  const deposit = Math.round(total * 0.2);
  const finance = Math.round(total / 60);
  panel.innerHTML = `
    <h5>Estimate Summary</h5>
    <div class="summary-products"><ul style="margin:0;padding-left:16px;">${items.map(i=>`<li><strong>${i.label}:</strong> ${escapeHtml(i.value)}</li>`).join('')}</ul></div>
    <div class="summary-line"><span>Price Range</span><span>$${t.low.toLocaleString()} – $${t.high.toLocaleString()}</span></div>
    <div class="summary-line"><span>GST included</span><span>~$${gst.toLocaleString()}</span></div>
    <div class="summary-line"><span>20% Deposit</span><span>~$${deposit.toLocaleString()}</span></div>
    <div class="summary-total">$${t.low.toLocaleString()}+</div>
    <div class="summary-meta">
      Est. build time: 3–6 weeks · Install duration: 1–2 weeks<br>
      Finance estimate: ~$${finance.toLocaleString()}/mo over 5 yrs*
    </div>
  `;
}

/* ============================================================
   PRODUCT CARD COMPONENT
============================================================ */
function productCard(item, selected, dataAttrs, opts={}){
  opts = Object.assign({category:'', priceDiff:undefined, showSuppliers:false, layoutIcon:''}, opts);
  const badges = [];
  if(item.premium) badges.push('<span class="badge badge-premium">Premium</span>');
  if(item.recommended) badges.push('<span class="badge badge-recommended">Recommended</span>');
  if(selected) badges.push('<span class="badge badge-selected">Selected</span>');
  const searchText = [item.name, item.brand||'', item.collection||'', item.material||'', item.finish||'', item.description||'', (item.tags||[]).join(' ')].join(' ').toLowerCase();
  const tags = (item.tags||[]).join(',').toLowerCase();
  const price = opts.priceDiff!==undefined ? `<div class="card-price ${item.mod>0?'positive':''}">${opts.priceDiff}</div>` : '';
  const suppliers = opts.showSuppliers && item.suppliers ? `<div class="card-suppliers">${item.suppliers.map(s=>`<span>${escapeHtml(s)}</span>`).join('')}</div>` : '';
  const img = opts.layoutIcon || `<img src="${item.image||'https://placehold.co/600x400?text='+encodeURIComponent(item.name)}" alt="${escapeHtml(item.name)}" loading="lazy">`;
  return `<article class="product-card ${selected?'selected':''}" ${dataAttrs} role="button" tabindex="0" data-search-text="${escapeHtml(searchText)}" data-tags="${escapeHtml(tags)}" data-premium="${!!item.premium}" data-recommended="${!!item.recommended}" aria-label="Select ${escapeHtml(item.name)}">
    <div class="card-badges">${badges.join('')}</div>
    <figure class="card-media">${img}<button type="button" class="gallery-trigger" aria-label="Open gallery for ${escapeHtml(item.name)}">⤢</button></figure>
    <div class="card-body">
      <div class="card-meta">${item.brand?`<span>${escapeHtml(item.brand)}</span>`:''}${item.collection?`<span>${escapeHtml(item.collection)}</span>`:''}</div>
      <h4 class="card-title">${escapeHtml(item.name)}</h4>
      ${item.description?`<p class="card-desc">${escapeHtml(item.description)}</p>`:''}
      <div class="card-specs">${item.material?`<span>${escapeHtml(item.material)}</span>`:''}${item.finish?`<span>${escapeHtml(item.finish)}</span>`:''}</div>
      ${price}
      ${suppliers}
    </div>
  </article>`;
}

/* ============================================================
   KITCHEN PREVIEW
============================================================ */
function renderKitchenPreview(){
  const wrap = document.getElementById('kitchenPreviewSvg');
  const cabinet = colorById().hex;
  const bench = benchtopById().hex;
  const splash = splashById().hex;
  const hasHandles = kState.upgrades.handles;
  const hasLed = kState.upgrades.led;
  const door = kState.door;
  const is3d = kState.view === '3d';

  if(is3d){
    const c1 = cabinet, c2 = shade(cabinet,25), c3 = shade(cabinet,-30);
    const b1 = bench, b2 = shade(bench,20), b3 = shade(bench,-25);
    const s1 = splash, s2 = shade(splash,15);
    let svg = `<svg viewBox="0 0 420 260" width="100%" height="auto" aria-label="Kitchen 3D preview">
      <rect width="420" height="260" fill="#f2efe8"/>
      <polygon points="20,60 400,60 380,40 40,40" fill="#e0dbd1"/>
      <rect x="20" y="60" width="380" height="120" fill="${s1}"/>
      <polygon points="20,60 40,40 40,160 20,180" fill="${s2}" opacity=".6"/>`;
    for(let i=0;i<kState.wallCount;i++){
      const x=35+i*72, y=65, w=64, h=50;
      svg += isoBox(x, y+h, w, h, 12, c1, c2, c3);
      if(door==='shaker'||door==='raised') svg+=`<rect x="${x+8}" y="${y+8}" width="${w-16}" height="${h-16}" fill="none" stroke="rgba(0,0,0,.12)" stroke-width="2"/>`;
      if(hasHandles) svg+=`<circle cx="${x+w-8}" cy="${y+h-12}" r="3" fill="#C9A24B"/>`;
      if(hasLed) svg+=`<rect x="${x}" y="${y+h+2}" width="${w}" height="3" fill="#FFE9AE" opacity=".85"/>`;
    }
    svg += isoBox(30, 190, 360, 12, 18, b1, b2, b3);
    for(let i=0;i<kState.baseCount;i++){
      const x=30+i*72, w=68, h=70;
      svg += isoBox(x, 190, w, h, 18, c1, c2, c3);
      if(door==='shaker'||door==='raised') svg+=`<rect x="${x+6}" y="${190-h+6}" width="${w-12}" height="${h-12}" fill="none" stroke="rgba(0,0,0,.12)" stroke-width="2"/>`;
      else if(door==='handleless') svg+=`<rect x="${x+6}" y="${190-h+4}" width="${w-12}" height="4" fill="rgba(0,0,0,.08)"/>`;
      if(hasHandles) svg+=`<circle cx="${x+w-10}" cy="${190-h+35}" r="3" fill="#C9A24B"/>`;
    }
    svg += `<rect x="260" y="178" width="54" height="8" rx="2" fill="#2a2a2a"/>`;
    svg += `<circle cx="272" cy="182" r="3" fill="#555"/><circle cx="302" cy="182" r="3" fill="#555"/>`;
    svg += `<rect x="340" y="140" width="40" height="48" rx="2" fill="#1f2226" stroke="#444"/>`;
    svg += `<rect x="348" y="148" width="24" height="32" rx="2" fill="#333"/>`;
    svg += `<path d="M330 60 L350 40 L390 40 L410 60 Z" fill="#1f2226"/>`;
    svg += `</svg>`;
    wrap.innerHTML = svg;
    return;
  }

  const baseSpan = Math.max(18, 330 / kState.baseCount);
  const wallSpan = Math.max(22, 330 / kState.wallCount);
  let layoutShape='';
  if(kState.layout==='ushape') layoutShape='<path d="M25 35 H95 V95 H75 V55 H45 V95 H25 Z" fill="#d7cfbf" stroke="#8a7d63"/>';
  else if(kState.layout==='lshape') layoutShape='<path d="M25 35 H95 V55 H45 V95 H25 Z" fill="#d7cfbf" stroke="#8a7d63"/>';
  else if(kState.layout==='galley') layoutShape='<rect x="25" y="35" width="80" height="14" fill="#d7cfbf" stroke="#8a7d63"/><rect x="25" y="81" width="80" height="14" fill="#d7cfbf" stroke="#8a7d63"/>';
  else layoutShape='<rect x="25" y="35" width="80" height="14" fill="#d7cfbf" stroke="#8a7d63"/><rect x="55" y="72" width="20" height="14" fill="#d7cfbf" stroke="#8a7d63"/>';

  let baseDoors='', wallDoors='';
  for(let i=0;i<kState.baseCount;i++){
    const x=14+i*baseSpan, w=baseSpan-2;
    baseDoors += `<rect x="${x}" y="122" width="${w}" height="46" fill="${cabinet}" stroke="#0000001e"/>`;
    if(door==='shaker'||door==='raised') baseDoors += `<rect x="${x+5}" y="127" width="${w-10}" height="36" fill="none" stroke="rgba(0,0,0,.1)" stroke-width="2"/>`;
    if(door==='handleless') baseDoors += `<rect x="${x+4}" y="124" width="${w-8}" height="4" fill="rgba(0,0,0,.08)"/>`;
    if(hasHandles) baseDoors += `<circle cx="${x+w-8}" cy="${145}" r="3" fill="#C9A24B"/>`;
  }
  for(let i=0;i<kState.wallCount;i++){
    const x=14+i*wallSpan, w=wallSpan-2;
    wallDoors += `<rect x="${x}" y="38" width="${w}" height="38" fill="${cabinet}" stroke="#0000001e"/>`;
    if(door==='shaker'||door==='raised') wallDoors += `<rect x="${x+4}" y="42" width="${w-8}" height="30" fill="none" stroke="rgba(0,0,0,.1)" stroke-width="2"/>`;
    if(hasHandles) wallDoors += `<circle cx="${x+w-7}" cy="${57}" r="2.5" fill="#C9A24B"/>`;
    if(hasLed) wallDoors += `<rect x="${x}" y="${78}" width="${w}" height="3" fill="#FFE9AE" opacity=".85"/>`;
  }
  let svg = `<svg viewBox="0 0 380 200" width="100%" height="auto" aria-label="Kitchen 2D preview">
    <rect width="380" height="200" fill="#f2efe8"/>
    <rect x="8" y="78" width="364" height="42" fill="${splash}" stroke="#0000001e"/>
    ${wallDoors}
    <rect x="8" y="118" width="364" height="10" fill="${bench}" stroke="#0000001f"/>
    ${baseDoors}
    <rect x="270" y="118" width="46" height="10" rx="2" fill="#1f2226"/>
    <circle cx="282" cy="123" r="3" fill="#555"/><circle cx="304" cy="123" r="3" fill="#555"/>
    <rect x="330" y="124" width="34" height="44" rx="2" fill="#1f2226" stroke="#444"/>
    <rect x="336" y="130" width="22" height="32" rx="2" fill="#333"/>
    <g transform="translate(220,10)">${layoutShape}</g>
  </svg>`;
  wrap.innerHTML = svg;
}

function shade(hex, amt){
  const c = hex.replace('#','');
  const num = parseInt(c,16);
  let r=(num>>16)+amt, g=((num>>8)&0xff)+amt, b=(num&0xff)+amt;
  r=Math.max(0,Math.min(255,r)); g=Math.max(0,Math.min(255,g)); b=Math.max(0,Math.min(255,b));
  return '#'+((1<<24)+(r<<16)+(g<<8)+b).toString(16).slice(1);
}
function isoBox(x, y, w, h, d, frontColor, topColor, sideColor){
  const dx = d*0.55, dy = d*0.32;
  return `<polygon points="${x},${y-h} ${x+w},${y-h} ${x+w},${y} ${x},${y}" fill="${frontColor}" stroke="#00000022"/>
    <polygon points="${x},${y-h} ${x+dx},${y-h-dy} ${x+w+dx},${y-h-dy} ${x+w},${y-h}" fill="${topColor}" stroke="#00000022"/>
    <polygon points="${x+w},${y-h} ${x+w+dx},${y-h-dy} ${x+w+dx},${y-dy} ${x+w},${y}" fill="${sideColor}" stroke="#00000022"/>`;
}

function layoutIcon(id){
  const s='stroke="#1C2B33" stroke-width="4" fill="#E9E4D6"';
  if(id==='ushape') return `<svg viewBox="0 0 100 70" aria-hidden="true"><path d="M10 10 H30 V45 H70 V10 H90 V60 H10 Z" ${s}/></svg>`;
  if(id==='lshape') return `<svg viewBox="0 0 100 70" aria-hidden="true"><path d="M10 10 H90 V30 H40 V60 H10 Z" ${s}/></svg>`;
  if(id==='galley') return `<svg viewBox="0 0 100 70" aria-hidden="true"><rect x="10" y="10" width="80" height="14" ${s}/><rect x="10" y="46" width="80" height="14" ${s}/></svg>`;
  return `<svg viewBox="0 0 100 70" aria-hidden="true"><rect x="10" y="10" width="80" height="14" ${s}/><rect x="38" y="42" width="24" height="18" ${s}/></svg>`;
}

/* ============================================================
   BATHROOM PREVIEW
============================================================ */
function getBathroomPreviewSVG(view){
  const vColor = vanityColors.find(c=>c.id===bState.vanityColor).hex;
  const wTile = wallTiles.find(t=>t.id===bState.wallTile).hex;
  const fTile = floorTiles.find(t=>t.id===bState.floorTile).hex;
  const tap = tapware.find(t=>t.id===bState.tap).hex;
  if(view==='3d'){
    let parts=`<rect x="0" y="0" width="460" height="300" fill="${shade(wTile,10)}"/>`;
    parts+=`<polygon points="0,220 460,220 400,300 60,300" fill="${shade(fTile,-10)}"/>`;
    parts+=isoBox(60,260,140,55,34,vColor,shade(vColor,25),shade(vColor,-30));
    parts+=`<rect x="70" y="150" width="120" height="70" fill="#cfe3ea" stroke="#00000022"/>`;
    if(bState.ledMirror) parts+=`<rect x="68" y="148" width="124" height="74" fill="none" stroke="#FFE9AE" stroke-width="4" opacity=".85"/>`;
    parts+=`<rect x="118" y="228" width="6" height="20" fill="${tap}"/><circle cx="121" cy="226" r="5" fill="${tap}"/>`;
    parts+=isoBox(300,260,90,190,60,'#dbeef2','#eef9fb','#c3dee3');
    return `<svg viewBox="0 0 460 300" width="100%" height="auto" style="max-width:100%;display:block;">${parts}</svg>`;
  }
  const isFreestanding=bState.vanityStyle==='freestanding';
  const isFramed=bState.screen==='framed';
  const mirrorGlow=bState.ledMirror?`<rect x="30" y="55" width="130" height="66" fill="none" stroke="#FFE9AE" stroke-width="4" opacity=".8"/>`:'';
  return `<svg viewBox="0 0 420 260" width="100%" height="auto" style="max-width:100%;display:block;">
    <rect x="0" y="0" width="420" height="190" fill="${wTile}"/>
    <rect x="0" y="190" width="420" height="70" fill="${fTile}"/>
    <rect x="270" y="30" width="130" height="230" fill="#dff0f5" opacity=".35" stroke="${isFramed?'#2b2c2e':'#9fb8bd'}" stroke-width="${isFramed?6:2}"/>
    <rect x="270" y="30" width="6" height="230" fill="${isFramed?'#2b2c2e':'#9fb8bd'}"/>
    <rect x="20" y="${isFreestanding?150:170}" width="150" height="70" rx="4" fill="${vColor}" stroke="#00000022"/>
    ${isFreestanding?`<rect x="20" y="150" width="150" height="4" fill="#00000022"/>`:``}
    <rect x="35" y="140" width="120" height="18" rx="9" fill="#fff" stroke="#00000022"/>
    <rect x="90" y="118" width="6" height="24" fill="${tap}"/><circle cx="93" cy="116" r="5" fill="${tap}"/>
    <rect x="35" y="58" width="120" height="60" rx="4" fill="#cfe3ea" stroke="#00000015"/>
    ${mirrorGlow}
  </svg>`;
}
function renderBathroomPreview(){ document.getElementById('bathroomPreviewSvg').innerHTML = getBathroomPreviewSVG(bState.view); }

/* ============================================================
   KITCHEN WIZARD RENDER
============================================================ */
function renderKitchenSidebar(){
  const list = document.getElementById('kitchenStepsList');
  list.innerHTML = kitchenSteps.map(step=>{
    const complete = isKitchenStepComplete(step.id);
    return `<div class="step-item ${kState.step===step.id?'active':''} ${complete?'completed':''}" data-step-go="${step.id}" role="button" tabindex="0" aria-label="Go to ${step.title}">
      <div class="step-index">${complete ? '✓' : step.id}</div>
      <div class="step-meta"><strong>${step.title}</strong><span>${step.desc}</span></div>
    </div>`;
  }).join('');
}
function renderKitchenRunningTotal(){
  const box = document.getElementById('kitchenRunningTotal');
  if(kState.step===1){ box.style.display='none'; return; }
  const t = calcKitchenTotals();
  box.style.display='flex';
  box.innerHTML = `Running Total <span class="amount">$${t.total.toLocaleString()}+</span>`;
}
function renderStepHead(step){
  return `<div class="step-head">
    <div><h3>Step ${step.id}: ${step.title}</h3><p>${step.desc}</p></div>
    ${isKitchenStepComplete(step.id)?'<span class="completed-badge">Completed</span>':''}
  </div>`;
}
function kitchenDesignSummaryText(){
  const t = calcKitchenTotals();
  const upgrades = kitchenUpgradeOptions.filter(o=>kState.upgrades[o.id]).map(o=>o.title);
  return [
    `PACKAGE: ${t.pkg.name} ($${t.pkg.low.toLocaleString()}–$${t.pkg.high.toLocaleString()})`,
    `LAYOUT: ${layoutById().name}`,
    `CABINETS: ${kState.baseCount} base + ${kState.wallCount} wall`,
    `DOOR STYLE: ${doorById().name}`,
    `COLOR: ${colorById().name}`,
    `BENCHTOP: ${benchtopById().brand} ${benchtopById().name} — ${money(t.benchtopMod)}`,
    `SPLASHBACK: ${splashById().name} (${kState.splashPattern}) — ${money(t.splashbackMod)}`,
    `APPLIANCES: ${microwaves.find(a=>a.id===kState.microwave).brand} / ${ovens.find(a=>a.id===kState.oven).brand} / ${cooktops.find(a=>a.id===kState.cooktop).brand} / ${rangehoods.find(a=>a.id===kState.rangehood).brand} — ${money(t.applianceMod)}`,
    `UPGRADES: ${upgrades.length ? upgrades.join(', ') : 'None'} — ${money(t.upgradesMod)}`,
    `TOTAL INVESTMENT: $${t.total.toLocaleString()}+`
  ].join('\n');
}

function renderKitchenStepContent(){
  const container = document.getElementById('kitchenStepContent');
  const step = kitchenSteps.find(s=>s.id===kState.step);
  let content = renderStepHead(step);

  if(kState.step===1){
    content += searchFilterBarHTML('packages',[{key:'recommended',label:'Recommended'},{key:'premium',label:'Premium'},{key:'australian',label:'Australian Made'}]);
    content += `<div class="cards-grid cols-3">${kitchenPackages.map(pkg=>productCard(pkg, kState.pkg===pkg.id, `data-pkg="${pkg.id}"`, {category:'Package', priceDiff:`$${pkg.low.toLocaleString()}–$${pkg.high.toLocaleString()}`, showSuppliers:true})).join('')}</div>`;
  }
  else if(kState.step===2){
    content += `<div class="cards-grid">${kitchenLayouts.map(layout=>productCard(layout, kState.layout===layout.id, `data-layout="${layout.id}"`, {category:'Layout', layoutIcon:`<div class="layout-icon">${layoutIcon(layout.id)}</div>`})).join('')}</div>`;
  }
  else if(kState.step===3){
    content += `<div class="cards-grid cols-2">
      <div class="stepper-box"><h5>Base Cabinets</h5><div class="stepper"><button type="button" data-stepper="base" data-dir="-1" aria-label="Decrease base cabinets">−</button><span aria-live="polite">${kState.baseCount}</span><button type="button" data-stepper="base" data-dir="1" aria-label="Increase base cabinets">+</button></div><div class="stepper-mod">${money((kState.baseCount-BASE_CABINET_DEFAULT)*BASE_CABINET_MOD)} adjustment</div></div>
      <div class="stepper-box"><h5>Wall Cabinets</h5><div class="stepper"><button type="button" data-stepper="wall" data-dir="-1" aria-label="Decrease wall cabinets">−</button><span aria-live="polite">${kState.wallCount}</span><button type="button" data-stepper="wall" data-dir="1" aria-label="Increase wall cabinets">+</button></div><div class="stepper-mod">${money((kState.wallCount-WALL_CABINET_DEFAULT)*WALL_CABINET_MOD)} adjustment</div></div>
    </div>
    <h5 style="margin:22px 0 12px;color:var(--navy);font-size:13px;text-transform:uppercase;letter-spacing:.45px;">Door Style</h5>
    <div class="cards-grid cols-2">${doorStyles.map(d=>productCard(d, kState.door===d.id, `data-door="${d.id}"`, {category:'Door Style', priceDiff:money(d.mod)})).join('')}</div>`;
  }
  else if(kState.step===4){
    content += searchFilterBarHTML('cabinet colours',[{key:'australian',label:'Australian Made'},{key:'new',label:'New Arrival'}]);
    content += `<div class="color-grid">${cabinetColors.map(color=>`
      <article class="color-card ${kState.color===color.id?'selected':''}" data-color="${color.id}" role="button" tabindex="0" aria-label="Select ${color.name}" data-search-text="${escapeHtml(color.name+' '+color.brand+' '+color.finish+' '+color.material).toLowerCase()}" data-tags="${(color.tags||[]).join(',').toLowerCase()}" data-premium="${!!color.premium}" data-recommended="${!!color.recommended}">
        <div class="color-swatch" style="background:${color.hex};"></div>
        <h4>${color.name}</h4>
        <span>${color.brand} · ${color.finish}</span>
      </article>`).join('')}</div>`;
  }
  else if(kState.step===5){
    content += searchFilterBarHTML('benchtops',[{key:'premium',label:'Premium'},{key:'recommended',label:'Recommended'},{key:'australian',label:'Australian Made'}]);
    content += `<div class="cards-grid">${benchtops.map(b=>productCard(b, kState.benchtop===b.id, `data-benchtop="${b.id}"`, {category:'Benchtop', priceDiff:money(b.mod)})).join('')}</div>`;
  }
  else if(kState.step===6){
    const selectedSplash = splashById();
    content += searchFilterBarHTML('splashbacks',[{key:'premium',label:'Premium'},{key:'recommended',label:'Recommended'}]);
    content += `<div class="cards-grid">${splashbacks.map(s=>productCard(s, kState.splash===s.id, `data-splash="${s.id}"`, {category:'Splashback', priceDiff:money(s.mod)})).join('')}</div>`;
    content += `<div class="stepper-box" style="margin-top:18px;"><h5>Pattern Options</h5><div class="cards-grid cols-3">${selectedSplash.patterns.map(pattern=>`
      <article class="product-card ${kState.splashPattern===pattern?'selected':''}" data-pattern="${pattern}" role="button" tabindex="0" aria-label="Select ${pattern}" data-search-text="${escapeHtml(pattern+' '+selectedSplash.name).toLowerCase()}">
        <div class="card-body"><h4 class="card-title">${pattern}</h4><p class="card-desc">${selectedSplash.name}</p></div>
      </article>`).join('')}</div></div>`;
  }
  else if(kState.step===7){
    const sections = [
      {key:'microwave', title:'Microwave', list:microwaves},
      {key:'oven', title:'Oven', list:ovens},
      {key:'cooktop', title:'Cooktop', list:cooktops},
      {key:'rangehood', title:'Rangehood', list:rangehoods}
    ];
    content += searchFilterBarHTML('appliances',[{key:'premium',label:'Premium'},{key:'recommended',label:'Recommended'}]);
    content += sections.map(sec=>`<div style="margin-bottom:18px;"><h5 style="margin:0 0 10px;color:var(--navy);font-size:13px;text-transform:uppercase;letter-spacing:.45px;">${sec.title}</h5><div class="cards-grid cols-3">${sec.list.map(item=>productCard(item, kState[sec.key]===item.id, `data-appliance="${sec.key}" data-id="${item.id}"`, {category:sec.title, priceDiff:money(item.mod)})).join('')}</div></div>`).join('');
  }
  else if(kState.step===8){
    content += `<div class="toggle-grid">${kitchenUpgradeOptions.map(option=>`
      <article class="toggle-card ${kState.upgrades[option.id]?'on':''}" data-upgrade="${option.id}" role="button" tabindex="0" aria-pressed="${kState.upgrades[option.id]?'true':'false'}" aria-label="Toggle ${option.title}">
        <div><h4>${option.title}</h4><p>${option.desc}</p><div class="card-price">${money(option.mod)}</div></div>
        <div class="toggle-check">${kState.upgrades[option.id]?'✓':''}</div>
      </article>`).join('')}</div>`;
  }
  else if(kState.step===9){
    const t = calcKitchenTotals();
    const upgrades = kitchenUpgradeOptions.filter(o=>kState.upgrades[o.id]);
    const canRequest = areKitchenStepsComplete();
    content += `<div class="review-grid">
      <div class="preview-frame" style="min-height:auto;">${document.getElementById('kitchenPreviewSvg').innerHTML}</div>
      <div class="review-summary"><pre>${kitchenDesignSummaryText()}</pre></div>
    </div>
    <div class="price-breakdown">
      <div class="line"><span>Base Package</span><span>$${t.pkg.low.toLocaleString()}–$${t.pkg.high.toLocaleString()}</span></div>
      <div class="line"><span>Cabinet Adjustment</span><span>${money(t.cabinetAdjustment)}</span></div>
      <div class="line"><span>Benchtop Upgrade</span><span>${money(t.benchtopMod)}</span></div>
      <div class="line"><span>Splashback</span><span>${money(t.splashbackMod)}</span></div>
      <div class="line"><span>Appliances</span><span>${money(t.applianceMod)}</span></div>
      <div class="line"><span>Extras & Upgrades</span><span>${money(t.upgradesMod)}</span></div>
      <div class="line"><strong>TOTAL INVESTMENT</strong><strong>$${t.total.toLocaleString()}+</strong></div>
      <div style="font-size:11px;color:#7f7667;margin-top:8px;">(Fixed quote after free consultation)</div>
      <button type="button" id="kitchenRequestBtn" class="nav-btn primary request-btn" ${canRequest?'':'disabled'}>Request This Design</button>
      ${!canRequest?'<div style="margin-top:6px;font-size:11px;color:#a14f39;">Complete Steps 1–8 to enable requests.</div>':''}
      <div style="margin-top:8px;font-size:11px;color:#7f7667;">Selected upgrades: ${upgrades.length?upgrades.map(u=>u.title).join(', '):'None'}.</div>
    </div>`;
  }

  container.innerHTML = content;
  bindSearchFilter(container);
  bindRipple(container);
  bindGalleryTriggers(container);
  updateKitchenNav();
  renderKitchenRunningTotal();
  renderKitchenPreview();
  renderKitchenSummaryPanel();
}

function bindGalleryTriggers(root){
  root.querySelectorAll('.gallery-trigger').forEach(btn=>{
    btn.addEventListener('click', e=>{
      e.stopPropagation();
      const card = btn.closest('.product-card, .color-card');
      if(!card) return;
      let product = null, category='';
      if(card.dataset.pkg){ product=kitchenPackages.find(p=>p.id===card.dataset.pkg); category='Package'; }
      else if(card.dataset.layout){ product=kitchenLayouts.find(l=>l.id===card.dataset.layout); category='Layout'; }
      else if(card.dataset.door){ product=doorStyles.find(d=>d.id===card.dataset.door); category='Door Style'; }
      else if(card.dataset.color){ product=cabinetColors.find(c=>c.id===card.dataset.color); category='Cabinet Colour'; }
      else if(card.dataset.benchtop){ product=benchtops.find(b=>b.id===card.dataset.benchtop); category='Benchtop'; }
      else if(card.dataset.splash){ product=splashbacks.find(s=>s.id===card.dataset.splash); category='Splashback'; }
      else if(card.dataset.appliance){ const key=card.dataset.appliance; product=[...microwaves,...ovens,...cooktops,...rangehoods].find(a=>a.id===card.dataset.id && (key==='microwave'?microwaves.includes(a):key==='oven'?ovens.includes(a):key==='cooktop'?cooktops.includes(a):rangehoods.includes(a))); category='Appliance'; }
      else if(card.dataset.bpkg){ product=bathroomPackages.find(p=>p.id===card.dataset.bpkg); category='Bathroom Package'; }
      else if(card.dataset.bvanity){ product=vanityStyles.find(v=>v.id===card.dataset.bvanity); category='Vanity Style'; }
      else if(card.dataset.bvcolor){ product=vanityColors.find(c=>c.id===card.dataset.bvcolor); category='Vanity Colour'; }
      else if(card.dataset.bfloor){ product=floorTiles.find(t=>t.id===card.dataset.bfloor); category='Floor Tile'; }
      else if(card.dataset.bwall){ product=wallTiles.find(t=>t.id===card.dataset.bwall); category='Wall Tile'; }
      else if(card.dataset.btap){ product=tapware.find(t=>t.id===card.dataset.btap); category='Tapware'; }
      else if(card.dataset.bscreen){ product=showerScreens.find(s=>s.id===card.dataset.bscreen); category='Shower Screen'; }
      if(product) openGallery(product, category);
    });
  });
}

function updateKitchenNav(){
  const backBtn = document.getElementById('kitchenBackBtn');
  const nextBtn = document.getElementById('kitchenNextBtn');
  backBtn.disabled = kState.step===KITCHEN_FIRST_STEP;
  backBtn.setAttribute('aria-disabled', backBtn.disabled?'true':'false');
  if(kState.step===KITCHEN_REVIEW_STEP){ nextBtn.textContent='Design Complete'; nextBtn.disabled=true; }
  else if(kState.step===KITCHEN_CONFIG_LAST_STEP){ nextBtn.textContent='Review Design'; nextBtn.disabled=false; }
  else{ nextBtn.textContent='Next →'; nextBtn.disabled=false; }
  nextBtn.setAttribute('aria-disabled', nextBtn.disabled?'true':'false');
}

function renderKitchenWizard(){
  renderKitchenSidebar();
  renderKitchenStepContent();
}

function changeKitchenStep(delta){
  if(delta>0) markKitchenStep(kState.step);
  const next = Math.min(KITCHEN_TOTAL_STEPS, Math.max(KITCHEN_FIRST_STEP, kState.step+delta));
  if(next===KITCHEN_REVIEW_STEP) markKitchenStep(KITCHEN_CONFIG_LAST_STEP);
  kState.step = next;
  renderKitchenWizard();
}

/* ============================================================
   BATHROOM WIZARD RENDER
============================================================ */
function renderBathroomSidebar(){
  const list = document.getElementById('bathroomStepsList');
  list.innerHTML = bathroomSteps.map(step=>{
    const complete = !!bState.completed[step.id];
    return `<div class="step-item ${bState.step===step.id?'active':''} ${complete?'completed':''}" data-bstep="${step.id}" role="button" tabindex="0" aria-label="Go to ${step.title}">
      <div class="step-index">${complete?'✓':step.id}</div>
      <div class="step-meta"><strong>${step.title}</strong><span>${step.desc}</span></div>
    </div>`;
  }).join('');
}
function renderBathroomRunningTotal(){
  const box = document.getElementById('bathroomRunningTotal');
  if(bState.step===1 || !bState.pkg){ box.style.display='none'; return; }
  const t = calcBathroomTotals();
  if(!t){ box.style.display='none'; return; }
  box.style.display='flex';
  box.innerHTML = `Price Range <span class="amount">$${t.low.toLocaleString()} – $${t.high.toLocaleString()}</span>`;
}
function getBathroomSummaryText(){
  const t = calcBathroomTotals();
  if(!t) return 'No package selected.';
  return [
    `PACKAGE: ${t.pkg.name} ($${t.pkg.low.toLocaleString()}–$${t.pkg.high.toLocaleString()})`,
    `VANITY: ${getSelectionName(vanityStyles,bState.vanityStyle)} / ${getSelectionName(vanityColors,bState.vanityColor)}`,
    `FLOOR TILE: ${getSelectionName(floorTiles,bState.floorTile)}`,
    `WALL TILE: ${getSelectionName(wallTiles,bState.wallTile)}`,
    `TAPWARE: ${getSelectionName(tapware,bState.tap)} — ${t.tMod?'+$'+t.tMod.toLocaleString():'included'}`,
    `SHOWER SCREEN: ${getSelectionName(showerScreens,bState.screen)} — ${t.sMod?'+$'+t.sMod.toLocaleString():'included'}`,
    `LED MIRROR: ${bState.ledMirror?'Yes (+$550)':'No'}`,
    `ELECTRICAL & PLUMBING UPGRADE: ${bState.elecPlumb?'Yes (+$1,500)':'No'}`,
    `PRICE RANGE: $${t.low.toLocaleString()} – $${t.high.toLocaleString()}`
  ].join('\n');
}
function renderBathroomStepContent(){
  const container = document.getElementById('bathroomStepContent');
  const step = bathroomSteps.find(s=>s.id===bState.step);
  let content = `<div class="step-head"><div><h3>Step ${step.id}: ${step.title}</h3><p>${step.desc}</p></div>${bState.completed[step.id]?'<span class="completed-badge">Completed</span>':''}</div>`;

  if(bState.step===1){
    content += searchFilterBarHTML('bathroom packages',[{key:'recommended',label:'Most Popular'},{key:'premium',label:'Luxury'},{key:'australian',label:'Australian Made'}]);
    content += `<div class="cards-grid cols-3">${bathroomPackages.map(pkg=>productCard(pkg, bState.pkg===pkg.id, `data-bpkg="${pkg.id}"`, {category:'Bathroom Package', priceDiff:`$${pkg.low.toLocaleString()} – $${pkg.high.toLocaleString()}`, showSuppliers:true})).join('')}</div>`;
  }
  else if(bState.step===2){
    content += `<h5 style="margin:0 0 12px;color:var(--navy);font-size:13px;text-transform:uppercase;letter-spacing:.45px;">Vanity Style</h5>`;
    content += `<div class="cards-grid">${vanityStyles.map(v=>productCard(v, bState.vanityStyle===v.id, `data-bvanity="${v.id}"`, {category:'Vanity Style', priceDiff:money(v.mod)})).join('')}</div>`;
    content += `<h5 style="margin:22px 0 12px;color:var(--navy);font-size:13px;text-transform:uppercase;letter-spacing:.45px;">Cabinet Colour</h5>`;
    content += `<div class="color-grid">${vanityColors.map(color=>`
      <article class="color-card ${bState.vanityColor===color.id?'selected':''}" data-bvcolor="${color.id}" role="button" tabindex="0" aria-label="Select ${color.name}" data-search-text="${escapeHtml(color.name+' '+color.brand+' '+color.finish+' '+color.material).toLowerCase()}">
        <div class="color-swatch" style="background:${color.hex};"></div>
        <h4>${color.name}</h4>
        <span>${color.brand} · ${color.finish}</span>
      </article>`).join('')}</div>`;
  }
  else if(bState.step===3){
    content += searchFilterBarHTML('floor tiles',[{key:'premium',label:'Premium'},{key:'australian',label:'Australian Made'}]);
    content += `<div class="cards-grid cols-2">${floorTiles.map(t=>productCard(t, bState.floorTile===t.id, `data-bfloor="${t.id}"`, {category:'Floor Tile'})).join('')}</div>`;
    content += `<h5 style="margin:22px 0 12px;color:var(--navy);font-size:13px;text-transform:uppercase;letter-spacing:.45px;">Wall Tile</h5>`;
    content += searchFilterBarHTML('wall tiles',[{key:'premium',label:'Premium'}]);
    content += `<div class="cards-grid cols-2">${wallTiles.map(t=>productCard(t, bState.wallTile===t.id, `data-bwall="${t.id}"`, {category:'Wall Tile'})).join('')}</div>`;
  }
  else if(bState.step===4){
    content += searchFilterBarHTML('tapware',[{key:'premium',label:'Luxury'},{key:'recommended',label:'Recommended'}]);
    content += `<div class="cards-grid cols-2">${tapware.map(t=>productCard(t, bState.tap===t.id, `data-btap="${t.id}"`, {category:'Tapware', priceDiff:money(t.mod)})).join('')}</div>`;
    content += `<h5 style="margin:22px 0 12px;color:var(--navy);font-size:13px;text-transform:uppercase;letter-spacing:.45px;">Shower Screen</h5>`;
    content += `<div class="cards-grid">${showerScreens.map(s=>productCard(s, bState.screen===s.id, `data-bscreen="${s.id}"`, {category:'Shower Screen', priceDiff:money(s.mod)})).join('')}</div>`;
  }
  else if(bState.step===5){
    content += `<div class="toggle-grid">
      <article class="toggle-card ${bState.ledMirror?'on':''}" data-btoggle="ledMirror" role="button" tabindex="0" aria-pressed="${bState.ledMirror?'true':'false'}">
        <div><h4>LED Backlit Mirror</h4><p>Touch-sensor demister mirror.</p><div class="card-price">+$550</div></div>
        <div class="toggle-check">${bState.ledMirror?'✓':''}</div>
      </article>
      <article class="toggle-card ${bState.elecPlumb?'on':''}" data-btoggle="elecPlumb" role="button" tabindex="0" aria-pressed="${bState.elecPlumb?'true':'false'}">
        <div><h4>Electrical &amp; Plumbing Upgrade</h4><p>New points, exhaust fan, water relocation.</p><div class="card-price">+$1,500</div></div>
        <div class="toggle-check">${bState.elecPlumb?'✓':''}</div>
      </article>
    </div>`;
  }
  else if(bState.step===6){
    const t = calcBathroomTotals();
    content += `<div class="review-grid">
      <div class="preview-frame" style="min-height:auto;">${document.getElementById('bathroomPreviewSvg').innerHTML}</div>
      <div class="review-summary"><pre>${getBathroomSummaryText()}</pre></div>
    </div>`;
    if(t){
      content += `<div class="price-breakdown">
        <div class="line"><span>Base Package</span><span>$${t.pkg.low.toLocaleString()}–$${t.pkg.high.toLocaleString()}</span></div>
        <div class="line"><span>Vanity Style</span><span>${t.vMod?'+$'+t.vMod.toLocaleString():'included'}</span></div>
        <div class="line"><span>Tapware</span><span>${t.tMod?'+$'+t.tMod.toLocaleString():'included'}</span></div>
        <div class="line"><span>Shower Screen</span><span>${t.sMod?'+$'+t.sMod.toLocaleString():'included'}</span></div>
        <div class="line"><span>LED Mirror</span><span>${t.ledMod?'+$'+t.ledMod.toLocaleString():'not included'}</span></div>
        <div class="line"><span>Elec &amp; Plumbing</span><span>${t.elecMod?'+$'+t.elecMod.toLocaleString():'not included'}</span></div>
        <div class="line"><strong>PRICE RANGE</strong><strong>$${t.low.toLocaleString()} – $${t.high.toLocaleString()}</strong></div>
        <button type="button" id="bathroomQuoteBtn" class="nav-btn primary request-btn">Request This Quote</button>
        <div style="font-size:11px;color:#7f7667;margin-top:6px;">(Fixed quote after free consultation)</div>
      </div>`;
    } else {
      content += '<p style="color:#a14f39;">Please complete steps 1–5 first.</p>';
    }
  }

  container.innerHTML = content;
  bindSearchFilter(container);
  bindRipple(container);
  bindGalleryTriggers(container);
  updateBathroomNav();
  renderBathroomRunningTotal();
  renderBathroomPreview();
  renderBathroomSummaryPanel();
}
function updateBathroomNav(){
  const backBtn = document.getElementById('bathroomBackBtn');
  const nextBtn = document.getElementById('bathroomNextBtn');
  backBtn.disabled = bState.step===BATHROOM_FIRST_STEP;
  backBtn.setAttribute('aria-disabled', backBtn.disabled?'true':'false');
  if(bState.step===BATHROOM_REVIEW_STEP){ nextBtn.textContent='Review Design'; nextBtn.disabled=true; }
  else{ nextBtn.textContent='Next →'; nextBtn.disabled=false; }
  nextBtn.setAttribute('aria-disabled', nextBtn.disabled?'true':'false');
}
function renderBathroomWizard(){ renderBathroomSidebar(); renderBathroomStepContent(); }
function changeBathroomStep(delta){
  if(delta>0) bState.completed[bState.step] = true;
  bState.step = Math.max(BATHROOM_FIRST_STEP, Math.min(BATHROOM_TOTAL_STEPS, bState.step+delta));
  renderBathroomWizard();
}

/* ============================================================
   EVENT BINDING
============================================================ */
function initKitchenWizard(){
  const stepsList = document.getElementById('kitchenStepsList');
  const stepContent = document.getElementById('kitchenStepContent');
  const backBtn = document.getElementById('kitchenBackBtn');
  const nextBtn = document.getElementById('kitchenNextBtn');
  const modal = document.getElementById('kitchenRequestModal');
  const modalClose = document.getElementById('kitchenModalClose');
  const summaryText = document.getElementById('kitchenSummaryText');
  const viewToggle = document.querySelector('#kitchen-tab .view-toggle');
  let modalTrigger = null;

  function closeKitchenModal(){ modal.classList.remove('open'); modal.setAttribute('aria-hidden','true'); if(modalTrigger) modalTrigger.focus(); }

  if(viewToggle) viewToggle.addEventListener('click', e=>{
    const btn = e.target.closest('[data-kview]');
    if(!btn) return;
    kState.view = btn.dataset.kview;
    [...viewToggle.children].forEach(b=>{b.classList.toggle('active',b===btn);b.setAttribute('aria-pressed',b===btn?'true':'false');});
    renderKitchenPreview();
  });

  stepsList.addEventListener('click', e=>{ const item=e.target.closest('[data-step-go]'); if(!item) return; kState.step=Number(item.dataset.stepGo); renderKitchenWizard(); });
  stepsList.addEventListener('keydown', e=>{ if(e.key!=='Enter'&&e.key!==' ') return; const item=e.target.closest('[data-step-go]'); if(!item) return; e.preventDefault(); kState.step=Number(item.dataset.stepGo); renderKitchenWizard(); });
  backBtn.addEventListener('click', ()=>changeKitchenStep(-1));
  nextBtn.addEventListener('click', ()=>changeKitchenStep(1));

  stepContent.addEventListener('click', e=>{
    const pkg = e.target.closest('[data-pkg]');
    if(pkg){ kState.pkg=pkg.dataset.pkg; markKitchenStep(1); showKitchenInfo(kitchenPackages.find(p=>p.id===pkg.dataset.pkg),'Package'); renderKitchenWizard(); return; }

    const layout = e.target.closest('[data-layout]');
    if(layout){ kState.layout=layout.dataset.layout; markKitchenStep(2); showKitchenInfo(kitchenLayouts.find(l=>l.id===layout.dataset.layout),'Layout'); renderKitchenWizard(); return; }

    const stepper = e.target.closest('[data-stepper]');
    if(stepper){ const key=stepper.dataset.stepper, dir=Number(stepper.dataset.dir); if(key==='base') kState.baseCount=clampValue(kState.baseCount+dir,BASE_CABINET_MIN,BASE_CABINET_MAX); if(key==='wall') kState.wallCount=clampValue(kState.wallCount+dir,WALL_CABINET_MIN,WALL_CABINET_MAX); markKitchenStep(3); renderKitchenWizard(); return; }

    const door = e.target.closest('[data-door]');
    if(door){ kState.door=door.dataset.door; markKitchenStep(3); showKitchenInfo(doorStyles.find(d=>d.id===door.dataset.door),'Door Style'); renderKitchenWizard(); return; }

    const color = e.target.closest('[data-color]');
    if(color){ kState.color=color.dataset.color; markKitchenStep(4); showKitchenInfo(cabinetColors.find(c=>c.id===color.dataset.color),'Cabinet Colour'); renderKitchenWizard(); return; }

    const top = e.target.closest('[data-benchtop]');
    if(top){ kState.benchtop=top.dataset.benchtop; markKitchenStep(5); showKitchenInfo(benchtops.find(b=>b.id===top.dataset.benchtop),'Benchtop'); renderKitchenWizard(); return; }

    const splash = e.target.closest('[data-splash]');
    if(splash){ kState.splash=splash.dataset.splash; const def=splashbacks.find(s=>s.id===kState.splash)?.patterns[0]??''; kState.splashPattern=kState.splashPatterns[kState.splash]||def; markKitchenStep(6); showKitchenInfo(splashbacks.find(s=>s.id===splash.dataset.splash),'Splashback'); renderKitchenWizard(); return; }

    const pattern = e.target.closest('[data-pattern]');
    if(pattern){ kState.splashPattern=pattern.dataset.pattern; kState.splashPatterns[kState.splash]=pattern.dataset.pattern; markKitchenStep(6); renderKitchenWizard(); return; }

    const appliance = e.target.closest('[data-appliance]');
    if(appliance){ const key=appliance.dataset.appliance, list={microwave,oven,cooktop,rangehood}[key]; kState[key]=appliance.dataset.id; markKitchenStep(7); showKitchenInfo(list.find(a=>a.id===appliance.dataset.id),key.charAt(0).toUpperCase()+key.slice(1)); renderKitchenWizard(); return; }

    const upgrade = e.target.closest('[data-upgrade]');
    if(upgrade){ const key=upgrade.dataset.upgrade; kState.upgrades[key]=!kState.upgrades[key]; markKitchenStep(8); showKitchenInfo(kitchenUpgradeOptions.find(o=>o.id===key),'Upgrade'); renderKitchenWizard(); return; }

    const requestBtn = e.target.closest('#kitchenRequestBtn');
    if(requestBtn && areKitchenStepsComplete()){
      modalTrigger=requestBtn; summaryText.value=kitchenDesignSummaryText(); modal.classList.add('open'); modal.setAttribute('aria-hidden','false'); modalClose.focus(); markKitchenStep(9); renderKitchenSidebar(); return;
    }
  });

  modalClose.addEventListener('click', closeKitchenModal);
  modal.addEventListener('click', e=>{ if(e.target===modal) closeKitchenModal(); });
  modal.addEventListener('keydown', e=>{
    if(e.key==='Escape'){ closeKitchenModal(); return; }
    if(e.key!=='Tab') return;
    const focusable=[...modal.querySelectorAll('button,[href],input,select,textarea,[tabindex]:not([tabindex="-1"])')].filter(n=>!n.disabled);
    if(!focusable.length) return;
    const first=focusable[0], last=focusable[focusable.length-1];
    if(e.shiftKey && document.activeElement===first){ e.preventDefault(); last.focus(); }
    else if(!e.shiftKey && document.activeElement===last){ e.preventDefault(); first.focus(); }
  });

  renderKitchenWizard();
}

function initBathroomWizard(){
  const stepsList = document.getElementById('bathroomStepsList');
  const stepContent = document.getElementById('bathroomStepContent');
  const backBtn = document.getElementById('bathroomBackBtn');
  const nextBtn = document.getElementById('bathroomNextBtn');
  const viewToggle = document.querySelector('#bathroom-tab .view-toggle');

  if(viewToggle) viewToggle.addEventListener('click', e=>{
    const btn = e.target.closest('[data-bview]');
    if(!btn) return;
    bState.view = btn.dataset.bview;
    [...viewToggle.children].forEach(b=>{b.classList.toggle('active',b===btn);b.setAttribute('aria-pressed',b===btn?'true':'false');});
    renderBathroomPreview();
  });

  stepsList.addEventListener('click', e=>{ const item=e.target.closest('[data-bstep]'); if(!item) return; bState.step=Number(item.dataset.bstep); renderBathroomWizard(); });
  stepsList.addEventListener('keydown', e=>{ if(e.key!=='Enter'&&e.key!==' ') return; const item=e.target.closest('[data-bstep]'); if(!item) return; e.preventDefault(); bState.step=Number(item.dataset.bstep); renderBathroomWizard(); });
  backBtn.addEventListener('click', ()=>changeBathroomStep(-1));
  nextBtn.addEventListener('click', ()=>changeBathroomStep(1));

  stepContent.addEventListener('click', e=>{
    const pkg = e.target.closest('[data-bpkg]');
    if(pkg){ bState.pkg=pkg.dataset.bpkg; bState.completed[1]=true; showBathroomInfo(bathroomPackages.find(p=>p.id===pkg.dataset.bpkg),'Bathroom Package'); renderBathroomWizard(); return; }

    const vanity = e.target.closest('[data-bvanity]');
    if(vanity){ bState.vanityStyle=vanity.dataset.bvanity; bState.completed[2]=true; showBathroomInfo(vanityStyles.find(v=>v.id===vanity.dataset.bvanity),'Vanity Style'); renderBathroomWizard(); return; }

    const vcolor = e.target.closest('[data-bvcolor]');
    if(vcolor){ bState.vanityColor=vcolor.dataset.bvcolor; bState.completed[2]=true; showBathroomInfo(vanityColors.find(c=>c.id===vcolor.dataset.bvcolor),'Vanity Colour'); renderBathroomWizard(); return; }

    const floor = e.target.closest('[data-bfloor]');
    if(floor){ bState.floorTile=floor.dataset.bfloor; bState.completed[3]=true; showBathroomInfo(floorTiles.find(t=>t.id===floor.dataset.bfloor),'Floor Tile'); renderBathroomWizard(); return; }

    const wall = e.target.closest('[data-bwall]');
    if(wall){ bState.wallTile=wall.dataset.bwall; bState.completed[3]=true; showBathroomInfo(wallTiles.find(t=>t.id===wall.dataset.bwall),'Wall Tile'); renderBathroomWizard(); return; }

    const tap = e.target.closest('[data-btap]');
    if(tap){ bState.tap=tap.dataset.btap; bState.completed[4]=true; showBathroomInfo(tapware.find(t=>t.id===tap.dataset.btap),'Tapware'); renderBathroomWizard(); return; }

    const screen = e.target.closest('[data-bscreen]');
    if(screen){ bState.screen=screen.dataset.bscreen; bState.completed[4]=true; showBathroomInfo(showerScreens.find(s=>s.id===screen.dataset.bscreen),'Shower Screen'); renderBathroomWizard(); return; }

    const toggle = e.target.closest('[data-btoggle]');
    if(toggle){ const key=toggle.dataset.btoggle; bState[key]=!bState[key]; bState.completed[5]=true; renderBathroomWizard(); return; }

    const quoteBtn = e.target.closest('#bathroomQuoteBtn');
    if(quoteBtn){ openQuoteModal('Bathroom Renovation', buildBathroomQuoteMessage(), quoteBtn); return; }
  });

  renderBathroomWizard();
}

/* ============================================================
   QUOTE MODAL (unchanged logic)
============================================================ */
const quoteModal = document.getElementById('quoteModal');
const quoteModalTitle = document.getElementById('quoteModalTitle');
const quoteRequestForm = document.getElementById('quoteRequestForm');
const quoteSubmitBtn = document.getElementById('quoteSubmitBtn');
const quoteCancelBtn = document.getElementById('quoteCancelBtn');
const quoteFormStatus = document.getElementById('quoteFormStatus');
let pendingQuoteRequest = null;

function setQuoteStatus(message, isError=false){ quoteFormStatus.textContent=message; quoteFormStatus.classList.toggle('error',isError); }
function closeQuoteModal(){
  quoteModal.classList.remove('show'); quoteModal.setAttribute('aria-hidden','true'); setQuoteStatus('');
  const triggerBtn = pendingQuoteRequest && pendingQuoteRequest.button; pendingQuoteRequest=null;
  if(triggerBtn && document.contains(triggerBtn)){ try{ triggerBtn.focus(); }catch(e){} }
}
function openQuoteModal(serviceName, message, button){
  pendingQuoteRequest={serviceName,message,button,originalLabel:button.textContent};
  quoteModalTitle.textContent=`Request Your ${serviceName} Quote`;
  quoteRequestForm.reset(); setQuoteStatus('');
  quoteModal.classList.add('show'); quoteModal.setAttribute('aria-hidden','false');
  document.getElementById('quoteName').focus();
}
async function submitQuoteRequest(contact){
  if(!pendingQuoteRequest){ setQuoteStatus(`Sorry, something went wrong. Please reopen the quote form or contact MIC NSW directly at ${MIC_CONTACT_EMAIL}.`,true); return; }
  const {serviceName,message,button,originalLabel}=pendingQuoteRequest;
  button.disabled=true; button.textContent='Sending quote request...'; quoteSubmitBtn.disabled=true;
  const controller=new AbortController(); const timeoutId=setTimeout(()=>controller.abort(),QUOTE_REQUEST_TIMEOUT_MS);
  try{
    const response=await fetch('https://api.web3forms.com/submit',{method:'POST',signal:controller.signal,headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({access_key:WEB3FORMS_ACCESS_KEY,subject:`${serviceName} Quote Request`,from_name:contact.from_name,email:contact.email,phone:contact.phone,message})});
    const result=await response.json();
    if(!response.ok || !result.success) throw new Error(result.message||'Unable to submit quote request.');
    button.textContent='Quote request sent ✓'; quoteSubmitBtn.disabled=false;
    setQuoteStatus(`Thanks ${contact.from_name}! Your ${serviceName.toLowerCase()} quote request has been sent to MIC NSW.`);
    setTimeout(()=>{ button.textContent=originalLabel; button.disabled=false; closeQuoteModal(); },2500);
  }catch(error){
    const errorMessage=error && error.name==='AbortError'?`Your quote request timed out. Please try again or contact MIC NSW directly at ${MIC_CONTACT_EMAIL}.`:`Sorry, we could not send your quote request. Please try again or contact MIC NSW directly at ${MIC_CONTACT_EMAIL}.`;
    setQuoteStatus(errorMessage,true); button.textContent=originalLabel; button.disabled=false; quoteSubmitBtn.disabled=false; return;
  }finally{ clearTimeout(timeoutId); }
}
function buildKitchenQuoteMessage(){
  const t=calcKitchenTotals(); const pkg=t.pkg; const upgrades=kitchenUpgradeOptions.filter(o=>kState.upgrades[o.id]).map(o=>o.title);
  return [
    'Kitchen renovation quote request from the MIC NSW design studio.',`Estimated total: $${t.total.toLocaleString()}+`,
    `Package: ${pkg?pkg.name:'Not selected'}`,`Layout: ${getSelectionName(kitchenLayouts,kState.layout)}`,
    `Door style: ${getSelectionName(doorStyles,kState.door)}`,`Cabinet colour: ${getSelectionName(cabinetColors,kState.color)}`,
    `Benchtop: ${getSelectionName(benchtops,kState.benchtop)}`,`Microwave: ${getSelectionName(microwaves,kState.microwave)}`,
    `Oven: ${getSelectionName(ovens,kState.oven)}`,`Cooktop: ${getSelectionName(cooktops,kState.cooktop)}`,
    `Rangehood: ${getSelectionName(rangehoods,kState.rangehood)}`,`Base cabinets: ${kState.baseCount}`,
    `Wall cabinets: ${kState.wallCount}`,`Upgrades: ${upgrades.length?upgrades.join(', '):'None'}`
  ].join('\n');
}
function buildBathroomQuoteMessage(){
  const t=calcBathroomTotals(); const pkg=bathroomPackages.find(p=>p.id===bState.pkg);
  return [
    'Bathroom renovation quote request from the MIC NSW design studio.',
    t?`Estimated price range: $${t.low.toLocaleString()} – $${t.high.toLocaleString()}`:'No package selected.',
    `Package: ${pkg?pkg.name:'Not selected'} (${pkg?pkg.theme:'No theme'})`,
    `Vanity style: ${getSelectionName(vanityStyles,bState.vanityStyle)}`,`Vanity colour: ${getSelectionName(vanityColors,bState.vanityColor)}`,
    `Floor tile: ${getSelectionName(floorTiles,bState.floorTile)}`,`Wall tile: ${getSelectionName(wallTiles,bState.wallTile)}`,
    `Tapware: ${getSelectionName(tapware,bState.tap)}`,`Shower screen: ${getSelectionName(showerScreens,bState.screen)}`,
    `LED mirror: ${bState.ledMirror?'Yes':'No'}`,`Electrical & plumbing upgrade: ${bState.elecPlumb?'Yes':'No'}`
  ].join('\n');
}

/* ============================================================
   INIT
============================================================ */
initKitchenWizard();
initBathroomWizard();
initGalleryModal();

document.querySelectorAll('.tab').forEach(tab=>{
  tab.addEventListener('click', ()=>{
    document.querySelectorAll('.tab').forEach(t=>{t.classList.remove('active');t.setAttribute('aria-selected','false');});
    tab.classList.add('active'); tab.setAttribute('aria-selected','true');
    const target=tab.dataset.tab;
    document.getElementById('kitchen-tab').style.display=target==='kitchen'?'block':'none';
    document.getElementById('bathroom-tab').style.display=target==='bathroom'?'block':'none';
  });
});

quoteCancelBtn.addEventListener('click', closeQuoteModal);
quoteModal.addEventListener('click', e=>{ if(e.target===quoteModal) closeQuoteModal(); });
quoteRequestForm.addEventListener('submit', e=>{
  e.preventDefault(); if(!quoteRequestForm.reportValidity()) return;
  const from_name=document.getElementById('quoteName').value.trim();
  const email=document.getElementById('quoteEmail').value.trim();
  const phone=document.getElementById('quotePhone').value.trim();
  if(!from_name||!email||!phone){ setQuoteStatus('Please enter your name, email, and phone number.',true); return; }
  submitQuoteRequest({from_name,email,phone});
});

// Default info panels
showKitchenInfo(kitchenPackages[0],'Package');
</script>
'''

# ---------------------------------------------------------------------------
# Assemble and write
# ---------------------------------------------------------------------------
html = f'''<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Design Your Kitchen or Bathroom | MIC NSW — Sydney</title>
<meta name="description" content="Build your kitchen or bathroom renovation package online — choose your layout, cabinetry, benchtop, appliances and finishes, with live 2D/3D preview and instant pricing.">
<link rel="canonical" href="https://mic-nsw.com.au/build-your-renovation.html">
<link rel="icon" href="https://mic-nsw.com.au/front/images/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Work+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
{BODY_HTML}
{JS_LOGIC}
</body>
</html>
'''

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Wrote {len(html)} chars to {OUT}')
