import xmltodict  # XML을 파이썬 딕셔너리로 변환
import yaml       # 파이썬 딕셔너리를 YAML로 변환
import json

def convert_xml_to_yaml(xml_file, yaml_file):
    """XML 파일을 읽어 YAML 파일로 변환하여 저장합니다."""

    # 1. XML 파일을 읽어 파이썬 딕셔너리(Dictionary)로 변환
    with open(xml_file, 'r', encoding='utf-8') as f:
        xml_string = f.read()

    data_dict = xmltodict.parse(xml_string)

    # (선택) 변환된 딕셔너리 구조 중간 확인
    # print(json.dumps(data_dict, indent=2, ensure_ascii=False))

    # 2. 딕셔너리를 YAML 형식의 문자열로 변환
    # allow_unicode=True: 한글이 깨지지 않게 처리
    # sort_keys=False: 원래 순서 유지
    yaml_string = yaml.dump(data_dict, allow_unicode=True, sort_keys=False, indent=2)

    # 3. YAML 문자열을 파일로 저장
    with open(yaml_file, 'w', encoding='utf-8') as f:
        f.write(yaml_string)

    print(f"✅ 변환 완료: '{xml_file}' -> '{yaml_file}'")


# 스크립트 실행
if __name__ == '__main__':
    convert_xml_to_yaml('my_data.xml', 'my_data_from_python.yaml')