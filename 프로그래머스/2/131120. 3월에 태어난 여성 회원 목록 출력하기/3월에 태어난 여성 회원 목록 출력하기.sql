-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER,Date_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH)='03' and TLNO IS NOT NULL and GENDER = 'W'
Order by member_id asc;