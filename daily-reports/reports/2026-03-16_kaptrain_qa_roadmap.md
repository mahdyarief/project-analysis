# Kaptrain QA & Pending Tasks Roadmap - 2026-03-16

Laporan ini merangkum status fitur **Kaptrain** yang saat ini berada dalam tahap **Testing (Staging)** dan **Pending**, diekstraksi dari sinkronisasi database Notion terbaru.

---

## 🚧 Status Overview: Testing & Pending

| Kategori Prioritas | Testing (Staging) | Pending / In Progress |
| :--- | :---: | :---: |
| **Total Tasks** | **66** | **14+** |

---

## 🔍 Detail breakdown per Module

### 1. **Core System & UI Excellence**
*   **Status**: 🧪 **31 Tasks (Testing)** | 🚧 **6 Tasks (Pending)**
*   **Konteks Tugas**: 
    - Penyesuaian UI agar presisi sesuai desain Figma (ikon, sudut kotak, dll).
    - Perbaikan bug kritikal: Pengguna ter-logout otomatis setelah verifikasi email.
    - Review dan update aset SVG terbaru untuk seluruh aplikasi.

### 2. **Training Programs & Agenda**
*   **Status**: 🧪 **8 Tasks (Testing)** | 🚧 **1 Task (Pending)**
*   **Konteks Tugas**: 
    - Modifikasi sesi pada fitur Agenda (FR: *Modification de séance*).
    - Implementasi slicing UI untuk alur pemrograman latihan.
    - Investigasi error "Cannot create session" yang menghambat fungsionalitas utama.

### 3. **Messenger & Notifications**
*   **Status**: 🧪 **6 Tasks (Testing)** | 🚧 **2 Tasks (Pending)**
*   **Konteks Tugas**: 
    - Validasi alur pengiriman pesan (Chat) antar pengguna.
    - Koreksi pesan error pada form mandatori agar lebih informatif bagi user.

### 4. **Mobile Widgets (Home Screen)**
*   **Status**: 🧪 **7 Tasks (Testing)** | 🚧 **2 Tasks (Pending)**
*   **Konteks Tugas**: 
    - Verifikasi *Widget Detail Screen* untuk visualisasi data atlet.
    - Testing performa widget *Daily Steps* dan *Volume Latihan*.
    - Penanganan *error states* dan tampilan saat data kosong (empty state).

### 5. **Sign In, Profile & Auth**
*   **Status**: 🧪 **4 Tasks (Testing)** | 🚧 **1 Task (Pending)**
*   **Konteks Tugas**: 
    - Perbaikan navigasi tombol *back* pada perangkat agar tidak kembali ke layar OTP setelah login berhasil.
    - Validasi checklist pada input email di form registrasi.

### 6. **Sports & Wellness Tracking**
*   **Status**: 🧪 **7 Tasks (Testing)** | 🚧 **0 Tasks (Pending)**
*   **Konteks Tugas**: 
    - **Sports**: Perbaikan fungsi pembuatan olahraga baru (Master data).
    - **Wellness**: Memastikan prompt harian muncul tepat satu kali dan menangani logika "dismiss" secara benar.

### 7. **Coach/Athlete Invitation**
*   **Status**: 🧪 **1 Task (Testing)** | 🚧 **1 Task (Pending)**
*   **Konteks Tugas**: 
    - Perbaikan alur kounter undangan (Invitation Code) yang gagal saat mengundang user tertentu.

---

## 📊 Summary Insight
> [!IMPORTANT]
> Konsentrasi tugas terbesar berada pada **Core System (31 tasks)**, yang menandakan aplikasi sedang dalam fase pembersihan (UX Polish) sebelum rilis stabil. Isu navigasi dan autenitkasi menjadi fokus utama untuk diperbaiki minggu ini.

---
**Lampiran Data**: 
- [Laporan Lengkap (CSV)](file:///d:/Github/Gemini%20Gems/project-manager/daily-reports/reports/2026-03-16_multi_project_feature_report.csv)
