# Bilingual Routing

Use bilingual lookup when the user asks in Chinese, mixes Chinese and English,
or asks for Chinese/English comparison.

## Process

1. Extract Chinese golf terms from the question.
2. Search the local Chinese Markdown corpus first.
3. Map the rule number to English terms and search the English Markdown corpus.
4. Cross-check official online sources when the answer is contested or recent.
5. Answer in the user's language unless asked to translate.

## Common Term Map

| Chinese | English | Likely Rules |
|---|---|---|
| 比杆赛 | stroke play | Rule 3.3 |
| 比洞赛 | match play | Rule 3.2 |
| 发球区 | teeing area | Rule 6 |
| 一般区域 | general area | Definitions |
| 沙坑 | bunker | Rule 12 |
| 推杆果岭 / 果岭 | putting green | Rule 13 |
| 罚杆区 / 红桩 / 黄桩 | penalty area | Rule 17 |
| 出界 | out of bounds | Rule 18 |
| 暂定球 | provisional ball | Rule 18.3 |
| 不可打之球 | unplayable ball | Rule 19 |
| 散置障碍物 | loose impediment | Rule 15.1 |
| 可移动妨碍物 | movable obstruction | Rule 15.2 |
| 异常球场状况 | abnormal course condition | Rule 16.1 |
| 装备 | equipment | Definitions, Rule 4, Rule 11 |
| 球被移动 | ball moved | Rule 9 |
| 运动中球 | ball in motion | Rule 11 |
| 抛球 | drop | Rule 14.3 |
| 放置回原位 | replace | Rule 14.2 |
| 一般性处罚 | general penalty | Definitions |
