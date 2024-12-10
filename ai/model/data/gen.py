import pandas as pd

data = [
     [1, "чтение книг, программирование игр", "Студент имеет хорошие навыки в программировании. Рекомендуется развивать проектные навыки и работать с более сложными задачами."],
    [2, "игры на компьютере, анализ данных", "Интересуется Python, но нужно больше практики. Рекомендуется освоить библиотеки Python, такие как pandas и numpy."],
    [3, "спорт, разработки на Java", "Хорошие знания Java, но необходимо углубить навыки в многозадачности и многопоточности."],
    [4, "путешествия, системное администрирование", "Отличные знания в backend, рекомендуется изучить масштабируемость и микросервисную архитектуру."],
    [5, "музыка, работа с интерфейсами", "Проявляет интерес к фронтенду, работает с JavaScript. Рекомендуется углубить знания о фреймворках, таких как React или Vue."],
    [6, "рисование, искусственный интеллект", "Очень интересуется нейронными сетями. Рекомендуется продолжать обучение и участвовать в проектах по машинному обучению."],
    [7, "фото, аналитика данных", "Отличные знания в области математики, рекомендуется изучать статистику и методы анализа данных для будущих исследований."],
    [8, "кулинария, обработка данных", "Проявляет хорошие аналитические способности. Рекомендуется больше работать с большими данными и изучать методы визуализации."],
    [9, "программирование игр, администрирование серверов", "Очень сильные навыки в fullstack разработке. Рекомендуется более активно работать с архитектурой приложений."],
    [10, "автомобили, сетевые технологии", "Хорошие знания сетевых технологий. Рекомендуется развивать навыки в области безопасности и администрирования."],
    [1, "книги, open-source проекты", "Проявляет интерес к программированию. Рекомендуется начать с работы над реальными проектами и углубить знания о структуре кода."],
    [2, "велоспорт, анализ данных", "Хорошие навыки в Python, требуется больше практики с реальными проектами, такими как обработка данных и машинное обучение."],
    [3, "аниме, Java-разработка", "Имеет сильные знания Java, но необходимо работать над навыками обработки исключений и многозадачности."],
    [4, "плавание, backend-разработка", "Хорошие навыки в backend-разработке, рекомендуется больше изучать вопросы масштабируемости и обработки данных."],
    [5, "футбол, работа с веб-интерфейсами", "Проявляет интерес к веб-разработке. Рекомендуется улучшить навыки в CSS и JavaScript, а также освоить фреймворки."],
    [6, "кино, нейронные сети", "Очень заинтересован в нейронных сетях, но необходимо больше практики в реальных проектах и изучение теории."],
    [7, "компьютерные сети, математика", "Проявляет высокий интерес к математике, рекомендуется углубить знания в области статистики и машинного обучения."],
    [8, "финансовое планирование, анализ больших данных", "Хорошие аналитические способности, требуется больше практики с обработкой данных и машинным обучением."],
    [9, "психология, fullstack разработка", "Сильные технические навыки как в backend, так и во фронтенде. Рекомендуется больше уделить времени архитектуре приложений."],
    [10, "видеоблогинг, системное администрирование", "Проявляет интерес к сетям и связи, нужно развивать навыки в области администрирования и обеспечения безопасности."],
    [1, "научная работа, искусственный интеллект", "Имеет отличные навыки в программировании, но необходимо больше практики с алгоритмами и проектами."],
    [2, "велоспорт, автоматизация процессов", "Проявляет интерес к Python. Рекомендуется продолжить изучение машинного обучения и углубиться в практическое применение."],
    [1, "программирование на C++, создание игр", "Студент имеет глубокие знания C++. Рекомендуется работать над проектами в области игр и алгоритмов."],
    [3, "разработка приложений для Android, Java", "Знания Java на высоком уровне. Рекомендуется изучить паттерны проектирования для улучшения качества кода."],
    [5, "фронтенд-разработка, работа с React", "Активно работает с React. Рекомендуется углубить знания о менеджерах состояний, таких как Redux."],
    [4, "системное администрирование, работа с серверами", "Имеет хорошие навыки в администрировании серверов. Рекомендуется изучить инфраструктуру как код (IaC)."],
    [6, "искусственный интеллект, работа с TensorFlow", "Студент активно работает с нейронными сетями. Рекомендуется углубить знания о трансформерах и улучшить практические навыки."],
    [7, "анализ данных, математические модели", "Имеет хорошие знания математических моделей. Рекомендуется изучать статистику и методы машинного обучения."],
    [8, "data science, работа с большими данными", "Проявляет интерес к анализу данных. Рекомендуется продолжить изучение Python и библиотек для обработки данных."],
    [9, "разработка на Python, автоматизация", "Хорошие знания Python, рекомендовано расширить опыт работы с фреймворками для автоматизации процессов."],
    [10, "администрирование сетей, работа с Cisco", "Знания сетевых технологий. Рекомендуется углубить знания о безопасности сетей и маршрутизации."],
    [1, "создание веб-сайтов, JavaScript", "Хорошие навыки в JavaScript. Рекомендуется изучить новые фреймворки, такие как Angular или Vue."],
    [2, "обработка данных, анализ с использованием Python", "Имеет опыт работы с Python. Рекомендуется улучшить знания pandas и matplotlib для более качественного анализа."],
    [3, "разработка программного обеспечения на Java", "Активно работает с Java. Рекомендуется развивать навыки в многозадачности и многопоточности."],
    [4, "бэкенд-разработка на Python", "Хорошие навыки в Python. Рекомендуется изучить фреймворки Django и Flask для бэкенд-разработки."],
    [6, "нейронные сети, работа с Keras", "Имеет хорошие навыки в нейронных сетях. Рекомендуется углубить знания о deep learning и нейросетевых архитектурах."],
    [7, "математика, статистика, Python", "Хорошие знания математики и статистики. Рекомендуется углубить знания статистических методов и их применение в Python."],
    [8, "анализ данных, использование SQL", "Проявляет интерес к анализу данных. Рекомендуется изучить SQL и его применение в обработке больших данных."],
    [9, "fullstack разработка, JavaScript и Node.js", "Имеет опыт работы с JavaScript. Рекомендуется углубить знания о Node.js и серверной части разработки."],
    [10, "сетевые технологии, администрирование", "Хорошие знания сетевых технологий. Рекомендуется продолжить изучение маршрутизации и протоколов безопасности."],
    [1, "создание программ на Python, обработка текстов", "Активно использует Python. Рекомендуется изучить библиотеки для обработки текста и машинного обучения."],
    [5, "разработка веб-приложений, HTML/CSS", "Проявляет интерес к веб-разработке. Рекомендуется углубить знания в CSS и разработке адаптивных интерфейсов."],
    [2, "Python, анализ данных", "Хорошие знания Python. Рекомендуется углубить знания в области анализа данных и машинного обучения."],
    [3, "разработка на C#, работа с базами данных", "Имеет хорошие знания C#. Рекомендуется изучить методы работы с базами данных и оптимизацию запросов."],
    [4, "системное администрирование, автоматизация", "Хорошие знания Linux. Рекомендуется изучить инструменты для автоматизации администрирования."],
    [6, "нейронные сети, машинное обучение", "Интересуется нейронными сетями. Рекомендуется углубить знания по глубоком обучении и практике машинного обучения."],
    [7, "математика, алгоритмы", "Имеет хорошие знания алгоритмов. Рекомендуется углубить знания о математических методах и их применении."],
    [8, "анализ данных, использование R", "Проявляет интерес к анализу данных. Рекомендуется изучить R и его применение для статистического анализа."],
    [9, "разработка мобильных приложений, Swift", "Имеет хорошие знания Swift. Рекомендуется углубить знания о паттернах проектирования для мобильных приложений."],
    [10, "сетевые технологии, настройка маршрутизаторов", "Проявляет интерес к сетям. Рекомендуется продолжить изучение маршрутизации и сетевой безопасности."],
    [1, "разработка программных приложений, работа с C#", "Хорошие навыки программирования на C#. Рекомендуется изучить паттерны проектирования и улучшить практические навыки."],
    [2, "Python, веб-скрапинг", "Проявляет интерес к Python и веб-скрапингу. Рекомендуется изучить библиотеки BeautifulSoup и Scrapy для улучшения практических навыков."],
    [3, "разработка приложений для Android, Kotlin", "Активно использует Kotlin для разработки Android-приложений. Рекомендуется изучить архитектуру приложений и принципы разработки."],
    [4, "системное администрирование, работа с Docker", "Имеет хорошие навыки работы с Docker. Рекомендуется углубить знания о контейнеризации и Kubernetes для более гибкой работы."],
    [5, "frontend-разработка, создание SPA на Angular", "Имеет опыт работы с Angular. Рекомендуется изучить более сложные аспекты Angular, такие как состояние приложения и тестирование."],
    [6, "машинное обучение, работа с Scikit-learn", "Хорошие знания машинного обучения. Рекомендуется изучить более сложные алгоритмы и улучшить практическое применение в проектах."],
    [7, "математика, линейная алгебра", "Имеет хорошие знания линейной алгебры. Рекомендуется углубить знания в математических методах для анализа данных."],
    [8, "анализ больших данных, работа с Hadoop", "Проявляет интерес к анализу больших данных. Рекомендуется изучить Hadoop и его компоненты для обработки больших объемов данных."],
    [9, "разработка на Node.js, backend-разработка", "Проявляет хорошие знания в backend-разработке на Node.js. Рекомендуется изучить обработку асинхронных операций и тестирование API."],
    [10, "сетевые технологии, настройка VPN", "Проявляет интерес к сетевой безопасности. Рекомендуется изучить настройку и администрирование VPN для обеспечения безопасности данных."],
    [1, "программирование на C, разработка утилит", "Активно использует C для создания утилит. Рекомендуется углубить знания о системном программировании и многозадачности."],
    [2, "анализ данных с использованием Python, работа с TensorFlow", "Имеет хорошие знания Python. Рекомендуется изучить TensorFlow для работы с нейронными сетями и глубоким обучением."],
    [3, "разработка приложений на Java, алгоритмы", "Хорошие знания Java. Рекомендуется углубить знания в алгоритмах и структуре данных для улучшения производительности приложений."],
    [4, "системное администрирование, работа с виртуальными машинами", "Проявляет интерес к виртуализации. Рекомендуется изучить инструменты для управления виртуальными машинами, такие как VMware."],
    [5, "frontend-разработка, работа с Vue.js", "Имеет опыт работы с Vue.js. Рекомендуется улучшить навыки в создании интерактивных приложений и работе с состоянием."],
    [6, "нейронные сети, работа с PyTorch", "Проявляет интерес к нейронным сетям. Рекомендуется изучить PyTorch для создания более сложных моделей глубокого обучения."],
    [7, "математика, вычислительная геометрия", "Имеет хорошие знания в области вычислительной геометрии. Рекомендуется углубить знания математических алгоритмов для анализа данных."],
    [8, "анализ данных, машинное обучение", "Имеет опыт работы с анализом данных. Рекомендуется углубить знания в машинном обучении и работе с алгоритмами классификации."],
    [9, "разработка на Python, работа с Django", "Проявляет интерес к Python и веб-разработке. Рекомендуется углубить знания Django и изучить принципы MVC."],
    [10, "сетевые технологии, безопасность сетей", "Проявляет интерес к безопасности сетей. Рекомендуется изучить криптографию и методы защиты данных в сетях."],
    [1, "разработка на Java, создание приложений для бизнеса", "Хорошие знания Java. Рекомендуется углубить знания в области разработки корпоративных приложений и оптимизации бизнес-процессов."],
    [2, "анализ данных, работа с большими данными", "Имеет опыт работы с данными. Рекомендуется изучить методы работы с большими данными, такие как MapReduce и Hadoop."],
    [3, "разработка на C++, оптимизация программ", "Проявляет интерес к разработке на C++. Рекомендуется изучить методы оптимизации программ и работы с многозадачностью."],
    [4, "backend-разработка, работа с REST API", "Имеет опыт работы с REST API. Рекомендуется углубить знания в создании масштабируемых и отказоустойчивых сервисов."],
    [5, "frontend-разработка, работа с Vue.js", "Активно работает с Vue.js. Рекомендуется изучить Vuex для управления состоянием и улучшения производительности приложений."],
    [6, "нейронные сети, глубокое обучение", "Очень интересуется нейронными сетями. Рекомендуется продолжить обучение в области глубокого обучения и участвовать в реальных проектах."],
    [7, "математика, теории графов", "Имеет хорошие знания в теории графов. Рекомендуется углубить знания в области алгоритмов и их применении в машинном обучении."],
    [8, "анализ данных, SQL", "Проявляет интерес к анализу данных. Рекомендуется изучить SQL для работы с большими базами данных и эффективного извлечения информации."],
    [9, "fullstack-разработка, работа с Node.js и React", "Имеет опыт работы с Node.js и React. Рекомендуется углубить знания в области разработки fullstack-приложений."],
    [10, "сетевые технологии, работа с протоколами", "Проявляет интерес к сетевым протоколам. Рекомендуется изучить TCP/IP, а также методы диагностики и настройки сетевых соединений."],
      [1, "разработка игр, C#", "Хорошие знания C# для разработки игр. Рекомендуется изучить Unity для более эффективной работы в игровой разработке."],
    [2, "анализ данных, работа с библиотеками Python", "Имеет опыт работы с библиотеками Python, такими как pandas. Рекомендуется продолжить обучение в области анализа данных и машинного обучения."],
    [3, "разработка на Java, создание мобильных приложений", "Хорошие знания Java для мобильной разработки. Рекомендуется изучить Android SDK для создания качественных мобильных приложений."],
    [4, "системное администрирование, работа с сетями", "Проявляет интерес к настройке и управлению сетями. Рекомендуется углубить знания по безопасности и мониторингу сетевой инфраструктуры."],
    [5, "frontend-разработка, работа с Angular", "Имеет опыт работы с Angular. Рекомендуется изучить RxJS и другие библиотеки для работы с реактивным программированием."],
    [6, "искусственный интеллект, обработка естественного языка", "Проявляет интерес к искусственному интеллекту. Рекомендуется изучить библиотеки обработки естественного языка, такие как spaCy и NLTK."],
    [7, "математика, теоретическая информатика", "Имеет хорошие знания теоретической информатики. Рекомендуется углубить знания в области алгоритмов и теории сложности."],
    [8, "анализ данных, работа с Python", "Проявляет интерес к анализу данных. Рекомендуется углубить знания Python и изучить библиотеки для работы с большими данными, такие как Dask."],
    [9, "backend-разработка, работа с микросервисами", "Имеет опыт работы с микросервисами. Рекомендуется изучить внедрение и управление микросервисной архитектурой в реальных проектах."],
    [10, "сети и связь, администрирование серверов", "Проявляет интерес к администрированию серверов. Рекомендуется изучить практики по обеспечению безопасности серверов и управления ими."],
    [1, "разработка игр, 3D-графика", "Проявляет интерес к 3D-графике. Рекомендуется изучить основы OpenGL и DirectX для создания визуально насыщенных игр."],
    [2, "анализ данных, машинное обучение на Python", "Хорошие навыки в Python и машинном обучении. Рекомендуется углубить знания в области обработки данных и применении алгоритмов."],
    [3, "разработка на Java, работа с многозадачностью", "Проявляет интерес к многозадачности в Java. Рекомендуется изучить многопоточность и работу с асинхронными задачами."],
    [4, "системное администрирование, управление облачными инфраструктурами", "Проявляет интерес к облачным технологиям. Рекомендуется изучить управление инфраструктурой в облаке с использованием AWS или Azure."],
    [5, "frontend-разработка, работа с SASS", "Проявляет интерес к CSS-препроцессорам. Рекомендуется углубить знания о SASS и его возможностях для более гибкой стилизации."],
    [6, "нейронные сети, работа с TensorFlow", "Проявляет интерес к глубоким нейронным сетям. Рекомендуется изучить TensorFlow для более глубокого понимания нейросетей и их применения."],
    [7, "математика, численные методы", "Имеет хорошие знания в численных методах. Рекомендуется изучить методы численного интегрирования и их применение в науке."],
    [8, "анализ данных, создание визуализаций", "Проявляет интерес к визуализации данных. Рекомендуется изучить библиотеки, такие как Matplotlib и Seaborn для создания графиков и диаграмм."],
    [9, "fullstack-разработка, работа с TypeScript", "Хорошие навыки работы с TypeScript. Рекомендуется углубить знания о типизации и объектно-ориентированном программировании в TypeScript."],
    [10, "сетевые технологии, работа с SNMP", "Проявляет интерес к управлению сетями. Рекомендуется изучить протокол SNMP для мониторинга и управления сетевыми устройствами."],
    [1, "программирование на Python, создание API", "Имеет опыт создания REST API на Python. Рекомендуется изучить методы авторизации и безопасности API."],
    [2, "анализ данных, обработка текстов", "Проявляет интерес к обработке текстов с использованием Python. Рекомендуется изучить библиотеки для обработки текстов, такие как NLTK."],
    [3, "разработка на Java, работа с веб-технологиями", "Проявляет интерес к веб-разработке на Java. Рекомендуется изучить фреймворки, такие как Spring, для создания веб-приложений."],
    [4, "системное администрирование, управление базами данных", "Проявляет интерес к администрированию баз данных. Рекомендуется углубить знания по SQL и настройке производительных баз данных."],
    [5, "frontend-разработка, работа с Webpack", "Проявляет интерес к сборщикам для фронтенда. Рекомендуется изучить Webpack для более эффективного управления зависимостями и сборки проекта."],
    [6, "нейронные сети, обучение без учителя", "Проявляет интерес к методам обучения без учителя. Рекомендуется изучить алгоритмы кластеризации и их практическое применение."],
    [7, "математика, теоремы вероятности", "Имеет хорошие знания теории вероятностей. Рекомендуется углубить знания в статистике и их применении в машинном обучении."],
    [8, "анализ данных, работа с R", "Имеет интерес к анализу данных с использованием R. Рекомендуется изучить библиотеки для обработки данных, такие как dplyr и ggplot2."],
    [9, "fullstack-разработка, работа с MongoDB", "Имеет опыт работы с MongoDB. Рекомендуется изучить более сложные вопросы проектирования и оптимизации баз данных."],
    [10, "сетевые технологии, работа с DNS", "Проявляет интерес к DNS. Рекомендуется изучить работу с DNS-серверами и управление доменными именами в сети."],
    
]

# Создаем DataFrame
df = pd.DataFrame(data, columns=["Классы", "Хобби", "Рекомендации"])

# Печать первых строк для проверки
df.to_csv("./model/data/dataset_for_nn.csv", index=False, encoding="utf-8")