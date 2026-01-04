---
title: "Library 마이그레이션 순서 논의"
date: 2026-01-04
source: "gemify:draft 세션 - library 분류 체계 리팩토링"
type: conversation
status: raw
used_in: null
---

# Library 마이그레이션 순서 논의

## 맥락

library 분류 체계를 6대 domain에서 Type 기반으로 리팩토링하는 작업 진행 중.

## 논의 내용

- 기존 library 파일 37개 존재 (6대 domain 폴더 구조)
- 새 구조: principles/, decisions/, insights/, how-tos/, specs/
- 마이그레이션 시점 결정 필요

## 결정

**draft 완성 → migration 일괄 진행**

이유:
- draft에서 views 관련 설계도 함께 고도화 중
- 전체 그림이 완성된 후 일괄 마이그레이션이 효율적
- 중간에 구조가 바뀌면 두 번 작업해야 함
