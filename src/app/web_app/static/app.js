(function(){
    // --- Translations (English, Amharic, Afaan Oromo) ---
    const DICT = {
      en:{
        formTitle:" US DV Lottery Registration Form",
        personalSection:"A. Personal Information",
        labelFullName:"Full Legal Name (exactly as it appears on your passport or national ID)",
        labelGender:"Gender",
        genderMale:"Male", genderFemale:"Female",
        labelDOB:"Date of Birth (Gregorian calendar)",
        labelBirthCity:"City or town of birth",
        labelBirthCountry:"Country of birth",
        labelPhoto:"Upload a recent passport-style photo",
        req1:"Plain light background (white or cream)",
        req2:"No glasses, hats, or shadows",
        req3:"Face in the center, clearly visible",
        req4:"Photo taken within the last 6 months",
        req5:"JPEG, max size 240 KB, recommended 600×600 px",
        contactSection:"B. Contact Information",
        labelRegion:"Mailing address: Region",
        labelCity:"City",
        labelDistrict:"District (sub-city)",
        labelPhone:"Active phone number",
        labelEmail:"Email address",
        educationSection:"C. Education",
        labelEducation:"What is your highest level of education?",
        maritalSection:"D. Marital Status",
        labelMarital:"Select marital status",
        spouseTitle:"For Married Applicants — Spouse Information",
        labelSpouseName:"Spouse's full name",
        labelSpouseDOB:"Spouse's date of birth",
        labelSpouseCity:"Spouse birth city / town",
        labelSpouseCountry:"Spouse birth country",
        labelSpousePhoto:"Upload a recent passport-style photo of your spouse",
        childrenSection:"E. Children (under 21)",
        labelHasChildren:"Do you have children under 21?",
        labelChildrenCount:"If yes, how many?",
        paymentSection:"F. Payment Verification",
        paymentHint:"Please upload your payment receipt screenshot and ensure it clearly shows:",
        pay1:"Full name of the sender",
        pay2:"Transaction amount",
        pay3:"Transaction reference code",
        pay4:"Date & time of payment",
        submitText:"Submit Application"
      },
      am:{
        formTitle:"የUS DV ዎተሪ የምዝገባ ቅጽ",
        personalSection:"A. የግል መረጃ",
        labelFullName:"ሙሉ ሕጋዊ ስም (እንደ ፓስፖርት ወይም ብሔራዊ መታወቂያ)",
        labelGender:"ፆታ",
        genderMale:"ወንድ", genderFemale:"ሴት",
        labelDOB:"የትውልድ ቀን (ግሪጎሪያን)",
        labelBirthCity:"የትውልድ ከተማ/ከተማ",
        labelBirthCountry:"የትውልድ ሀገር",
        labelPhoto:"የፓስፖርት የምስል ማስገባት",
        req1:"ቀለም ቀላል መስመር (ነጭ ወይም cream)",
        req2:"መነጽር/ኮፊያ/ጥላ አይገኝ",
        req3:"ፊት በመሀከል በግልጽ መልኩ ይታያል",
        req4:"በመጨረሻ 6 ወር ውስጥ የተነሳ",
        req5:"JPEG, 240 KB ውስጥ, 600×600 px መመኪያ",
        contactSection:"B. የንግድ መረጃ",
        labelRegion:"አድራሻ - ክልል",
        labelCity:"ከተማ",
        labelDistrict:"የክፍለ ከተማ / ክፍል",
        labelPhone:"ንቁ ስልክ ቁጥር",
        labelEmail:"ኢሜይል",
        educationSection:"C. ትምህርት",
        labelEducation:"ከፍተኛ የትምህርት ደረጃዎ ምንድን ነው?",
        maritalSection:"D. የጋብቻ ሁኔታ",
        labelMarital:"የጋብቻ ሁኔታ ይምረጡ",
        spouseTitle:"E. የባልንጀራ መረጃ",
        labelSpouseName:"የባልንጀራ ሙሉ ስም",
        labelSpouseDOB:"የባልንጀራ የትውልድ ቀን",
        labelSpouseCity:"የባልንጀራ የትውልድ ከተማ",
        labelSpouseCountry:"የባልንጀራ የትውልድ ሀገር",
        labelSpousePhoto:"የባልንጀራ ፎቶ ያስገቡ",
        childrenSection:"F. ልጆች (21 ከታች)",
        labelHasChildren:"21 ከታች ልጆች አሉዎዎት?",
        labelChildrenCount:"እስከ ስንት ልጆች?",
        paymentSection:"G. የክፍያ ማረጋገጫ",
        paymentHint:"የክፍያ ስክሪንሹት እባክዎ ያስገቡ፡ እባክዎ እንዲህ እንዲያሳየው ያረጋግጡ፡",
        pay1:"የላኪው ሙሉ ስም",
        pay2:"የግዢ መጠን",
        pay3:"የግንኙነት መለያ ኮድ",
        pay4:"ቀን እና ሰዓት",
        submitText:"አቅርብ"
      },
      om:{
        formTitle:"Fuula Galmee US DV Lottarii",
        personalSection:"A. Odeeffannoo Dhuunfaa",
        labelFullName:"Maqaa Seeraa Guutuu (akka paaspportii ykn eenyummeessaa irratti jiru)",
        labelGender:"Saala",
        genderMale:"Dhiira", genderFemale:"Dubartii",
        labelDOB:"Guyyaa Dhalootaa (GC)",
        labelBirthCity:"Magaalaa/Iddoo dhalootaa",
        labelBirthCountry:"Biyyaa dhalootaa",
        labelPhoto:"Suuraa paaspoortii galchaa",
        req1:"Bakka ifaa (adii ykn cream)",
        req2:"Ija, koofiyyaa ykn dukkana hin qabaatu",
        req3:"Fuulli gidduutti, ifaan mul'atu",
        req4:"Ji'oota 6 darban keessatti fudhatame",
        req5:"JPEG, max 240 KB, 600×600 px",
        contactSection:"B. Odeeffannoo qunnamtii",
        labelRegion:"Teessoo - Naannoo",
        labelCity:"Magaalaa",
        labelDistrict:"Kutaa/Sub-city",
        labelPhone:"Lakkoofsa bilbila hojii irra jiru",
        labelEmail:"Imeelii",
        educationSection:"C. Barnoota",
        labelEducation:"Sadarkaa barnoota ol'aanaa maal akka ta'e filadhu",
        maritalSection:"D. Haala fuudhaa heerumaa",
        labelMarital:"Haala fuudhaa heerumaa filadhu",
        spouseTitle:"E. Odeeffannoo fuudhaa heerumaa",
        labelSpouseName:"Maqaa guutuu fuudhaa heerumaa",
        labelSpouseDOB:"Guyyaa dhalootaa fuudhaa heerumaa",
        labelSpouseCity:"Magaalaa dhalootaa fuudhaa heerumaa",
        labelSpouseCountry:"Biyya dhalootaa fuudhaa heerumaa",
        labelSpousePhoto:"Suuraa fuudhaa heerumaa galchaa",
        childrenSection:"F. Ilmaan (21 gadi)",
        labelHasChildren:"Ilmaan 21 gadi qabduu?",
        labelChildrenCount:"Meeqa qaba?",
        paymentSection:"G. Ragaa Kaffaltii",
        paymentHint:"Suuraa ragaa kaffaltii galchaa, kunniin ifatti mul'achuu qabu:",
        pay1:"Maqaa guutuu ergaa ergamee",
        pay2:"Baajata kaffaltii",
        pay3:"Lakkoofsa ragaa",
        pay4:"Guyyaa fi sa'aatii",
        submitText:"Ergaa"
      }
    };

    // --- Element refs ---
    const lang = document.getElementById('lang');
    const formTitle = document.querySelector('[data-key="formTitle"]') || document.querySelector('.title');
    const subtitle = document.querySelector('[data-key="subtitle"]') || document.querySelector('.subtitle');

    function q(id){return document.getElementById(id)}

    const fields = {
      fullName:q('fullName'), gender:q('gender'),
      day:q('day'), month:q('month'), year:q('year'),
      birthCity:q('birthCity'), birthCountry:q('birthCountry'),
      photo:q('photo'), photoPreview:q('photoPreview'),
      region:q('region'), city:q('city'), district:q('district'),
      phone:q('phone'), email:q('email'),
      education:q('education'),
      marital:q('marital'),
      spouseBlock:q('spouseBlock'), spouseName:q('spouseName'), spouseDay:q('spouseDay'), spouseMonth:q('spouseMonth'), spouseYear:q('spouseYear'),
      spousePhoto:q('spousePhoto'), spousePreview:q('spousePreview'),
      hasChildren:q('hasChildren'), childrenCount:q('childrenCount'), childrenContainer:q('childrenContainer'),
      payment:q('payment'), paymentPreview:q('paymentPreview'),
      submitBtn:q('submitBtn')
    };

    // current language
    let cur = localStorage.getItem('dv_lang') || 'en';
    if(lang) lang.value = cur;

    // --- utility: set innerText for elements with data-key attr ---
    function applyTranslations(code){
      const dict = DICT[code] || DICT.en;
      // top texts
      if(formTitle) formTitle.textContent = dict.formTitle;
      if(subtitle) subtitle.textContent = dict.subtitle;

      // data-key elements labels
      document.querySelectorAll('[data-key]').forEach(el=>{
        const key = el.getAttribute('data-key');
        if(dict[key]) el.textContent = dict[key];
      });
      // options that were using data-key-option
      document.querySelectorAll('[data-key-option]').forEach(opt=>{
        const key = opt.getAttribute('data-key-option');
        if(key && dict[key]) opt.textContent = dict[key];
      });

      // update submit button
      if(fields.submitBtn) fields.submitBtn.textContent = dict.submitText || dict.submitText;
      
      // Update select options manually where needed
      document.querySelectorAll('#gender option').forEach(opt=>{
        if(opt.value==='male') opt.textContent = dict.genderMale;
        if(opt.value==='female') opt.textContent = dict.genderFemale;
      });
      document.querySelectorAll('#marital option').forEach(opt=>{
        if(opt.value==='unmarried') opt.textContent = (dict['maritalUnmarried']||'Unmarried');
        if(opt.value==='married') opt.textContent = (dict['maritalMarried']||'Married');
        if(opt.value==='divorced') opt.textContent = (dict['maritalDivorced']||'Divorced');
        if(opt.value==='widowed') opt.textContent = (dict['maritalWidowed']||'Widowed');
        if(opt.value==='legally_separated') opt.textContent = (dict['maritalLegallySeparated']||'Legally Separated');
      });
    }

    // --- populate day/month/year selects ---
    function fillDOBselects(context){
      let dayEl, monthEl, yearEl;
      if (typeof context === 'string') {
        const base = context;
        dayEl = base ? document.querySelector(`select[name="${base}Day"]`) : fields.day;
        monthEl = base ? document.querySelector(`select[name="${base}Month"]`) : fields.month;
        yearEl = base ? document.querySelector(`select[name="${base}Year"]`) : fields.year;
      } else if (context instanceof HTMLElement) {
        dayEl = context.querySelector('select[name*="day"]');
        monthEl = context.querySelector('select[name*="month"]');
        yearEl = context.querySelector('select[name*="year"]');
      }

      if(!dayEl || !monthEl || !yearEl) return;
      // Clear existing except first
      dayEl.innerHTML = '<option value="">Day</option>';
      monthEl.innerHTML = '<option value="">Month</option>';
      yearEl.innerHTML = '<option value="">Year</option>';
      
      for(let d=1; d<=31; d++){ const o=document.createElement('option'); o.value=d; o.text=d; dayEl.appendChild(o); }
      const months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
      for(let m=1; m<=12; m++){ const o=document.createElement('option'); o.value=m; o.text=months[m-1]; monthEl.appendChild(o); }
      const current = new Date().getFullYear();
      for(let y=current; y>=1900; y--){ const o=document.createElement('option'); o.value=y; o.text=y; yearEl.appendChild(o); }
    }

    // populate applicant and spouse DOB selects now
    fillDOBselects('');
    fillDOBselects('spouse');

    // --- language change handler ---
    function onLanguageChange(){
      cur = lang.value || 'en';
      localStorage.setItem('dv_lang', cur);
      applyTranslations(cur);
    }
    if(lang) lang.addEventListener('change', onLanguageChange);
    
    // --- show/hide spouse block when married ---
    if(fields.marital){
        fields.marital.addEventListener('change', () => {
          if(fields.marital.value === 'married'){
            fields.spouseBlock.classList.remove('hidden'); fields.spouseBlock.setAttribute('aria-hidden','false');
            fillDOBselects('spouse');
          } else {
            fields.spouseBlock.classList.add('hidden'); fields.spouseBlock.setAttribute('aria-hidden','true');
          }
        });
    }

    // --- children logic ---
    if(fields.hasChildren){
        fields.hasChildren.addEventListener('change', () => {
          const v = fields.hasChildren.value;
          if(v === 'yes'){
            document.getElementById('childrenCountWrapper').classList.remove('hidden');
          } else {
            document.getElementById('childrenCountWrapper').classList.add('hidden');
            fields.childrenContainer.innerHTML = '';
          }
        });
    }

    if(fields.childrenCount){
        fields.childrenCount.addEventListener('change', ()=> {
          const n = parseInt(fields.childrenCount.value) || 0;
          fields.childrenContainer.innerHTML = '';
          for(let i=0; i<n; i++){
            const block = document.createElement('div');
            block.className = 'block child-block';
            // Note: Naming convention 'children-{i}-field' matches Flask-WTF FieldList expectations
            block.innerHTML = `
              <div class="block" role="group" aria-label="Child ${i+1}">
                <h4>Child ${i+1}</h4>
                <label>Full name</label>
                <input type="text" name="children-${i}-name" />

                <label>Gender</label>
                <select name="children-${i}-gender"><option value="">--</option><option value="male">Male</option><option value="female">Female</option></select>

                <label>Date of Birth</label>
                <div class="dob-row">
                  <select name="children-${i}-day"></select>
                  <select name="children-${i}-month"></select>
                  <select name="children-${i}-year"></select>
                </div>

                <label>Birth city / town</label>
                <input type="text" name="children-${i}-city" />

                <label>Birth country</label>
                <input type="text" name="children-${i}-country" />

                <label>Upload passport photo</label>
                <input type="file" name="children-${i}-photo" accept="image/jpeg" />
                <div class="preview-row" id="childPreview${i+1}"></div>
              </div>
            `;
            fields.childrenContainer.appendChild(block);
            fillDOBselects(block); 
            
            // attach preview handler for child's photo
            const fileInput = block.querySelector(`input[name="children-${i}-photo"]`);
            const previewDiv = block.querySelector(`#childPreview${i+1}`);
            fileInput.addEventListener('change', (e)=> handleImagePreview(e.target.files[0], previewDiv));
          }
        });
    }

    // --- image preview ---
    function handleImagePreview(file, previewEl){
      previewEl.innerHTML = '';
      if(!file) return;
      const reader = new FileReader();
      reader.onload = (ev)=>{
        const img = document.createElement('img'); img.src = ev.target.result;
        previewEl.appendChild(img);
      };
      reader.readAsDataURL(file);
    }

    if(fields.photo) fields.photo.addEventListener('change', (e)=> handleImagePreview(e.target.files[0], fields.photoPreview));
    if(fields.spousePhoto) fields.spousePhoto.addEventListener('change', (e)=> handleImagePreview(e.target.files[0], fields.spousePreview));
    if(fields.payment) fields.payment.addEventListener('change', (e)=> handleImagePreview(e.target.files[0], fields.paymentPreview));

    // Initial apply
    applyTranslations(cur);

})();