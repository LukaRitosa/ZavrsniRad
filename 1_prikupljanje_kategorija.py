import requests
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()

url = "https://data.g2.com/api/v2/categories/education" 
api_token = os.getenv("G2_API_TOKEN")

response = requests.get(url, headers={'Authorization': f'Bearer {api_token}'})
if response.ok:
  print(response.json())


r = requests.get(
    url,
    headers={"Authorization": f"Bearer {api_token}"},
    params={"page[size]": 3}
)

print(r.status_code)
print(json.dumps(r.json(), indent=2))

children_ids = [
    "a9413408-1cd3-4caf-8ba7-11a093c21739",
    "708cdbd5-e2c9-47ef-8f64-ab13d7e7112d",
    "8ae4469f-280d-4f5a-b6f5-9624204cf7e4",
    "20736f4d-2680-417f-954c-bc676b7b90cd",
    "ba1767af-bfa0-4b42-8084-a48dc55cae7f",
    "197c2974-6915-4af1-8884-c165b8d1599a",
    "1a143bfd-462b-4ab5-91a9-650bcf80c4da",
    "1173512b-2493-471c-91d4-9b3b686074b2",
    "a9c9e9b8-9344-4412-ad45-26a71d117228",
    "757da3f1-9a28-418d-8a15-002e47c96918",
    "824b713f-3f29-47d7-afd4-5dfb6204a99c",
    "63ca5357-8e1c-4764-ac14-4df923ba9786",
    "20ebce90-e7c6-47f7-b460-d1546e00f52f",
    "31e6a532-241e-4bbb-a192-d2ae057a0d6b",
    "a756379e-7d00-46d8-b9b6-362c14fe4c7d",
    "9d8c7023-c280-4ded-9581-a963cc68f05c",
    "c5484ced-0d8f-4221-98df-d924cbd3ee7b",
    "7b57d593-ec33-469d-9f7a-d151e8e57a97",
    "32d0a3b1-dc2d-4826-a6eb-d4111cf11f5e",
    "7a0271f6-e1ec-4825-b200-d15aede21be3",
    "15d20c82-1010-4a91-b44e-30781db90a70",
    "03e6ad15-c113-481d-9b61-99a7a6e12f82",
    "5165eab1-0d94-4fe7-9790-1b0f1c00cfc1",
    "604c173c-bfb2-4a38-9b7d-a3223a53af77",
    "ff0e4d5e-da48-4764-a756-ffd4396022a3",
    "9615de8c-6b84-45e3-9380-80908d0f7e62",
    "52d6dac8-a73d-4a9f-97f0-03c044c75745",
    "285afd6f-1bcf-4b43-a9e8-37dbb06ab12b",
    "7e81ccb2-7183-4089-9963-59b9c3f21cd0"
]



brojac = 1
for cid in children_ids:
    r = requests.get(
        f"https://data.g2.com/api/v2/categories/{cid}",
        headers={"Authorization": f"Bearer {api_token}"}
    )
    name = r.json()['data']['attributes']['name']
    slug = r.json()['data']['attributes']['slug']
    print(f"{brojac} | {cid} | {name} | {slug}")
    brojac+=1
    time.sleep(0.5)



