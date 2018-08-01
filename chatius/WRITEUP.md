# Chatius: Write-up

После перехода на сайт мы видим информативное описание, в котором говорится, что
за 1000 рефералов нам дадут приз. Ой, а 1000 — это много, да? Ну, такое.

Таск имеет два пути решения:

1. Ручками сделать 1001 аккаунт (единственное верное решение)
2. Написать скрипт, который сам бы регистрировал 1000 аккаунтов

Поскольку здесь всё настолько защищено, что даже нет подтверждения почты, мы просто
берём CSRF-токен на странице с регистрацией, генерируем рандомные имя и почту и спамим
своими аккаунтами очень мощный сервер из Парижа, на котором раньше хостили проекты по
Minecraft. [Скрипт для решения →](private/solve.py)

По достижении 1000 рефералов, на главной странице появится флаг.

Флаг: **uctf_l0ve_pr0t3cted_ch@ts**