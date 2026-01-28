import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from medicine.models import Medicine
from board.models import Post

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@test.com', 'admin123')
    print('Superuser created: admin / admin123')

# Create test user
if not User.objects.filter(username='testuser').exists():
    test_user = User.objects.create_user('testuser', 'test@test.com', 'test123')
    print('Test user created: testuser / test123')
else:
    test_user = User.objects.get(username='testuser')

# Create sample medicines
medicines_data = [
    {
        '약품명': '타이레놀정 500mg',
        '성분명': '아세트아미노펜',
        '효능': '해열, 진통',
        '용량': '1회 1정, 1일 3-4회',
        '주의사항': '간 질환자 주의, 음주 시 복용 금지',
        '회사명': '한국얀센'
    },
    {
        '약품명': '게보린정',
        '성분명': '아세트아미노펜, 에텐자미드',
        '효능': '두통, 치통, 발열 시 해열진통',
        '용량': '1회 1정, 1일 3회',
        '주의사항': '위장장애가 있는 환자 주의',
        '회사명': '삼진제약'
    },
    {
        '약품명': '박트로반연고',
        '성분명': '뮤피로신',
        '효능': '피부감염증 치료',
        '용량': '1일 2-3회 환부에 도포',
        '주의사항': '눈 주위 사용 금지',
        '회사명': 'GSK'
    },
    {
        '약품명': '아스피린',
        '성분명': '아세틸살리실산',
        '효능': '해열, 진통, 소염, 혈전 예방',
        '용량': '1회 500mg, 1일 3회',
        '주의사항': '출혈 위험, 위장장애 주의',
        '회사명': '바이엘'
    },
    {
        '약품명': '브루펜정',
        '성분명': '이부프로펜',
        '효능': '해열, 진통, 소염',
        '용량': '1회 200-400mg, 1일 3회',
        '주의사항': '공복 복용 피할 것',
        '회사명': '삼일제약'
    },
    {
        '약품명': '판시딜정',
        '성분명': '파모티딘',
        '효능': '위궤양, 십이지장궤양 치료',
        '용량': '1회 20mg, 1일 2회',
        '주의사항': '신장 질환자 용량 조절 필요',
        '회사명': '한국얀센'
    },
    {
        '약품명': '후시딘연고',
        '성분명': '푸시드산',
        '효능': '세균성 피부감염 치료',
        '용량': '1일 2-3회 환부 도포',
        '주의사항': '장기간 사용 금지',
        '회사명': '동화약품'
    },
    {
        '약품명': '지르텍정',
        '성분명': '세티리진',
        '효능': '알레르기성 비염, 두드러기',
        '용량': '1회 10mg, 1일 1회',
        '주의사항': '졸음 주의, 운전 주의',
        '회사명': 'UCB'
    },
    {
        '약품명': '베아제정',
        '성분명': '판크레아틴',
        '효능': '소화불량, 복부팽만',
        '용량': '1회 1-2정, 1일 3회 식후',
        '주의사항': '급성 췌장염 환자 금기',
        '회사명': '한국얀센'
    },
    {
        '약품명': '훼스탈플러스정',
        '성분명': '판크레아틴, 디메티콘',
        '효능': '소화불량, 복부팽만, 가스제거',
        '용량': '1회 1-2정, 1일 3회 식후',
        '주의사항': '췌장염 환자 주의',
        '회사명': '동아제약'
    },
    {
        '약품명': '큐렉솔캡슐',
        '성분명': '덱스트로메토르판',
        '효능': '기침 억제',
        '용량': '1회 1캡슐, 1일 3회',
        '주의사항': '운전 주의, 알코올 금지',
        '회사명': '일동제약'
    },
    {
        '약품명': '코푸시럽',
        '성분명': '구아이페네신',
        '효능': '가래 제거',
        '용량': '1회 10ml, 1일 3-4회',
        '주의사항': '충분한 수분 섭취 필요',
        '회사명': '한미약품'
    },
]

created_count = 0
for data in medicines_data:
    if not Medicine.objects.filter(약품명=data['약품명']).exists():
        Medicine.objects.create(**data)
        created_count += 1

print(f'{created_count} medicines created')

# Create sample board posts
posts_data = [
    {
        'title': '의약품 복용 시 주의사항',
        'content': '의약품을 복용할 때는 반드시 용법과 용량을 지켜야 합니다.\n특히 항생제는 의사의 처방대로 복용 기간을 완료해야 합니다.',
        'author': test_user
    },
    {
        'title': '타이레놀과 게보린 함께 복용 가능한가요?',
        'content': '두 약 모두 아세트아미노펜 성분이 포함되어 있어서\n함께 복용 시 과량 복용이 될 수 있으니 주의가 필요합니다.',
        'author': test_user
    },
    {
        'title': '알레르기 약 복용 시 졸음이 심해요',
        'content': '항히스타민제는 졸음을 유발할 수 있습니다.\n운전이나 위험한 작업은 피하시고, 졸음이 덜한 2세대 항히스타민제를 처방받는 것이 좋습니다.',
        'author': test_user
    },
]

created_posts = 0
for data in posts_data:
    if not Post.objects.filter(title=data['title']).exists():
        Post.objects.create(**data)
        created_posts += 1

print(f'{created_posts} posts created')
print('\nSample data creation completed!')
