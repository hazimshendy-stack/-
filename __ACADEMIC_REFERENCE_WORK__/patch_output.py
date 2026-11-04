import re

OUT = '__ACADEMIC_REFERENCE_OUTPUT__/index.html'
src = open(OUT, encoding='utf-8').read()
orig_len = len(src)

# ---------- 1) provenance tag on practice bank heading ----------
old = '<h2><span class="number">١٨</span> بنك المسائل والتمارين المتدرجة (مع الحلول النموذجية المخفية)</h2>'
assert src.count(old) == 1
src = src.replace(old, '<h2><span class="number">١٨</span> [E] بنك المسائل والتمارين المتدرجة (مع الحلول النموذجية المخفية)</h2>', 1)

# ---------- 2) new graded problems appended inside section 18 ----------
i = src.find('<section id="sec-practice-bank">')
end = src.find('  </section>', i)
assert i > 0 and end > i

P5 = '''    <!-- Problem 5 -->
    <details>
      <summary>مسألة ٥: تصنيف النقاط الحرجة بمميز هسيان (<span class="english">Hessian discriminant</span>) — مستوى متوسط <span class="english">[E]</span></summary>
      <div class="inside">
        <p><strong>المسألة:</strong> صنّف جميع النقاط الحرجة للدالة <span class="formula">f(x, y) = x^3 - 3xy + y^3</span>.</p>
        <p><strong>الحل النموذجي خطوة بخطوة:</strong></p>
        <ol>
          <li><strong>المشتقتان الجزئيتان الأولى:</strong>
            <span class="formula">f_x = 3x^2 - 3y</span> و <span class="formula">f_y = 3y^2 - 3x</span>.
          </li>
          <li><strong>حل النظام <span class="formula">f_x = 0,\\ f_y = 0</span>:</strong>
            من المعادلة الأولى <span class="formula">y = x^2</span>؛ بالتعويض في الثانية:
            <span class="formula">3(x^2)^2 - 3x = 0 \\implies 3x^4 - 3x = 0 \\implies 3x(x^3 - 1) = 0</span>،
            ومن ثم <span class="formula">x = 0</span> أو <span class="formula">x = 1</span>. النقاط الحرجة هي <span class="formula">(0, 0)</span> و <span class="formula">(1, 1)</span>.
          </li>
          <li><strong>المشتقات الثانية والمميز:</strong>
            <span class="formula">f_{xx} = 6x</span>، <span class="formula">f_{yy} = 6y</span>، <span class="formula">f_{xy} = -3</span>،
            والمميز هو <span class="formula">D = f_{xx} f_{yy} - (f_{xy})^2 = 36xy - 9</span>.
          </li>
          <li><strong>التصنيف عند <span class="formula">(0,0)</span>:</strong>
            <span class="formula">D(0,0) = -9 &lt; 0</span> ⟹ <strong>نقطة سرج</strong> بحكم قاعدة القرار في القسم ١١.
          </li>
          <li><strong>التصنيف عند <span class="formula">(1,1)</span>:</strong>
            <span class="formula">D(1,1) = 27 &gt; 0</span> مع <span class="formula">f_{xx}(1,1) = 6 &gt; 0</span> ⟹ <strong>قيمة صغرى محلية</strong> مقدارها <span class="formula">f(1,1) = 1 - 3 + 1 = -1</span>.
          </li>
        </ol>
        <div class="recall">
          <span class="box-title">استرجاع نشط [E]: بيّن على ورقة خارجية لماذا لا يكفي تحقق <span class="formula">f_x = f_y = 0</span> لاستنتاج وجود قيمة قصوى، بالدراسة على المسار <span class="formula">y = x</span> قرب <span class="formula">(0,0)</span>.</span>
          <p><strong>معيار إثبات الإتقان:</strong> إنتاج المميز <span class="formula">D = 36xy - 9</span> وتصنيف النقطتين خلال دقيقتين دون الرجوع إلى القسم ١١.</p>
        </div>
      </div>
    </details>

'''

P6 = '''    <!-- Problem 6 -->
    <details>
      <summary>مسألة ٦: التحقق الصريح من مبرهنة غرين على دائرة الوحدة (<span class="english">Green's Theorem check</span>) — مستوى متقدم <span class="english">[E]</span></summary>
      <div class="inside">
        <p><strong>المسألة:</strong> تحقّق من مبرهنة غرين للحقل <span class="formula">\\mathbf{a} = (-y,\\ x)</span> على المنحنى <span class="formula">C: x^2 + y^2 = 1</span> باتجاه عكس عقارب الساعة.</p>
        <p><strong>الحل النموذجي خطوة بخطوة:</strong></p>
        <ol>
          <li><strong>الطرف الأول (تكامل المسار):</strong> نوسّط الدائرة بـ <span class="formula">x = \\cos t,\\ y = \\sin t,\\ 0 \\le t \\le 2\\pi</span> فيكون
            <span class="formula">dx = -\\sin t\\,dt</span> و <span class="formula">dy = \\cos t\\,dt</span>:
            <div class="formula" style="direction:ltr; text-align:center; margin:6px 0;">
              \\oint_C (-y)\\,dx + x\\,dy = \\int_0^{2\\pi} \\left[ (-\\sin t)(-\\sin t) + (\\cos t)(\\cos t) \\right] dt = \\int_0^{2\\pi} dt = 2\\pi
            </div>
          </li>
          <li><strong>الطرف الثاني (التكامل الثنائي):</strong> هنا <span class="formula">P = -y</span> و <span class="formula">Q = x</span> إذن
            <span class="formula">\\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y} = 1 - (-1) = 2</span>، ومنه
            <div class="formula" style="direction:ltr; text-align:center; margin:6px 0;">
              \\iint_D 2\\,dA = 2 \\cdot A(D) = 2\\pi
            </div>
          </li>
          <li><strong>الخلاصة:</strong> الطرفان متساويان (<span class="formula">2\\pi = 2\\pi</span>)، وهو تحقق صريح من صيغة المصدر (ص 146).</li>
        </ol>
        <div class="warning">
          <span class="box-title">خطأ شائع يجب تجنبه:</span>
          <p>حساب <span class="formula">Q_x - P_y</span> بوصله <span class="formula">1 - 1 = 0</span> بنسيان الإشارة السالبة في <span class="formula">P = -y</span>. قاعدة التصحيح: اكتب <span class="formula">P</span> و<span class="formula">Q</span> في عمودين منفصلين قبل الاشتقاق الجزئي.</p>
        </div>
      </div>
    </details>

'''

