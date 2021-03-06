# coding: utf-8
from PIL import Image

# Everything is calculated in units of 500000 years

epochs = [  (0,    (0,0,0)),        # Big Bang, as seen through cosmic background radiation
            (1400, (201,201,201)),  # Oldest known Gamma Ray Burst
            (1900, (119,0,150)),    # First galaxies form
            (5600, (23,87,120)),    # Milky Way Galaxy formed
            (10000,(73,155,201)),   # Milky Way Galaxy disk formed
            (18460,(100,178,223)),  # formation of the Solar System
            (18800,(100,100,100)),  # Oldest rocks known on Earth
            (19400,(198,147,0)),    # "Remains of biotic life" found in 4.1 billion-year-old rocks in Western Australia.
            (20000,(255,224,97)),   # First Life (Prokaryotes)
            (20800,(87,135,38)),    # Photosynthesis
            (22800,(110,192,56)),   # Oxygenation of Atmosphere
            (23600,(156,225,147)),  # Complex Cells (Eukaryotes)
            (26000,(250,126,144)),  # First Multicellular Life
            (26260,(255,169,58)),   # Simple Animals
            (26500,(209,127,21)),   # Arthropods (ancestors of insects, arachnids)
            (26600,(130,207,205)),  # Fish and Proto-amphibians
            (26700,(83,205,150)),   # Land Plants
            (26800,(208,202,24)),   # Insects and Seeds
            (26880,(40,150,208)),   # Amphibians
            (27000,(39,205,143)),   # Reptiles
            (27100,(159,207,208)),  # Permian-Triassic Extinction Event, 90% of Species Die Out
            (27140,(208,186,171)),  # Dinosaurs
            (27200,(210,65,0)),     # Mammals
            (27300,(238,170,22)),   # Birds
            (27340,(184,164,208)),  # Flowers
            (27470,(153,206,212)),  # Cretaceous–Paleogene extinction event, Non-avian Dinosaurs Die Out
            (27471,(240,191,95)),   # Primates
            (27571,(181,190,16)),   # Apes
            (27576,(240,232,0)),    # Hominids
            (27595,(145,250,0)),    # Primitive Humans and Stone Tools
            (27599,(255,38,0)),     # Domestication of Fire
            (27600,(0,173,255))     # Now
          ]
# Index the epoch array
epochs_n = 0

# The colour which forms the gaps
colourSpacer = (255, 255, 255)

# Number of x/y pixels to draw
yearsWide = 140
yearsHigh = 198

# Artwork dimensions
pixelWidth = 2
pixelHeight = 2
spacerWidth = 1
spacerHeight = 1

# Total image size
width = (pixelWidth + spacerWidth) * yearsWide
height = (pixelHeight + spacerHeight) * yearsHigh

# Initialise image
img = Image.new('RGB', (width,height), colourSpacer)
pixels = img.load() # create the pixel map

# Loop through each drawable epoch
for e in range(0, (yearsWide * yearsHigh)-1):
    x = (e % yearsWide) * (pixelWidth + spacerWidth)
    y = int(e / yearsWide)  * (pixelHeight + spacerHeight)

    # Figure out epoch
    if (epochs_n < len(epochs)-1):
        if(e == epochs[epochs_n+1][0]):
            epochs_n = epochs_n + 1

    # Show blanks if past last epoch
    if(e < epochs[-1][0]):
        color = epochs[epochs_n][1]
        # Draw Pixel
        for i in range(0, pixelWidth):
            for j in range(0, pixelHeight):
                pixels[x+i,y+j] = color
    elif(e == epochs[-1][0]):
        color = epochs[epochs_n][1]
        pixels[x,y] = color

# Done!
img.show()
