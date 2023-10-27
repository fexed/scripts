from PIL import Image, ImageDraw
import datetime


# Constants
cell_width = 50  # Width of each cell in pixels
cell_height = 15  # Height of each cell in pixels
padding = 10  # Padding between each square
label_padding = 20  # Padding between labels and the grid
months_per_year = 12  # Number of months in a year
start_year = 2020  # Start year
current_year = datetime.datetime.now().year  # Get the current year
total_years = current_year - start_year + 1
grid_width = months_per_year
grid_height = total_years
image_width = grid_width * (cell_width + padding) + label_padding
image_height = grid_height * (cell_height + padding) + label_padding

# Initialize a blank image
image = Image.new("RGBA", (image_width, image_height), "#FFFFFF00")
draw = ImageDraw.Draw(image)

# Hard-coded data source (year/month;number)
data = [
    "2020/01;418",
    "2020/02;156",
    "2020/03;0",
    "2020/04;262",
    "2020/05;316",
    "2020/06;388",
    "2020/07;2098",
    "2020/08;3575",
    "2020/09;2025",
    "2020/10;1451",
    "2020/11;519",
    "2020/12;381",
    "2021/01;87",
    "2021/02;518",
    "2021/03;285",
    "2021/04;1355",
    "2021/05;3058",
    "2021/06;1255",
    "2021/07;981",
    "2021/08;1908",
    "2021/09;1626",
    "2021/10;739",
    "2021/11;436",
    "2021/12;1312",
    "2022/01;74",
    "2022/02;546",
    "2022/03;240",
    "2022/04;610",
    "2022/05;1829",
    "2022/06;529",
    "2022/07;897",
    "2022/08;1010",
    "2022/09;580",
    "2022/10;3795",
    "2022/11;1358",
    "2022/12;695",
    "2023/01;1211",
    "2023/02;797",
    "2023/03;1652",
    "2023/04;1709",
    "2023/05;4866",
    "2023/06;2562",
    "2023/07;2177",
    "2023/08;5642",
    "2023/09;7091",
    "2023/10;1920",
    "2023/11;0",
    "2023/12;0",
]

# Function to parse the data
def parse_data(data):
    contributions = {}
    for item in data:
        date, count = item.split(";")
        year, month = date.split("/")
        contributions[(int(year), int(month))] = int(count)
    return contributions

# Function to map a value to a color
def value_to_color(value):
    if value == 0:
        return "#FFFFFF00"
    else:
        # Map the value to a light shade of blue proportional to the value
        blue = int(255 - (value / maximum) * 255)  # Adjust the range for shading
        alpha = int(100 + (value / maximum) * 155)  # Adjust the range for shading
        return f"#{blue:02x}{blue:02x}FF{alpha:02x}"

# Parse the data
contributions = parse_data(data)
maximum = max(contributions.values())

# Add year labels on the left with padding
for year in range(start_year, current_year + 1):
    y = year - start_year
    draw.text((2, y * (cell_height + padding) + cell_height + 5 // 2 + 5), str(year), fill="white")

# Add month labels at the top with padding
for month in range(1, months_per_year + 1):
    x = month - 1
    draw.text((x * (cell_width + padding) + cell_width // 2 + label_padding, 2), datetime.date(1900, month, 1).strftime("%B")[:3], fill="white")

# Draw the contribution grid
for year in range(start_year, current_year + 1):
    for x in range(grid_width):
        for y in range(grid_height):
            month = 1 + x  # Increment month from 1 to 12
            day = y
            if (year, month) in contributions:
                count = contributions[(year, month)]
                color = value_to_color(count)
                x = month - 1
                y = year - start_year
                square_x = label_padding + x * (cell_width + padding) + padding
                square_y = label_padding + y * (cell_height + padding)
                draw.rectangle(
                    [(square_x, square_y), (square_x + cell_width, square_y + cell_height)],
                    fill=color,
            )

# Save the image
image.save("photos.png")
