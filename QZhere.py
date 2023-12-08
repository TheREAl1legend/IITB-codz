import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QSplitter,
    QTextEdit,
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
import random

# Assume you have SDK classes for guided tours, historical information, and interactive maps
class GuidedTourSDK:
    def start_guided_tour(self):
        print("Starting guided tour")

class HistoricalInfoSDK:
    def get_historical_info(self, location):
        print(f"Getting historical information for {location}")

class InteractiveMapSDK:
    def show_location_on_map(self, location):
        print(f"Showing location {location} on the map")

class QZhereApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QZhere")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a QSplitter to separate the map and chat
        splitter = QSplitter(Qt.Horizontal)

        # Create a web engine view to display the map
        self.web_view = QWebEngineView()
        splitter.addWidget(self.web_view)

        # Create a text edit for chat
        self.chat_edit = QTextEdit()
        self.chat_edit.setHidden(True)
        splitter.addWidget(self.chat_edit)

        # Set the stretch factor for better responsiveness
        splitter.setStretchFactor(0, 2)
        splitter.setStretchFactor(1, 1)

        layout.addWidget(splitter)

        # Create buttons for additional features
        toggle_chat_button = QPushButton("Toggle Chat", self)
        toggle_chat_button.clicked.connect(self.toggle_chat)
        layout.addWidget(toggle_chat_button)

        guided_tour_button = QPushButton("Start Guided Tour", self)
        guided_tour_button.clicked.connect(self.start_guided_tour)
        layout.addWidget(guided_tour_button)

        historical_info_button = QPushButton("Get Historical Info", self)
        historical_info_button.clicked.connect(self.get_historical_info)
        layout.addWidget(historical_info_button)

        show_location_button = QPushButton("Show Location on Map", self)
        show_location_button.clicked.connect(self.show_location_on_map)
        layout.addWidget(show_location_button)

        # Load the HERE Maps URL
        self.load_map("https://mapcreator.here.com/OpenStreetMap?l=15.3883,47.2399,4,normal")

        # Add markers for all historical sites
        for site in historical_sites:
            self.add_marker(site["lat"], site["lng"], site["title"], site["description"])

    def load_map(self, url):
        # Load the map URL
        self.web_view.setUrl(QUrl(url))

    def add_marker(self, lat, lng, title, description):
        # Execute JavaScript to add a marker with an info window
        script = f"""
            var marker = new H.map.Marker({{lat: {lat}, lng: {lng}}});
            map.addObject(marker);
            
            var bubble = new H.ui.InfoBubble({{lat: {lat}, lng: {lng}}}, {{
                content: '<div><h3>{title}</h3><p>{description}</p></div>'
            }});
            ui.addBubble(bubble);
        """
        self.web_view.page().runJavaScript(script)

    def toggle_chat(self):
        # Toggle chat visibility
        self.chat_edit.setHidden(not self.chat_edit.isHidden())

    def start_guided_tour(self):
        guided_tour_sdk.start_guided_tour()

    def get_historical_info(self):
        current_location = "Current Location"  # You need to determine the user's current location
        historical_info_sdk.get_historical_info(current_location)

    def show_location_on_map(self):
        current_location = "Current Location"  # You need to determine the user's current location
        interactive_map_sdk.show_location_on_map(current_location)

