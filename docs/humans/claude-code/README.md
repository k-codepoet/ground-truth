# skills 개념잡기
### 만드는법 및 예시  
https://github.com/anthropics/skills  
### 기준  
Note: This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Skills standard, see agentskills.io.  
http://agentskills.io/  
### claude code가 스킬을 어떻게 로드하고 사용하게 되는지에 대한 구현부도 있음
https://github.com/agentskills/agentskills


# skills 만들어보기

### skill-creator
- claude.ai랑 claude code에 사용할수있는 skill을 구현

# plugin 개념
- 패키징

# plugin 만들어보기

### plugin-dev
- 내가 만든 claude code 기능을 패키징하는걸 도와줌

# marketplace 만들기

### 자동 등록
- GitHub에 `.claude-plugin/marketplace.json` 파일이 있는 repo를 만들면 **24시간 내 자동 검색/등록**됨
- 별도 제출 프로세스 없음

### 공식문서
- Marketplace Schema: https://docs.claude.com/en/docs/claude-code/plugin-marketplaces#marketplace-schema
- Plugins Reference: https://docs.claude.com/en/docs/claude-code/plugins-reference

### 필수 구조
```
my-marketplace/
├── .claude-plugin/
│   └── marketplace.json    ← 필수 위치
└── plugins/
    └── my-plugin/
        ├── .claude-plugin/
        │   └── plugin.json ← 플러그인 매니페스트
        └── commands/
```

### marketplace.json 필수 필드
```json
{
  "name": "my-marketplace",      // kebab-case, 공백 불가
  "owner": { "name": "author" }, // 필수
  "plugins": [{
    "name": "my-plugin",
    "source": "./plugins/my-plugin",
    "description": "설명"
  }]
}
```

### 사용법
```bash
# 마켓플레이스 추가
/plugin marketplace add owner/repo
/plugin marketplace add ./local-path

# 플러그인 설치
/plugin install plugin-name@marketplace-name
```