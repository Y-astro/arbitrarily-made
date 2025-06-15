import re

def split_into_paragraphs(text):
    paragraphs = re.split(r'\n\s*\n', text.strip())
    return paragraphs

def highlight_and_find(paragraphs, search_word):
    found_paragraphs = []
    word_pattern = re.compile(rf'\b({re.escape(search_word)})\b', re.IGNORECASE)

    for para in paragraphs:
        if re.search(word_pattern, para):
            highlighted_para = re.sub(word_pattern, r'\033[1;31m\1\033[0m', para)
            found_paragraphs.append(highlighted_para)

    return found_paragraphs

if __name__ == "__main__":
    
    input_text = """
## 9-30


```shloka-sa

अपि चेत् सुदुराचारो भजते माम् अनन्यभाक् ।
साधुरेव स मन्तव्यः सम्यक् व्यवसितो हि सः ॥ ३० ॥

```
```shloka-sa-hk

api cet sudurAcAro bhajate mAm ananyabhAk |
sAdhureva sa mantavyaH samyak vyavasito hi saH || 30 ||

```
`अपि चेत्` `[api cet]` Even when `सुदुराचारः` `[sudurAcAraH]` a very offensive person `भजते माम्` `[bhajate mAm]` worships Me `अनन्यभाक्` `[ananyabhAk]` with unwavering devotion, `मन्तव्यः` `[mantavyaH]` he needs to be considered as `साधुः एव` `[sAdhuH eva]` virtuous indeed. `सः हि` `[saH hi]` He definitely `सम्यक् व्यवसितः` `[samyak vyavasitaH]` has the appropriate determination.

Having been born as a certain type of being, there are certain ways to behave and certain misbehaviors to avoid. A person who doesn’t comply and crosses the line is considered very offensive. 

When such a person worships the Lord with unwavering devotion, with the worship alone being the goal, he needs to be considered virtuous. He is a topper among the followers of the Lord, equal to the kind of people described in the previous Shloka.

How come? 

In this Shloka, the statement 'he has made the appropriate resolution' says that his determination is true and proper. This person has firmly resolved- 'The Lord is the one and only origin of the entire universe. He is the ultimate creator. He is the goal of all humans. He is the master of all things moving and stationary. He is our controller, my guide, my friend and He gives ultimate joy'. Such a resolution is difficult and rare. 

With this kind of resolution, a person is in constant worship of the Lord - with worship itself being the goal of his worship. Hence, this person must be considered virtuous indeed and be respected. Considering his resolve and consequent worship, the malicious deeds he commits are to be considered as minor imperfections. This person is not to be disrespected for those deeds. Instead, this person must be praised - this is the summary here.

Now, a question arises - Will the misconduct of this person not restrict the flow of devotion in future? As said in 
`कठोपनिषत्, १-२-२४` `[kaThopaniSat, 1-2-24]` :
 'Those who cannot keep off misconduct, those in whom desire and anger do not subside, even those whose mind does not have peace - such people cannot achieve Him through knowledge'. Will he still be capable of devotion?

This question is answered next -

    """

    search = "friend"
    paragraphs = split_into_paragraphs(input_text)
    result = highlight_and_find(paragraphs, search)

    if result:
        print("\nParagraphs containing the word:\n")
        for para in result:
            print(para + "\n")
    else:
        print("No paragraph contains the word.")
