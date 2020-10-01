# Hands-on #3: AWSで自動質問回答ボットを走らせる
https://tomomano.gitlab.io/intro-aws/#sec_handson_03

```
docker pull registry.gitlab.com/tomomano/intro-aws/handson03:latest

context="Albert Einstein (14 March 1879 – 18 April 1955) was a German-born theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics (alongside quantum mechanics). His work is also known for its influence on the philosophy of science. He is best known to the general public for his mass–energy equivalence formula E = mc2, which has been dubbed \"the world's most famous equation\". He received the 1921 Nobel Prize in Physics \"for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect\", a pivotal step in the development of quantum theory."

question="In what year did Einstein win the Nobel prize ?"

docker run registry.gitlab.com/tomomano/intro-aws/handson03:latest "${context}" "${question}" foo --no_save
```
