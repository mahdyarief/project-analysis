
1. Regarding the CMS role hierarchy: when logged in as an **Admin**, the user interface remains identical to the **Coach** role, with the sole exception of the 'Administrator' menu. Could you clarify if the Admin role inherits all Coach permissions? I'd like to confirm if the 'Administrator' menu is indeed the only distinguishing feature between these roles.

✅ **→ Answer: Yes, and also Admin can Coach some athletes as well, permission is the same like a normal Coach, unlimited athletes,** there are two types of Super Admin (predefined)

---

1. Entry points this page:

![image.png](attachment:a2810118-327f-4cbc-9904-a6a64b858e93:image.png)

**→ Answer: this button “Edit”**

![image.png](attachment:c447123a-58fb-4089-a01a-c60f080dff90:image.png)

---

1. Differences between “Training block model” and “Training cycle model”
    
    ✅ **→ Answer:**
    
    A **Training Block** is the *smallest unit* of a training session.
    
    It describes **a component inside a single session**, usually representing:
    
    - a warm-up section
    - a main workout block
    - a circuit
    - a specific exercise block
    - a cooldown
    - an interval sequence (e.g., 20s effort / 10s rest × 8 rounds)
    
    A training session is composed of **one or multiple blocks**.
    
    A **Training Cycle** is a *macro-structure* that organizes **multiple weeks of training sessions** around a progression plan. A cycle represents a **program phase**, usually lasting 2–6 weeks, where intensity and volume evolve gradually.
    
    **Kaptrain Programs** use cycles heavily because:
    
    - Week 1 → Base
    - Week 2 → Increase intensity
    - Week 3 → Peak
    - etc.

---

1. There is no sub-section for “Performance”

![image.png](attachment:6b204282-1c98-47b0-b3f3-500fcc9d194b:image.png)

**→ Answer: the client will add the “Performance” tab**

---

1. The confirmation of ranges inside profiles

| Metric | Unit | Min | Max | Notes |
| --- | --- | --- | --- | --- |
| FC Max | bpm |  |  |  |
| VMA | km/h |  |  |  |
| FTP | watts |  |  |  |
| PMA | watts |  |  |  |

![image.png](attachment:3e76ea77-822b-4dae-8ef3-cc6903ccf41f:image.png)

