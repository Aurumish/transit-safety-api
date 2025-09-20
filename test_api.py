# test_api.py - Basic API testing
import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000"

def test_api_endpoints():
    """Test basic API functionality"""
    print("🧪 Testing Transit Safety API endpoints...")
    
    try:
        # Test root endpoint
        response = requests.get(f"{BASE_URL}/")
        assert response.status_code == 200
        print("✅ Root endpoint working")
        
        # Test incidents endpoint
        response = requests.get(f"{BASE_URL}/api/incidents")
        assert response.status_code == 200
        incidents = response.json()
        print(f"✅ Incidents endpoint working - {len(incidents)} incidents found")
        
        # Test station safety endpoint
        response = requests.get(f"{BASE_URL}/api/stations/Times Square-42nd St/safety")
        assert response.status_code == 200
        station_data = response.json()
        print(f"✅ Station safety endpoint working - Safety score: {station_data.get('current_safety_score', 'N/A')}")
        
        # Test alerts endpoint
        response = requests.get(f"{BASE_URL}/api/alerts")
        assert response.status_code == 200
        alerts = response.json()
        print(f"✅ Alerts endpoint working - {len(alerts)} active alerts")
        
        # Test research trigger
        response = requests.post(f"{BASE_URL}/api/research/trigger")
        assert response.status_code == 200
        print("✅ Research trigger working")
        
        # Test ML integration endpoint
        response = requests.get(f"{BASE_URL}/api/stations/safety-scores")
        assert response.status_code == 200
        scores = response.json()
        print(f"✅ ML integration endpoint working - {len(scores)} station scores retrieved")

    except Exception as e:
        print(f"An error occurred: {e}")
        assert False, f"Request failed with exception: {e}"