'''
{'data': {'id': 'd85ba01c-66b2-43f1-b80a-233adb5097bd', 'type': 'categories', 'attributes': {'uuid': 'd85ba01c-66b2-43f1-b80a-233adb5097bd', 'name': 'Education', 'slug': 'education', 'description': 'Educational software helps automate and streamline educational programs, enhancing the teaching and learning experience. This enables organizations to offer personalized learning pathways that meet the unique needs of each student, improving their engagement and instructional outcomes. The software also supports automated grading and assessment, significantly reducing the administrative burden on teachers. Allowing them to spend more time on instruction and student interaction. Education software integrates real-time analytics to provide immediate feedback on student performance. This helps educators identify and address learning gaps promptly. These educational tools also offer robust accessibility features. This ensures that academic content is available to students anytime and anywhere, facilitating traditional and online learning environments. Best education software at a glance: Best language learning software: Speexx Best online learning platform: Udemy Best learning management system: Google Classroom Best school management software: Gaggle Best study tool: Kahoot! Best classroom management software: Lumio Best virtual classroom software: Zoom Workplace Best assessment software: Canvas LMS Best digital learning platform: Canvas LMS Best reference management software: EasyBib.com These software solutions are ranked using an algorithm that calculates customer satisfaction and market presence based on reviews from our user community. For more information, please check out G2’s Research Scoring Methodology.', 'updated_at': '2026-06-26T05:00:04.966-05:00'}, 'relationships': {'products': {'data': [{'id': '090c6f73-9bae-4323-98ac-8880acea7fbd', 'type': 'products'}, {'id': 'b587a293-4c04-4ac3-9237-38ad5b96c780', 'type': 'products'}, {'id': '7c61b99e-cd91-4479-87f6-3de05116e997', 'type': 'products'}, {'id': '004a03ba-687f-4f65-9814-3bd0b40ace88', 'type': 'products'}, {'id': '29bfb1b3-7aa4-4f29-aef3-bd05868b0c6c', 'type': 'products'}], 'links': {'related': 'https://data.g2.com/api/v2/products?filter%5Bcategory_id%5D=d85ba01c-66b2-43f1-b80a-233adb5097bd'}}, 'children': {'data': [{'id': '197c2974-6915-4af1-8884-c165b8d1599a', 'type': 'product_categories'}, {'id': '1a143bfd-462b-4ab5-91a9-650bcf80c4da', 'type': 'product_categories'}, {'id': '757da3f1-9a28-418d-8a15-002e47c96918', 'type': 'product_categories'}, {'id': '824b713f-3f29-47d7-afd4-5dfb6204a99c', 'type': 'product_categories'}, {'id': '20736f4d-2680-417f-954c-bc676b7b90cd', 'type': 'product_categories'}, {'id': 'a9413408-1cd3-4caf-8ba7-11a093c21739', 'type': 'product_categories'}, {'id': '708cdbd5-e2c9-47ef-8f64-ab13d7e7112d', 'type': 'product_categories'}, {'id': '8ae4469f-280d-4f5a-b6f5-9624204cf7e4', 'type': 'product_categories'}, {'id': 'ba1767af-bfa0-4b42-8084-a48dc55cae7f', 'type': 'product_categories'}, {'id': '1173512b-2493-471c-91d4-9b3b686074b2', 'type': 'product_categories'}, {'id': 'a9c9e9b8-9344-4412-ad45-26a71d117228', 'type': 'product_categories'}, {'id': '63ca5357-8e1c-4764-ac14-4df923ba9786', 'type': 'product_categories'}, {'id': '20ebce90-e7c6-47f7-b460-d1546e00f52f', 'type': 'product_categories'}, {'id': '31e6a532-241e-4bbb-a192-d2ae057a0d6b', 'type': 'product_categories'}, {'id': 'a756379e-7d00-46d8-b9b6-362c14fe4c7d', 'type': 'product_categories'}, {'id': '9d8c7023-c280-4ded-9581-a963cc68f05c', 'type': 'product_categories'}, {'id': 'c5484ced-0d8f-4221-98df-d924cbd3ee7b', 'type': 'product_categories'}, {'id': '7b57d593-ec33-469d-9f7a-d151e8e57a97', 'type': 'product_categories'}, {'id': '32d0a3b1-dc2d-4826-a6eb-d4111cf11f5e', 'type': 'product_categories'}, {'id': '7a0271f6-e1ec-4825-b200-d15aede21be3', 'type': 'product_categories'}, {'id': '15d20c82-1010-4a91-b44e-30781db90a70', 'type': 'product_categories'}, {'id': '03e6ad15-c113-481d-9b61-99a7a6e12f82', 'type': 'product_categories'}, {'id': '5165eab1-0d94-4fe7-9790-1b0f1c00cfc1', 'type': 'product_categories'}, {'id': '604c173c-bfb2-4a38-9b7d-a3223a53af77', 'type': 'product_categories'}, {'id': 'ff0e4d5e-da48-4764-a756-ffd4396022a3', 'type': 'product_categories'}, {'id': '9615de8c-6b84-45e3-9380-80908d0f7e62', 'type': 'product_categories'}, {'id': '52d6dac8-a73d-4a9f-97f0-03c044c75745', 'type': 'product_categories'}, {'id': '285afd6f-1bcf-4b43-a9e8-37dbb06ab12b', 'type': 'product_categories'}, {'id': '7e81ccb2-7183-4089-9963-59b9c3f21cd0', 'type': 'product_categories'}]}, 'ancestors': {'data': [{'id': '8da60a60-2e7f-44e9-84b8-4cfd2ed906ce', 'type': 'product_categories'}, {'id': '49712931-78c9-4e72-acc8-54ce84a8cdf9', 'type': 'product_categories'}, {'id': '583ed413-55c8-4c6a-a6b7-a6dbf742c8dc', 'type': 'product_categories'}]}, 'descendants': {'data': [{'id': '708cdbd5-e2c9-47ef-8f64-ab13d7e7112d', 'type': 'product_categories'}, {'id': '7b57d593-ec33-469d-9f7a-d151e8e57a97', 'type': 'product_categories'}, {'id': '20736f4d-2680-417f-954c-bc676b7b90cd', 'type': 'product_categories'}, {'id': '9615de8c-6b84-45e3-9380-80908d0f7e62', 'type': 'product_categories'}, {'id': 'ca035483-baf6-4d4f-9b39-8c67ed34d90f', 'type': 'product_categories'}, {'id': '285afd6f-1bcf-4b43-a9e8-37dbb06ab12b', 'type': 'product_categories'}, {'id': '2145b4ff-108a-4492-b330-8473f0096b2c', 'type': 'product_categories'}, {'id': '1173512b-2493-471c-91d4-9b3b686074b2', 'type': 'product_categories'}, {'id': '824b713f-3f29-47d7-afd4-5dfb6204a99c', 'type': 'product_categories'}, {'id': '32d0a3b1-dc2d-4826-a6eb-d4111cf11f5e', 'type': 'product_categories'}, {'id': 'f5cb3f92-9918-432e-91c6-863d6cb65b14', 'type': 'product_categories'}, {'id': '7a0271f6-e1ec-4825-b200-d15aede21be3', 'type': 'product_categories'}, {'id': '15d20c82-1010-4a91-b44e-30781db90a70', 'type': 'product_categories'}, {'id': '4363d625-8cc8-4275-8d5d-ae2a8258b050', 'type': 'product_categories'}, {'id': 'c5484ced-0d8f-4221-98df-d924cbd3ee7b', 'type': 'product_categories'}, {'id': '63ca5357-8e1c-4764-ac14-4df923ba9786', 'type': 'product_categories'}, {'id': 'a756379e-7d00-46d8-b9b6-362c14fe4c7d', 'type': 'product_categories'}, {'id': '31e6a532-241e-4bbb-a192-d2ae057a0d6b', 'type': 'product_categories'}, {'id': '7e81ccb2-7183-4089-9963-59b9c3f21cd0', 'type': 'product_categories'}, {'id': '757da3f1-9a28-418d-8a15-002e47c96918', 'type': 'product_categories'}, {'id': 'a9413408-1cd3-4caf-8ba7-11a093c21739', 'type': 'product_categories'}, {'id': '03e6ad15-c113-481d-9b61-99a7a6e12f82', 'type': 'product_categories'}, {'id': 'a9c9e9b8-9344-4412-ad45-26a71d117228', 'type': 'product_categories'}, {'id': '1a143bfd-462b-4ab5-91a9-650bcf80c4da', 'type': 'product_categories'}, {'id': '8ae4469f-280d-4f5a-b6f5-9624204cf7e4', 'type': 'product_categories'}, {'id': '197c2974-6915-4af1-8884-c165b8d1599a', 'type': 'product_categories'}, {'id': '52d6dac8-a73d-4a9f-97f0-03c044c75745', 'type': 'product_categories'}, {'id': '604c173c-bfb2-4a38-9b7d-a3223a53af77', 'type': 'product_categories'}, {'id': '9d8c7023-c280-4ded-9581-a963cc68f05c', 'type': 'product_categories'}, {'id': '20ebce90-e7c6-47f7-b460-d1546e00f52f', 'type': 'product_categories'}, {'id': '5165eab1-0d94-4fe7-9790-1b0f1c00cfc1', 'type': 'product_categories'}, {'id': 'ba1767af-bfa0-4b42-8084-a48dc55cae7f', 'type': 'product_categories'}, {'id': 'ff0e4d5e-da48-4764-a756-ffd4396022a3', 'type': 'product_categories'}, {'id': 'f9b78303-0d93-4b76-9605-08b472606f36', 'type': 'product_categories'}]}, 'parent': {'data': {'id': '583ed413-55c8-4c6a-a6b7-a6dbf742c8dc', 'type': 'product_categories'}}}}}
200
{
  "data": {
    "id": "d85ba01c-66b2-43f1-b80a-233adb5097bd",
    "type": "categories",
    "attributes": {
      "uuid": "d85ba01c-66b2-43f1-b80a-233adb5097bd",
      "name": "Education",
      "slug": "education",
      "description": "Educational software helps automate and streamline educational programs, enhancing the teaching and learning experience. This enables organizations to offer personalized learning pathways that meet the unique needs of each student, improving their engagement and instructional outcomes. The software also supports automated grading and assessment, significantly reducing the administrative burden on teachers. Allowing them to spend more time on instruction and student interaction. Education software integrates real-time analytics to provide immediate feedback on student performance. This helps educators identify and address learning gaps promptly. These educational tools also offer robust accessibility features. This ensures that academic content is available to students anytime and anywhere, facilitating traditional and online learning environments. Best education software at a glance: Best language learning software: Speexx Best online learning platform: Udemy Best learning management system: Google Classroom Best school management software: Gaggle Best study tool: Kahoot! Best classroom management software: Lumio Best virtual classroom software: Zoom Workplace Best assessment software: Canvas LMS Best digital learning platform: Canvas LMS Best reference management software: EasyBib.com These software solutions are ranked using an algorithm that calculates customer satisfaction and market presence based on reviews from our user community. For more information, please check out G2\u2019s Research Scoring Methodology.",
      "updated_at": "2026-06-26T05:00:04.966-05:00"
    },
    "relationships": {
      "products": {
        "data": [
          {
            "id": "090c6f73-9bae-4323-98ac-8880acea7fbd",
            "type": "products"
          },
          {
            "id": "b587a293-4c04-4ac3-9237-38ad5b96c780",
            "type": "products"
          },
          {
            "id": "7c61b99e-cd91-4479-87f6-3de05116e997",
            "type": "products"
          },
          {
            "id": "004a03ba-687f-4f65-9814-3bd0b40ace88",
            "type": "products"
          },
          {
            "id": "29bfb1b3-7aa4-4f29-aef3-bd05868b0c6c",
            "type": "products"
          }
        ],
        "links": {
          "related": "https://data.g2.com/api/v2/products?filter%5Bcategory_id%5D=d85ba01c-66b2-43f1-b80a-233adb5097bd"
        }
      },
      "children": {
        "data": [
          {
            "id": "197c2974-6915-4af1-8884-c165b8d1599a",
            "type": "product_categories"
          },
          {
            "id": "1a143bfd-462b-4ab5-91a9-650bcf80c4da",
            "type": "product_categories"
          },
          {
            "id": "757da3f1-9a28-418d-8a15-002e47c96918",
            "type": "product_categories"
          },
          {
            "id": "824b713f-3f29-47d7-afd4-5dfb6204a99c",
            "type": "product_categories"
          },
          {
            "id": "20736f4d-2680-417f-954c-bc676b7b90cd",
            "type": "product_categories"
          },
          {
            "id": "a9413408-1cd3-4caf-8ba7-11a093c21739",
            "type": "product_categories"
          },
          {
            "id": "708cdbd5-e2c9-47ef-8f64-ab13d7e7112d",
            "type": "product_categories"
          },
          {
            "id": "8ae4469f-280d-4f5a-b6f5-9624204cf7e4",
            "type": "product_categories"
          },
          {
            "id": "ba1767af-bfa0-4b42-8084-a48dc55cae7f",
            "type": "product_categories"
          },
          {
            "id": "1173512b-2493-471c-91d4-9b3b686074b2",
            "type": "product_categories"
          },
          {
            "id": "a9c9e9b8-9344-4412-ad45-26a71d117228",
            "type": "product_categories"
          },
          {
            "id": "63ca5357-8e1c-4764-ac14-4df923ba9786",
            "type": "product_categories"
          },
          {
            "id": "20ebce90-e7c6-47f7-b460-d1546e00f52f",
            "type": "product_categories"
          },
          {
            "id": "31e6a532-241e-4bbb-a192-d2ae057a0d6b",
            "type": "product_categories"
          },
          {
            "id": "a756379e-7d00-46d8-b9b6-362c14fe4c7d",
            "type": "product_categories"
          },
          {
            "id": "9d8c7023-c280-4ded-9581-a963cc68f05c",
            "type": "product_categories"
          },
          {
            "id": "c5484ced-0d8f-4221-98df-d924cbd3ee7b",
            "type": "product_categories"
          },
          {
            "id": "7b57d593-ec33-469d-9f7a-d151e8e57a97",
            "type": "product_categories"
          },
          {
            "id": "32d0a3b1-dc2d-4826-a6eb-d4111cf11f5e",
            "type": "product_categories"
          },
          {
            "id": "7a0271f6-e1ec-4825-b200-d15aede21be3",
            "type": "product_categories"
          },
          {
            "id": "15d20c82-1010-4a91-b44e-30781db90a70",
            "type": "product_categories"
          },
          {
            "id": "03e6ad15-c113-481d-9b61-99a7a6e12f82",
            "type": "product_categories"
          },
          {
            "id": "5165eab1-0d94-4fe7-9790-1b0f1c00cfc1",
            "type": "product_categories"
          },
          {
            "id": "604c173c-bfb2-4a38-9b7d-a3223a53af77",
            "type": "product_categories"
          },
          {
            "id": "ff0e4d5e-da48-4764-a756-ffd4396022a3",
            "type": "product_categories"
          },
          {
            "id": "9615de8c-6b84-45e3-9380-80908d0f7e62",
            "type": "product_categories"
          },
          {
            "id": "52d6dac8-a73d-4a9f-97f0-03c044c75745",
            "type": "product_categories"
          },
          {
            "id": "285afd6f-1bcf-4b43-a9e8-37dbb06ab12b",
            "type": "product_categories"
          },
          {
            "id": "7e81ccb2-7183-4089-9963-59b9c3f21cd0",
            "type": "product_categories"
          }
        ]
      },
      "ancestors": {
        "data": [
          {
            "id": "8da60a60-2e7f-44e9-84b8-4cfd2ed906ce",
            "type": "product_categories"
          },
          {
            "id": "49712931-78c9-4e72-acc8-54ce84a8cdf9",
            "type": "product_categories"
          },
          {
            "id": "583ed413-55c8-4c6a-a6b7-a6dbf742c8dc",
            "type": "product_categories"
          }
        ]
      },
      "descendants": {
        "data": [
          {
            "id": "708cdbd5-e2c9-47ef-8f64-ab13d7e7112d",
            "type": "product_categories"
          },
          {
            "id": "7b57d593-ec33-469d-9f7a-d151e8e57a97",
            "type": "product_categories"
          },
          {
            "id": "20736f4d-2680-417f-954c-bc676b7b90cd",
            "type": "product_categories"
          },
          {
            "id": "9615de8c-6b84-45e3-9380-80908d0f7e62",
            "type": "product_categories"
          },
          {
            "id": "ca035483-baf6-4d4f-9b39-8c67ed34d90f",
            "type": "product_categories"
          },
          {
            "id": "285afd6f-1bcf-4b43-a9e8-37dbb06ab12b",
            "type": "product_categories"
          },
          {
            "id": "2145b4ff-108a-4492-b330-8473f0096b2c",
            "type": "product_categories"
          },
          {
            "id": "1173512b-2493-471c-91d4-9b3b686074b2",
            "type": "product_categories"
          },
          {
            "id": "824b713f-3f29-47d7-afd4-5dfb6204a99c",
            "type": "product_categories"
          },
          {
            "id": "32d0a3b1-dc2d-4826-a6eb-d4111cf11f5e",
            "type": "product_categories"
          },
          {
            "id": "f5cb3f92-9918-432e-91c6-863d6cb65b14",
            "type": "product_categories"
          },
          {
            "id": "7a0271f6-e1ec-4825-b200-d15aede21be3",
            "type": "product_categories"
          },
          {
            "id": "15d20c82-1010-4a91-b44e-30781db90a70",
            "type": "product_categories"
          },
          {
            "id": "4363d625-8cc8-4275-8d5d-ae2a8258b050",
            "type": "product_categories"
          },
          {
            "id": "c5484ced-0d8f-4221-98df-d924cbd3ee7b",
            "type": "product_categories"
          },
          {
            "id": "63ca5357-8e1c-4764-ac14-4df923ba9786",
            "type": "product_categories"
          },
          {
            "id": "a756379e-7d00-46d8-b9b6-362c14fe4c7d",
            "type": "product_categories"
          },
          {
            "id": "31e6a532-241e-4bbb-a192-d2ae057a0d6b",
            "type": "product_categories"
          },
          {
            "id": "7e81ccb2-7183-4089-9963-59b9c3f21cd0",
            "type": "product_categories"
          },
          {
            "id": "757da3f1-9a28-418d-8a15-002e47c96918",
            "type": "product_categories"
          },
          {
            "id": "a9413408-1cd3-4caf-8ba7-11a093c21739",
            "type": "product_categories"
          },
          {
            "id": "03e6ad15-c113-481d-9b61-99a7a6e12f82",
            "type": "product_categories"
          },
          {
            "id": "a9c9e9b8-9344-4412-ad45-26a71d117228",
            "type": "product_categories"
          },
          {
            "id": "1a143bfd-462b-4ab5-91a9-650bcf80c4da",
            "type": "product_categories"
          },
          {
            "id": "8ae4469f-280d-4f5a-b6f5-9624204cf7e4",
            "type": "product_categories"
          },
          {
            "id": "197c2974-6915-4af1-8884-c165b8d1599a",
            "type": "product_categories"
          },
          {
            "id": "52d6dac8-a73d-4a9f-97f0-03c044c75745",
            "type": "product_categories"
          },
          {
            "id": "604c173c-bfb2-4a38-9b7d-a3223a53af77",
            "type": "product_categories"
          },
          {
            "id": "9d8c7023-c280-4ded-9581-a963cc68f05c",
            "type": "product_categories"
          },
          {
            "id": "20ebce90-e7c6-47f7-b460-d1546e00f52f",
            "type": "product_categories"
          },
          {
            "id": "5165eab1-0d94-4fe7-9790-1b0f1c00cfc1",
            "type": "product_categories"
          },
          {
            "id": "ba1767af-bfa0-4b42-8084-a48dc55cae7f",
            "type": "product_categories"
          },
          {
            "id": "ff0e4d5e-da48-4764-a756-ffd4396022a3",
            "type": "product_categories"
          },
          {
            "id": "f9b78303-0d93-4b76-9605-08b472606f36",
            "type": "product_categories"
          }
        ]
      },
      "parent": {
        "data": {
          "id": "583ed413-55c8-4c6a-a6b7-a6dbf742c8dc",
          "type": "product_categories"
        }
      }
    }
  }
}
1 | a9413408-1cd3-4caf-8ba7-11a093c21739 | Online Learning Platform | online-learning-platform
2 | 708cdbd5-e2c9-47ef-8f64-ab13d7e7112d | Special Education | special-education
3 | 8ae4469f-280d-4f5a-b6f5-9624204cf7e4 | Language Learning | language-learning
4 | 20736f4d-2680-417f-954c-bc676b7b90cd | School Management | school-management-software
5 | ba1767af-bfa0-4b42-8084-a48dc55cae7f | Learning Management System (LMS) | learning-management-system-lms
6 | 197c2974-6915-4af1-8884-c165b8d1599a | Other Education | other-education
7 | 1a143bfd-462b-4ab5-91a9-650bcf80c4da | Reference Management | reference-management
8 | 1173512b-2493-471c-91d4-9b3b686074b2 | Student Information Systems (SIS) | student-information-systems-sis
9 | a9c9e9b8-9344-4412-ad45-26a71d117228 | Online Course Providers | online-course-providers
10 | 757da3f1-9a28-418d-8a15-002e47c96918 | Technical Skills Development | technical-skills-development
11 | 824b713f-3f29-47d7-afd4-5dfb6204a99c | Digital Learning Platforms | digital-learning-platforms
12 | 63ca5357-8e1c-4764-ac14-4df923ba9786 | AI Grading Tools | ai-grading-tools
13 | 20ebce90-e7c6-47f7-b460-d1546e00f52f | Academic Scheduling | academic-scheduling
14 | 31e6a532-241e-4bbb-a192-d2ae057a0d6b | Virtual Classroom | virtual-classroom
15 | a756379e-7d00-46d8-b9b6-362c14fe4c7d | Admissions and Enrollment Management | admissions-and-enrollment-management
16 | 9d8c7023-c280-4ded-9581-a963cc68f05c | Education ERP | education-erp
17 | c5484ced-0d8f-4221-98df-d924cbd3ee7b | Student Health Records | student-health-records
18 | 7b57d593-ec33-469d-9f7a-d151e8e57a97 | Library Management Systems | library-management-systems
19 | 32d0a3b1-dc2d-4826-a6eb-d4111cf11f5e | Assessment | assessment
20 | 7a0271f6-e1ec-4825-b200-d15aede21be3 | Online Proctoring | online-proctoring
21 | 15d20c82-1010-4a91-b44e-30781db90a70 | Scholarship Management | scholarship-management
22 | 03e6ad15-c113-481d-9b61-99a7a6e12f82 | Tutoring | tutoring
23 | 5165eab1-0d94-4fe7-9790-1b0f1c00cfc1 | Classroom Management | classroom-management
24 | 604c173c-bfb2-4a38-9b7d-a3223a53af77 | Academic Advising | academic-advising
25 | ff0e4d5e-da48-4764-a756-ffd4396022a3 | School Transportation | school-transportation
26 | 9615de8c-6b84-45e3-9380-80908d0f7e62 | Financial Aid Software | financial-aid-software
27 | 52d6dac8-a73d-4a9f-97f0-03c044c75745 | Study Tools | study-tools
28 | 285afd6f-1bcf-4b43-a9e8-37dbb06ab12b | Curriculum Management | curriculum-management
29 | 7e81ccb2-7183-4089-9963-59b9c3f21cd0 | Classroom Messaging | classroom-messaging
'''


'''    
14 31e6a532-241e-4bbb-a192-d2ae057a0d6b - Virtual Classroom - virtual-classroom
19 32d0a3b1-dc2d-4826-a6eb-d4111cf11f5e - Assessment - assessment
23 5165eab1-0d94-4fe7-9790-1b0f1c00cfc1 - Classroom Management - classroom-management
27 52d6dac8-a73d-4a9f-97f0-03c044c75745 - Study Tools - study-tools
29 7e81ccb2-7183-4089-9963-59b9c3f21cd0 - Classroom Messaging - classroom-messaging
03 e6ad15-c113-481d-9b61-99a7a6e12f82 - Tutoring - tutoring
'''