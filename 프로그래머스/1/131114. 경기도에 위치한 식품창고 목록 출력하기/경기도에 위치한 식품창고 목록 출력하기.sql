-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, CASE
                                                WHEN FREEZER_YN = 'Y' THEN 'Y'
                                                WHEN FREEZER_YN = 'N' THEN 'N'
                                                ELSE 'N'
                                            END AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '%경기도%'
ORDER BY WAREHOUSE_ID;