src = src[:end] + P5 + P6 + src[end:]

# ---------- 3) comparison box inserted at end of section 17 ----------
j = src.find('<section id="sec-vector-theorems">')
kend = src.find('  </section>', j)
assert j > 0 and kend > j
CMP = '''    <h3>١٧.٥ صندوق مقارنة استراتيجي بين المبرهنات التكاملية الثلاث (<span class="english">[E] Comparison</span>)</h3>
    <div class="comparison">
      <span class="box-title">[E] مقارنة: غرين ↔ ستوكس ↔ غاوس — أيّها أستخدم؟ (تنظيم استنتاجي للمادة، لا نص حرفي من المصدر)</span>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>وجه المقارنة</th>
              <th>مبرهنة غرين (<span class="english">Green</span>, ص 146)</th>
              <th>مبرهنة ستوكس (<span class="english">Stokes</span>, ص 148)</th>
              <th>مبرهنة التباعد (<span class="english">Gauss</span>, ص 140)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>الكيان الهندسي</strong></td>
              <td>منحنى مغلق <span class="formula">C</span> في المستوى يحصر منطقة <span class="formula">D</span>.</td>
              <td>منحنى مغلق <span class="formula">C</span> في الفضاء يحدّ سطوحاً <span class="formula">S</span>.</td>
              <td>سطح مغلق <span class="formula">S</span> يحصراً حجماً <span class="formula">V</span>.</td>
            </tr>
            <tr>
              <td><strong>الصيغة</strong></td>
              <td><span class="formula">\\oint_C P\\,dx + Q\\,dy = \\iint_D (Q_x - P_y)\\,dA</span></td>
              <td><span class="formula">\\oint_C \\mathbf{a}\\cdot d\\mathbf{r} = \\int_S (\\nabla \\times \\mathbf{a})\\cdot d\\mathbf{S}</span></td>
              <td><span class="formula">\\oint_S \\mathbf{a}\\cdot d\\mathbf{S} = \\int_V (\\nabla \\cdot \\mathbf{a})\\,dV</span></td>
            </tr>
            <tr>
              <td><strong>المؤثر المتجهي</strong></td>
              <td>الدوران القياسي ثنائي البعد <span class="formula">Q_x - P_y</span>.</td>
              <td>التكبير <span class="formula">\\nabla \\times \\mathbf{a}</span>.</td>
              <td>التباعد <span class="formula">\\nabla \\cdot \\mathbf{a}</span>.</td>
            </tr>
            <tr>
              <td><strong>الاتفاقية الاتجاهية</strong></td>
              <td>الاتجاه الموجب هو عكس عقارب الساعة.</td>
              <td>قاعدة اليد اليمنى بين اتجاه <span class="formula">C</span> ومتجه <span class="formula">d\\mathbf{S}</span>.</td>
              <td>متجه العنصر السطحي يشير إلى الخارج دائماً.</td>
            </tr>
            <tr>
              <td><strong>تطبيق إضافي وارد في المرجع</strong></td>
              <td>حساب المساحة بصيغة <span class="formula">A = \\tfrac{1}{2} \\oint_C x\\,dy - y\\,dx</span>.</td>
              <td>إثبات استقلال تكامل الدوران عن اختيار السطح ما دامت الحافة واحدة.</td>
              <td>استنتاج معادلة الاستمرارية للموائع (ص 145).</td>
            </tr>
            <tr>
              <td><strong>شرط الانطباق ومتى تفشل</strong></td>
              <td>يلزم انغلاق <span class="formula">C</span> واتصال المشتقات الجزئية داخل <span class="formula">D</span>.</td>
              <td>يلزم سطح مجزّأ ناعم وحقل قابل للاشتقاق عليه.</td>
              <td>يلزم أن يكون السطح <strong>مغلقاً</strong>؛ وإن كان مفتوحاً يُغلق بسطح تعويضي ثم يُطرح تكامله.</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p><strong>خلاصة قرار سريع [I]:</strong> «تدفق عبر سطح مغلق» ← غاوس؛ «دوران حول حافة مغلقة» ← ستوكس؛ «كلُّ شيء في المستوى <span class="formula">xy</span>» ← غرين، وهي الحالة الخاصة من ستوكس حين يكون متجه العنصر السطحي عمودياً ثابتاً.</p>
    </div>

'''
src = src[:kend] + CMP + src[kend:]

open(OUT, 'w', encoding='utf-8').write(src)
print("OK. size:", orig_len, "->", len(src))
