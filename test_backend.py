import requests
import json
import os

# Create a dummy PDF file for testing
dummy_pdf_path = "test_resume.pdf"
with open(dummy_pdf_path, "wb") as f:
    # A very minimal PDF structure
    f.write(b"%PDF-1.4\n1 0 obj\n<< /Title (Test Resume) /Author (Tester) >>\nendobj\n2 0 obj\n<< /Type /Catalog /Pages 3 0 R >>\nendobj\n3 0 obj\n<< /Type /Pages /Kids [4 0 R] /Count 1 >>\nendobj\n4 0 obj\n<< /Type /Page /Parent 3 0 R /MediaBox [0 0 612 792] /Contents 5 0 R >>\nendobj\n5 0 obj\n<< /Length 44 >>\nstream\nBT /F1 12 Tf 70 700 Td (Python SQL Docker FastAPI) Tj ET\nendstream\nendobj\nxref\n0 6\n0000000000 65535 f\n0000000009 00000 n\n0000000062 00000 n\n0000000107 00000 n\n0000000162 00000 n\n0000000253 00000 n\ntrailer\n<< /Size 6 /Root 2 0 R >>\nstartxref\n346\n%%EOF")

# Backend URL
url = "http://127.0.0.1:9000/api/analyze"

print("🚀 Starting Terminal-Based Analysis Test...")
try:
    with open(dummy_pdf_path, 'rb') as pdf_file:
        files = {'resume': (dummy_pdf_path, pdf_file, 'application/pdf')}
        data = {'target_role': 'Data Scientist'}
        response = requests.post(url, files=files, data=data)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print("\n✅ ANALYSIS SUCCESSFUL!")
        print(f"Target Role: {result['target_role']}")
        print(f"Match Score: {result['gap_analysis']['match_score']}%")
        print(f"Technical Skills Found: {result['technical_skills']}")
        print("\n--- JSON OUTPUT SNAPSHOT ---")
        print(json.dumps(result, indent=2)[:500] + "...")
    else:
        print(f"❌ Error: {response.text}")
except Exception as e:
    print(f"❌ Connection Failed: {str(e)}")
finally:
    if os.path.exists(dummy_pdf_path):
        os.remove(dummy_pdf_path)
