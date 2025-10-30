# Proje Yönetimi ve Git Yönergesi

Öncelikle proje yönetimi için bir “Github Projects” oluşturduk. Süreç boyunca taskları herkese oradan atayacağız. MVP sürecinde çalışacak olan herkese bu projeye ve repoya erişim yetkisi verdim. Taskları yarın (pazartesi) atamaya başlayacağız ve bitirdikçe müsaitlik durumunuza ve isteğinize göre yeniden atayacağız.

Şimdi bir task size atandıktan sonra nasıl ilerleyeceğinize bakalım:

### 1- Projeyi Klonlama

`git clone <repo-url>`

kodu ile projeyi kendi bilgisayarınıza klonlayın. (Bunu sadece ilk sefer yapsanız yeterli).

### 2- Yeni Bir Branch Oluşturma ve İsimlendirme

`git checkout -b <branch-name>`

komutu yeni bir branch oluşturur ve o branch’e geçiş yapar. Eğer yenisini oluşturmadan var olan bir branch’e geçiş yapmak istiyorsanız “-b“ kullanmadan `git checkout <branch-name>` yazmanız yeterli. İlk kod da geçiş için kullanılabilir fakat eğer girilen isimde bir branch yoksa yenisini oluşturur. Branch isimlerinin açıklayıcı ve belirli bir standartta olması da önemlidir. Bu proje özelinde kullanacağımız isimlendirme standardı:

- **Küçük Harfler:** Tüm branch isimleri küçük harflerle yazılmalıdır.
- **Kelime Ayırıcı:** Kelimeler arasında ayırıcı olarak - (tire) kullanılmalıdır.
- **Kısa ve Anlamlı:** Branch isimleri mümkün olduğunca kısa, ama ne üzerinde çalışıldığını belirtecek kadar açıklayıcı olmalıdır.

**Component Geliştirme:**

Format: `feature/<component-name>`

Örnek: `feature/home-intro`, `feature/navbar`

**Yeni Özellik Eklenmesi:**

Format: `feature/<feature-name>`

Örnek: `feature/add-login`, `feature/language-selector`

**Hata Düzeltme:**

Format: `bugfix/<bug-description>`

Örnek: `bugfix/fix-navbar`, `bugfix/responsive-issue`

**Performans İyileştirmesi:**

Format: `enhancement/<area>`

Örnek: `enhancement/load-time`, `enhancement/api-optimization`

**Çakışma (Conflict) Çözümü:**

Format: `hotfix/<conflict-description>`

Örnek: `hotfix/resolve-merge-conflict`, `hotfix/style-conflict`

**Dokümantasyon Güncellemeleri:**

Format: `docs/<update-description>`

Örnek: `docs/update-readme`, `docs/api-documentation` 

### 3- Branch’te Değişiklik Yapma ve Commit Etme

Üzerinde çalıştığınız branch’e yaptığınız değişiklikleri kaydetmek için öncelikle `git add .` komutu ile değişikliklerinizi staging area’ya eklemelisiniz. Ardından `git commit -m "<commit-message>"` ile yaptığınız değişiklikleri commit etmelisiniz. Commit mesajı kısa, öz ve yaptığınız değişikliğin ne olduğunu net bir şekilde açıklayıcı olmalıdır. Bu kısma lütfen özen gösterelim.

### 4- Değişiklikleri Repoya Kaydetme

Yerel branch’inizde yaptığınız değişiklikleri repoya kaydetmek için `git push -u origin <branch-name>` komutunu kullanabilirsiniz. Bu komuttaki -u flag’i gelecekteki push komutlarının direkt belirttiğiniz repoya yapılmasını sağlar. Dolayısıyla aynı branch’e yapacağınız sonraki push’ları sadece `git push` komutuyla yapabilirsiniz. Burada asla main branch’e push yapmamanız önemli. Main branch’i sadece sürecin sonunda uygulamanın bitmiş halini içerecek.

### 5- Pull Request (PR) Oluşturma

Branch'inizdeki değişiklikler tamamlandığında, bu değişiklikleri develop branch'ine merge etmek için bir Pull Request (PR) oluşturun.

1. GitHub'da repository'ye gidin.
2. Yeni oluşturduğunuz branch'i seçin.
3. "Compare & pull request" düğmesine tıklayın.
4. PR başlığı ve açıklamasını yazın, değişiklikleri açıklayın.
5. PR'ı oluşturun.

### 6- Kod İncelemesi ve Merge

Oluşturduğunuz PR, diğer ekip üyeleri tarafından incelenecek. Onay aldıktan sonra, PR develop branch'ine merge edilecek.

### 7- Branch Silme (Opsiyonel)

PR merge edildikten sonra branch’inizi silebilirsiniz.

- Remote branch silme: `git push origin --delete <branch-name>`
- Lokal branch silme: `git branch -d <branch-name>`

### 8- Branch’i Develop ile Güncel Tutma

Öncelikle develop branch’indeki son değişiklikleri GitHub’dan lokale çekmek için `git checkout develop` ve `git pull origin develop` komutlarını kullanın. Sonra `git checkout <branch-name>` komutu ile güncel tutmak istediğiniz branch’e geçin. Sonra `git merge develop` komutu ile develop branch’indeki değişiklikleri üzerinde çalıştığınız branch’e uygulayın. Eğer bir conflict (çakışma) oluşursa, bu conflict'leri çözmeniz gerekecek. Merge’ler sırasında çıkabilecek conflict’leri önlemek adına bu işlemi develop branch’i her güncellendiğinde yapmanız önemli.

### 9- Başka Bir Branch’te Çalışmaya Geçme

GitHub’daki repoda var olan başka bir branch’te çalışmaya için öncelikle `git checkout -b <branch-name>` ile üzerinde çalışılacak branch’e geçiş yapılır. Son olarak `git pull <branch-name>` ile üzerinde çalışılacak olan branch’in güncel hali çekilir ve üzerinde çalışmaya hazır hale getirilir.

### Diğer Genel Kurallar ve İpuçları

- **Her Görev İçin Yeni Branch:** Her yeni görev veya özellik için yeni bir branch oluşturun.
- **Güncel Tutun:** Branch'inizi düzenli olarak develop branch'i ile güncelleyin.
- **Düzenli Commit:** Küçük ve sık commit’ler yaparak ilerlemenizi takip edin.
- **Branch İsimlendirmeleri:** Yukarıda belirtilen branch isimlendirme kurallarına uyun.
- **Merge Çatışmaları:** Merge çatışmaları durumunda, çözümden önce takım liderine haber verin.

`git branch -r` ile GitHub reposunda bulunan bütün branch’leri görebilirsiniz. Sadece `git branch` yazarsanız da lokal branch’ler listelenir

