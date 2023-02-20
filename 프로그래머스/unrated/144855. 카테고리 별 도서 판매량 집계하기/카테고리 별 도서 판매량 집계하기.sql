-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK AS t1
NATURAL JOIN BOOK_SALES AS t2
WHERE
    YEAR(SALES_DATE) = 2022
    AND MONTH(SALES_DATE) = 01
GROUP BY CATEGORY
ORDER BY CATEGORY;