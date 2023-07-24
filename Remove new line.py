def remove_newlines_from_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file_in:
            lines = file_in.readlines()
        # 줄바꿈을 제거한 내용으로 새로운 리스트 생성
        lines_without_newlines = [line.strip() for line in lines]
        with open(output_file, 'w', encoding='utf-8') as file_out:
            file_out.write('\n'.join(lines_without_newlines))
        print("줄바꿈 제거가 완료되었습니다.")
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    except Exception as e:
        print("오류가 발생했습니다:", e)

# 사용 예시
input_file_path = input("파일 경로를 입력해 주세요.: ")
output_file_path = 'output.txt'
remove_newlines_from_file(input_file_path, output_file_path)
