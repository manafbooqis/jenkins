# نص شرح العرض — Jenkins Tool CI/CD Basics

## 1. Introduction
السلام عليكم، مشروعنا اليوم عن أداة Jenkins واستخدامها في بناء CI Pipeline بسيط.
الفكرة الأساسية أن Jenkins يساعد فريق التطوير على تشغيل خطوات متكررة بشكل تلقائي مثل سحب الكود، تثبيت المتطلبات، وتشغيل الاختبارات.

## 2. What is Jenkins?
Jenkins هي أداة Automation مفتوحة المصدر تُستخدم كثيرًا في DevOps. بدل ما المطور يشغل الاختبارات يدويًا بعد كل تعديل، Jenkins يشغلها تلقائيًا بعد رفع الكود على GitHub.

## 3. What is CI?
CI تعني Continuous Integration. معناها أن المطورين يدمجون تعديلاتهم باستمرار، وكل تعديل يتم فحصه تلقائيًا عن طريق build و tests. هذا يساعدنا نكتشف الأخطاء بدري قبل ما تكبر المشكلة.

## 4. Project Architecture
المشروع يتكون من GitHub repository يحتوي على تطبيق Python بسيط، وملف requirements.txt للمتطلبات، وملف Jenkinsfile الذي يحدد مراحل الـ pipeline. Jenkins يسحب المشروع من GitHub، ثم يثبت pytest، وبعدها يشغل الاختبارات.

## 5. Pipeline Workflow
الـ pipeline عندنا فيها ثلاث مراحل:
1. Pull Code: سحب آخر نسخة من GitHub.
2. Install Dependencies: تثبيت المتطلبات من requirements.txt.
3. Run Tests: تشغيل الاختبارات باستخدام pytest.

## 6. Demo Explanation
في الديمو سنفتح Jenkins، ثم نشغل Build Now، وبعدها نراقب Console Output. إذا نجحت الاختبارات يظهر build باللون الأخضر. وإذا كان هناك خطأ في الكود أو الاختبار سيفشل الـ build، وهذا يوضح فائدة Jenkins في اكتشاف المشاكل مبكرًا.

## 7. Challenges
من المشاكل المتوقعة أن Jenkins لا يجد Python أو pip، والحل هو تثبيت Python وضبط PATH. أيضًا قد لا يستطيع Jenkins الوصول إلى GitHub إذا كان الرابط خطأ أو المستودع خاص بدون credentials.

## 8. Conclusion
في النهاية، تعلمنا كيف Jenkins يدخل في DevOps lifecycle من خلال أتمتة build و test. هذا يقلل العمل اليدوي، يرفع جودة الكود، ويساعد الفريق يكتشف الأخطاء بسرعة.