✅ → Answer: [https://www.notion.so/Markdown-Format-of-Application-2d419303246980859757c203897bad06?source=copy_link#2f4193032469805ea06fcae0c55889a5](https://www.notion.so/Specifications-and-Documentations-2d419303246980859757c203897bad06?pvs=21)

---

1. Entry point this screen:

![image.png](attachment:8be90a8d-2ebf-48aa-b418-269298540127:image.png)

→ Answer: 

![image.png](attachment:303cda32-0673-4310-a2fb-5450d59af1b7:image.png)

Notes(28/01): there would be a new Feature to add a session for all Athletes inside CMS (Super Admin account)

---

1. The CMS forgot password page is not yet available

![image.png](attachment:51973569-8f9c-42ab-af81-412f07694204:image.png)

Answer: we can use the same auth layout like sign in and register with different field for forgot password

---

1. What does the toggle below do? (Mobile Apps) 
✅ **→ Answer :** An accessibility toggle for changing the tutorial video to a disability-friendly version (22/01)

![image.png](attachment:52f6d278-e20f-4316-a333-0dfe6238e0d2:image.png)

1. When a user clicks the Pause button, does the background color change or remain the same? (Mobile Apps)
✅ **→ Answer :** The background doesn’t change, only the pause icon switches to a play icon (22/01)

![image.png](attachment:bcb76868-acdb-4d18-8a7b-9018cbda6730:image.png)

---

1. Where is the entry point or form for choosing the type? (Mobile Apps)

![image.png](attachment:eaebba75-0793-478a-8549-cc9dca67f23e:image.png)

![image.png](attachment:844ad115-9d95-4f34-8380-38cbedb1d754:image.png)

→ Answer: the first screen is when an Athelete do exercise based on Couch, the second screen is when Athlete create his own exercise.

---

1. Please confirm the mandatory fields for athlete data. The current fields include:
Prénom, Nom, Date de naissance, Numéro de téléphone, Genre, Votre poids actuel (Taille), Votre poids actuel (Poids), and Niveau de pratique.
    
    ✅ **→ Answer :** All fields are mandatory (22/01)
    

![image.png](attachment:92e13f40-27b6-4029-9e79-6f56f5d3446d:image.png)

---

1. How to define athlete’s form condition? There’s a table named `wellness_tracking` and has some variables (`energy_level` integer, `mood_level` integer, `sleep_quality` integer, `stress_level` integer, `muscle_soreness` integer)
    
    ✅ → Answer (26/1): https://www.figma.com/design/IHebumUD4vxDCjlyF0uEKd/Figma-Kaptrain?node-id=5407-195006&t=xW8XWUvN3LT9NbFy-4 and also this one for the documentation and define the score: [https://www.notion.so/Markdown-Format-of-Application-2d419303246980859757c203897bad06?source=copy_link#2f4193032469805ea06fcae0c55889a5](https://www.notion.so/Specifications-and-Documentations-2d419303246980859757c203897bad06?pvs=21)
    and also there would be a new icon if Athlete is not answered the Wellness question
    
    ![image.png](attachment:a9748be0-5c40-4a35-bb10-7788af807569:image.png)
    

![image.png](attachment:a401baf9-e270-4499-b2e1-9554410bb271:image.png)

---

1. Which column in database that I need to store `Workouts per Day` value?
    
    ✅ → Answer (26/11): If there is no column in database, you can add new one, its the average number of training sessions the athlete is expected to perform each day when following this program.
    
    for example:
    
    - **“2 workouts per day”** means the program is designed with **two distinct training sessions** on training days
        
        (e.g., a morning session + an evening session, or strength + conditioning, etc.).
        

---

1. Why can sessions be created on the mobile app? Can coaches log in on the mobile app?
(https://www.figma.com/design/IHebumUD4vxDCjlyF0uEKd/Figma-Kaptrain?node-id=5691-137859&t=xhHPkuL1ghyG5R9G-4)

![image.png](attachment:5dc5c6dd-f0c0-462a-961c-0e99b96fed1f:image.png)

✅ → Answer: the Athletes can create the training session by themself

---

1. Intensity Reference Confirmation and Explanation

[https://www.notion.so/Markdown-Format-of-Application-2d419303246980859757c203897bad06?source=copy_link#2f5193032469806891efc0dd32b9fedd](https://www.notion.so/Specifications-and-Documentations-2d419303246980859757c203897bad06?pvs=21)

![image.png](attachment:b590ea1d-67fe-4b7b-bbe2-0f242d81512b:image.png)

→ Answer: [https://www.notion.so/Markdown-Format-of-Application-2d419303246980859757c203897bad06?source=copy_link#2f4193032469805ea06fcae0c55889a5](https://www.notion.so/Specifications-and-Documentations-2d419303246980859757c203897bad06?pvs=21)

1. Latest discussion with the client on the Whatsapp group, after Coach or Athelete register, the user must to fill their banking data, but on the Figma there is no popup, or the user is redirected to “subscription plan page” with billing shows up? what happen if user doesn’t fulfill their bank details? can they navigate to the other pages? after fulfill their bank account, I can see that inside Figma its defined 14 days, but on the last chat on Whatsapp group it was 30 days, which one is the correct one?

✅  → Answer(9/2): [https://www.notion.so/CMS-Trial-Monetization-System-Proposal-v1-2fd19303246980eea5efcf5237047cec?source=copy_link](https://www.notion.so/CMS-Trial-Monetization-System-Proposal-v1-2fd19303246980eea5efcf5237047cec?pvs=21)

---

1. As we know that Administrator can change the current plan, with monthly and yearly, and also the number of Athelete, letsay I already add new Plan called “Basic” with max 5 Athlete, what happen if some Coach have 5 Athlete (maximum number) and then I as an admin change the maximum Athelete to 3? are those Coach with 5 Athelete will stay on 5 or should decreases to 3?

![image.png](attachment:e8475465-6a67-4803-872d-75c958c127d2:image.png)

![image.png](attachment:736da0d6-7271-4659-8b4b-dab9a6d91243:image.png)

✅ **→ Answer: we will discuss again later**

---

1. In the Athlete app’s Mon Coach menu, can users enter more than one coach referral code? (https://www.figma.com/design/IHebumUD4vxDCjlyF0uEKd/Figma-Kaptrain?node-id=3034-34784&t=xhHPkuL1ghyG5R9G-4)

![image.png](attachment:fbc117ce-ae1c-4bed-8a10-037e9b4334ff:image.png)

1. Will users be able to cancel their subscriptions? If yes, what should the feature do? (for CMS & Apps)

---

1. From the screens, Apnée has two categories (Mer & Piscine), and each category contains several record types such as “Jump Blue”, “CWT”, “CNF”, etc.
When adding or editing a record, we’ve seen the “Jump Blue” as the record name.

could you please answer and confirm these points:
- **Is the expected hierarchy:
Sport(**Apnée) **→ Category (Mer/Piscine) → Record Type (Jump Blue, CWT, CNF) → Unit**?
(Meaning “Jump Blue” is a record type inside Apnée, not a top-level record.)

- On the detail Records of Apnée, “Jump blue” appears as an item inside the categories Mer and Piscine. But on the “Add / Edit Record” screen, it also has “Jump blue” as the **record name** itself. Could you please explain more about this with case example? thanks

![image.png](attachment:56b2eed6-66a9-46a0-bdd7-e2e7a7282c60:image.png)

![image.png](attachment:97ed2904-d3a2-4f3d-b079-83f1b037b3d0:image.png)

✅ **Answer @Irfan from Weaver  :** 

Actually, **“Sea” (Mer in french)** and **“Pool” (Piscine in french)** are both **category** fields - same idea as having “Road” or “Track” as categories for running.

What you see listed as **“Jump Blue”**, **“CWT (Constant Weight with Fins)”**, etc. are **record titles only**—there should be **no categorization or prefill** for those.

So the expected hierarchy is:

**Sport selection (Freediving) → Category selection (Sea / Pool / etc ) → Record title (Jump Blue, CWT, etc.)**

And for every record, the user must also **select a specific unit**.

![records details.png](attachment:50c4a590-3220-474b-8d20-b3fe8978c64e:records_details.png)

---

1. There is an option to delete user’s account on profile menu. Is it hard-delete or soft-delete?

![image.png](attachment:5adcb584-c7d4-4880-85ca-3526aba6beac:image.png)

      ✅ **Answer: Soft delete**

1. **Subscription Questions**
    1. **After cancelling a subscription, what should the status be in Stripe, and how should it be displayed on the web UI (Subscriptions)?
    → Answer:** 
    2. **For upgrading subscriptions: if the user already has a 1-year subscription on a lower tier and wants to upgrade to a monthly plan on a higher tier, how should the flow be handled (Subscriptions)?
    ✅ Answer:** He can make the request, but the change will only take effect at the end of his annual commitment period.
    3. **For upgrading mid-cycle:** if the user is on a monthly subscription (e.g., Standard monthly) and wants to upgrade to a higher tier (e.g., Premium or Pro) while still in the middle of the current billing cycle, how should the upgrade be applied (prorated, immediate restart, or applied next cycle)?
     ✅ Answer: The price update will take effect the following month, thus postponing the commitment until the end of the following month; however, the customer will have the option to access their additional licenses immediately.
    4. **For downgrading plans:** if the user wants to downgrade from a higher tier (e.g., Pro → Premium or Premium → Standard), should the downgrade take effect immediately or only at the next billing cycle?
     ✅ Answer: only at the next billing cycle
    5. **For license limits when downgrading:** if licenses represent the number of athletes a coach can manage and the user currently exceeds the destination plan’s limit (e.g., 40 athletes but downgrading to Premium’s 25), what should happen in this situation?
    → Answer: —
    6. **For license expansions when upgrading:** when upgrading to a higher tier with more athlete slots, should the increased license limit apply immediately or at the next billing cycle?
    ✅Answer: The price update will take effect the following month; however, he will have the option to access his additional licenses immediately.
    7. **For proration rules:** when changing plans (upgrade or downgrade), should the system apply prorated credits/charges or always start a new billing cycle without proration?
    ✅ Answer: The system applies the new billing the following month.
    8. **For switching between monthly and yearly:** when a user switches between monthly and yearly billing, should the system preserve the 20% yearly discount or recalculate pricing based on the new billing cycle?
    ✅ Answer: If the user switches from monthly to annual, their new billing will take place the following month and will commit them to the annual rate for the next 12 months. If the user wants to switch from the annual to the monthly plan, they can, but this will take effect at the end of their annual commitment period.
    9. **For cancellation behavior:** when a user cancels a subscription, should the cancellation take effect immediately or continue until the current billing cycle ends?
    ✅ Answer: continue until the current billing cycle ends
    10. **For confirmation dialogs:** before applying an upgrade, downgrade, or billing-cycle change, do you want the system to show a confirmation modal explaining pricing changes, license limits, and when the new plan will take effect?
    ✅ Answer: Yes ! 
2. What is the mapping for the Grade View Exercise icons (Admin/Coach)

![image.png](attachment:6d6af47e-ac89-4686-a7bc-66b08b95aa10:image.png)

✅ **Answer: → No icone for this vision grid (just favorite + name + option : disability icon**

1. What is the mapping for the Theme icons in Detail Exercise 

![image.png](attachment:14ae5f50-bace-40b6-b2e5-fddcbd605fce:image.png)

✅ **Answer: →** Cf sigma design system “Theme icons”

1. Where do "My information" and "my calendar" in the coach dropdown sidebar lead to

![image.png](attachment:108f8b73-dd25-44b4-812b-a261eabce154:image.png)

✅**Answer →** For the time being, we have removed this option; if the coach clicks on their name, they are redirected directly to "My Information".

1. What page should redirect if an admin role click “My Dashboard” when click the profile?
✅**Answer →** Admin is a coach. It just has the administration tab in addition

1. https://www.figma.com/design/IHebumUD4vxDCjlyF0uEKd/Figma-Kaptrain?node-id=7694-190718&t=TYvCYqfAvkHRWYRi-4

I want to ask a few questions about the design flow.
Will this be appended to the training block, or is it handled differently?

and I also want to ask, is it added as a training block related to the session or is it just a training block?
Because if you look at it, there is an example of a training block that has been added as a training block related to the session, marked in blue.

✅ **Answer: →** Tristan is updating the screens to create prototypes for you, but indeed, when you create a session for an athlete, you can click on the "add a block" button. This takes you to the screen linked to your personal block library, and if you click on "insert the block," it is added to the session being created.

1. https://www.figma.com/design/IHebumUD4vxDCjlyF0uEKd/Figma-Kaptrain?node-id=7694-231705&t=TYvCYqfAvkHRWYRi-4

There are no fields to insert the session type and status. We need both fields in the database.
❌**Answer →** I didn't understand what you meant by session type and status? 
2. Regarding to this page https://www.figma.com/design/IHebumUD4vxDCjlyF0uEKd/Figma-Kaptrain?node-id=7979-88149&t=KvoiS8J8rZizokzm-4, how to calculate performance either of coaches or athletes? And then what’s the formula to calculate any cards that related to revenue (MRR/NRR)?

✅ **Answer:**

**1. Total MRR – €32 732 (+2.8%)**

Your **total active subscription revenue per month**. The green +2.8% indicates growth compared to the previous month.

**2. New MRR – €5 687 (+4.9%)**

Revenue gained from **new customers or plan upgrades** during the last month.

**3. Churn MRR – €1 457 (–1.1%)**

Revenue lost from **cancellations or downgrades** during the last month.

1. UI state for athlete pending coach approval? (https://www.figma.com/design/IHebumUD4vxDCjlyF0uEKd/Figma-Kaptrain?node-id=3034-35244&t=OMosvUZQcqXBaoMR-4)

![image.png](attachment:a5bb3f57-8d12-4860-afe3-244cc8a8db36:image.png)

1. Regarding to this page https://www.figma.com/design/IHebumUD4vxDCjlyF0uEKd/Figma-Kaptrain?node-id=3285-70963&t=XTp6ljPn8J8kUs4y-4, what is the formula to calculate `Niveau actuelle` value?
2. Regarding to this page https://www.figma.com/design/IHebumUD4vxDCjlyF0uEKd/Figma-Kaptrain?node-id=3034-33309&t=QkxMXSfN7U7IGmyY-1, there are two types of training programs for athlete in mobile app:
  - fixed term (one time purchase, having end date)  
  - ongoing (subscription purchase, no end date)

However, in CMS app regarding to this page https://www.figma.com/design/IHebumUD4vxDCjlyF0uEKd/Figma-Kaptrain?node-id=5045-101499&t=QkxMXSfN7U7IGmyY-1, when admin/coach creating a training program item, there’s no indication that the training program can be a one time purchase or subscription purchase.

What is the next step to continue this process?
3. If the daily wellness reminder is disabled, can it be enabled again? If yes, where can we enable it in the menu? https://www.figma.com/design/IHebumUD4vxDCjlyF0uEKd/Figma-Kaptrain?node-id=3034-31191&t=5jZpCWZ0GjbMshzF-4 
4.