from django.db import models

# Create your models here.

class Question(models.Model):
    name = models.CharField(max_length=10)
    statement = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.id} {self.name}"


class Testcase(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name="testcases")
    testcase = models.CharField(max_length=5242880)
    Hardanswer = models.BooleanField()
    answer = models.CharField(max_length=5242880)



class Submission(models.Model):
    ques = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="submissions")
    code = models.CharField(max_length=5242880)
    lang = models.CharField(max_length=10)


class Output(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name="outputs")
    output = models.CharField(max_length=5242880)