# List of historical sites with their coordinates
historical_sites = [
    {"title": "Great Wall of China", "lat": 40.4319, "lng": 116.5704, "description": "China"},
    {"title": "Machu Picchu", "lat": -13.1631, "lng": -72.5450, "description": "Peru"},
    {"title": "Pyramids of Giza", "lat": 29.9792, "lng": 31.1342, "description": "Egypt"},
    {"title": "Acropolis of Athens", "lat": 37.9715, "lng": 23.7269, "description": "Greece"},
    {"title": "Colosseum", "lat": 41.8902, "lng": 12.4922, "description": "Italy"},
    {"title": "Petra", "lat": 30.3285, "lng": 35.4429, "description": "Jordan"},
    {"title": "Taj Mahal", "lat": 27.1751, "lng": 78.0421, "description": "India"},
        {"title": "Stonehenge", "lat": 51.1789, "lng": -1.8262, "description": "United Kingdom"},
    {"title": "Angkor Wat", "lat": 13.4125, "lng": 103.8670, "description": "Cambodia"},
    {"title": "Chichen Itza", "lat": 20.6829, "lng": -88.5686, "description": "Mexico"},
    {"title": "The Alhambra", "lat": 37.1775, "lng": -3.5986, "description": "Spain"},
    {"title": "Easter Island", "lat": -27.1127, "lng": -109.3497, "description": "Chile"},
    {"title": "Pompeii", "lat": 40.7482, "lng": 14.4849, "description": "Italy"},
    {"title": "Ephesus", "lat": 37.9496, "lng": 27.3645, "description": "Turkey"},
    {"title": "Great Zimbabwe", "lat": -20.2719, "lng": 30.9365, "description": "Zimbabwe"},
    {"title": "Borobudur", "lat": -7.6079, "lng": 110.2039, "description": "Indonesia"},
    {"title": "Historic Cairo", "lat": 30.0330, "lng": 31.2357, "description": "Egypt"},
    {"title": "Kyoto Historic Monuments", "lat": 35.0116, "lng": 135.7681, "description": "Japan"},
    {"title": "Versailles Palace", "lat": 48.8048, "lng": 2.1204, "description": "France"},
    {"title": "Mont Saint-Michel", "lat": 48.6367, "lng": -1.5120, "description": "France"},
    {"title": "The Kremlin and Red Square", "lat": 55.7517, "lng": 37.6177, "description": "Russia"},
    {"title": "The Parthenon and Delphi", "lat": 37.9838, "lng": 23.7275, "description": "Greece"},
    {"title": "Cappadocia", "lat": 38.6431, "lng": 34.8287, "description": "Turkey"},
    {"title": "Old City of Jerusalem", "lat": 31.7784, "lng": 35.2299, "description": "Israel"},
    {"title": "The Louvre", "lat": 48.8611, "lng": 2.3358, "description": "France"},
    {"title": "The Vatican City", "lat": 41.9022, "lng": 12.4534, "description": "Vatican City"},
    {"title": "The Great Barrier Reef", "lat": -16.5000, "lng": 145.7500, "description": "Australia"},
    {"title": "Independence Hall", "lat": 39.9489, "lng": -75.1561, "description": "USA"},
    {"title": "Mount Rushmore", "lat": 43.8791, "lng": -103.4591, "description": "USA"},
    {"title": "Yellowstone National Park", "lat": 44.4280, "lng": -110.5885, "description": "USA"},
    {"title": "Palace Museum (Forbidden City)", "lat": 39.9042, "lng": 116.3890, "description": "China"},
    {"title": "Hiroshima Peace Memorial", "lat": 34.3955, "lng": 132.4544, "description": "Japan"},
    {"title": "Robben Island", "lat": -33.8066, "lng": 18.3663, "description": "South Africa"},
    {"title": "The Grand Canyon", "lat": 36.0544, "lng": -112.1401, "description": "USA"},
    {"title": "The Tower of London", "lat": 51.5081, "lng": -0.0759, "description": "United Kingdom"},
    {"title": "The Panama Canal", "lat": 9.0765, "lng": -79.5117, "description": "Panama"},
    {"title": "The Banaue Rice Terraces", "lat": 16.9184, "lng": 121.0565, "description": "Philippines"},
    {"title": "The Statue of Liberty", "lat": 40.6892, "lng": -74.0445, "description": "USA"},
    {"title": "The Sydney Opera House", "lat": -33.8568, "lng": 151.2153, "description": "Australia"},
    {"title": "The Hagia Sophia", "lat": 41.0082, "lng": 28.9784, "description": "Turkey"},
    {"title": "The Potala Palace", "lat": 29.6579, "lng": 91.1173, "description": "China"},
    {"title": "The Golden Temple", "lat": 31.6204, "lng": 74.8765, "description": "India"},
    {"title": "The Sistine Chapel", "lat": 41.9029, "lng": 12.4534, "description": "Vatican City"},
    {"title": "The Panama Canal", "lat": 9.0765, "lng": -79.5117, "description": "Panama"},
    {"title": "The Serengeti National Park", "lat": -2.1542, "lng": 34.6857, "description": "Tanzania"},
    {"title": "The Galapagos Islands", "lat": -0.8329, "lng": -91.1374, "description": "Ecuador"},
    {"title": "The Amazon Rainforest", "lat": -3.4653, "lng": -62.2159, "description": "Brazil/Peru"},
    {"title": "The Palace of Westminster", "lat": 51.4994, "lng": -0.1248, "description": "United Kingdom"},
    {"title": "The Brandenburg Gate", "lat": 52.5163, "lng": 13.3777, "description": "Germany"},
    {"title": "The Normandy Beaches", "lat": 49.3984, "lng": -0.9867, "description": "France"},
    {"title": "Mount Everest", "lat": 27.9881, "lng": 86.9250, "description": "Nepal/China"},
    {"title": "The Great Mosque of Cordoba", "lat": 37.8786, "lng": -4.7790, "description": "Spain"},
    {"title": "The Terracotta Army", "lat": 34.3840, "lng": 109.2787, "description": "China"},
    {"title": "The Valley of the Kings", "lat": 25.7400, "lng": 32.6014, "description": "Egypt"},
    {"title": "The Victoria Falls", "lat": -17.9244, "lng": 25.8567, "description": "Zambia/Zimbabwe"},
    {"title": "The Saint Petersburg Historic Centre", "lat": 59.9343, "lng": 30.3351, "description": "Russia"},
    {"title": "The Cliffs of Moher", "lat": 52.9719, "lng": -9.4265, "description": "Ireland"},
    {"title": "The Sydney Harbour Bridge", "lat": -33.8523, "lng": 151.2108, "description": "Australia"},
    {"title": "The Belize Barrier Reef", "lat": 16.5208, "lng": -88.3615, "description": "Belize"},
    {"title": "The Ancient City of Damascus", "lat": 33.5138, "lng": 36.2920, "description": "Syria"},
    {"title": "The Serpent Mound", "lat": 39.0255, "lng": -83.4307, "description": "USA"},
    {"title": "The Palace of the Parliament", "lat": 44.4268, "lng": 26.1025, "description": "Romania"},
    {"title": "The Machair of South Uist", "lat": 57.3734, "lng": -7.3402, "description": "United Kingdom"},
    {"title": "The Wailing Wall", "lat": 31.7767, "lng": 35.2354, "description": "Israel"},
    {"title": "The Shwedagon Pagoda", "lat": 16.7984, "lng": 96.1481, "description": "Myanmar"},
    {"title": "The Tower of Pisa", "lat": 43.7229, "lng": 10.3966, "description": "Italy"},
    {"title": "The Ayutthaya Historical Park", "lat": 14.3588, "lng": 100.5681, "description": "Thailand"},
    {"title": "The Palace of the Shirvanshahs", "lat": 40.3659, "lng": 49.8345, "description": "Azerbaijan"},
    {"title": "The Blarney Stone", "lat": 51.9291, "lng": -8.5706, "description": "Ireland"},
    {"title": "The Independence Arch", "lat": 5.5600, "lng": -0.2057, "description": "Ghana"},
    {"title": "The Jeju Volcanic Island and Lava Tubes", "lat": 33.4996, "lng": 126.5312, "description": "South Korea"},
    {"title": "The Golden Gate Bridge", "lat": 37.8199, "lng": -122.4783, "description": "USA"},
    {"title": "The Charles Bridge", "lat": 50.0865, "lng": 14.4119, "description": "Czech Republic"},
    {"title": "The Palace of the Popes", "lat": 43.9492, "lng": 4.8055, "description": "France"},
    {"title": "The Giant's Causeway", "lat": 55.2409, "lng": -6.5114, "description": "United Kingdom"},
    {"title": "The Edinburgh Castle", "lat": 55.9486, "lng": -3.1999, "description": "United Kingdom"},
    {"title": "The Blue Mosque", "lat": 41.0054, "lng": 28.9768, "description": "Turkey"},
    {"title": "The St. Mark's Basilica", "lat": 45.4345, "lng": 12.3399, "description": "Italy"},
    {"title": "The St. Basil's Cathedral", "lat": 55.7525, "lng": 37.6231, "description": "Russia"},
    {"title": "The Jeita Grotto", "lat": 33.9464, "lng": 35.6252, "description": "Lebanon"},
    {"title": "The Kuala Lumpur Petronas Towers", "lat": 3.1577, "lng": 101.7120, "description": "Malaysia"},
    {"title": "The Tower Bridge", "lat": 51.5055, "lng": -0.0754, "description": "United Kingdom"},
    {"title": "The Hermitage Museum", "lat": 59.9390, "lng": 30.3158, "description": "Russia"},
    {"title": "The Hall of Mirrors at the Palace of Versailles", "lat": 48.8048, "lng": 2.1204, "description": "France"},
    {"title": "The Cape of Good Hope", "lat": -34.3587, "lng": 18.4731, "description": "South Africa"},
    {"title": "The Terracotta Army", "lat": 34.3840, "lng": 109.2787, "description": "China"},
]

# Initialize SDK instances
guided_tour_sdk = GuidedTourSDK()
historical_info_sdk = HistoricalInfoSDK()
interactive_map_sdk = InteractiveMapSDK()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QZhereApp()
    window.show()
    sys.exit(app.exec_())