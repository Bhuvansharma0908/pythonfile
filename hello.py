class Resume:
    def __init__(self, name, email, phone, summary, education, experience):
        self.name = name
        self.email = email
        self.phone = phone
        self.summary = summary
        self.education = education
        self.experience = experience

    def generate_resume(self):
        resume = f"""
        Name: {self.name}
        Email: {self.email}
        Phone: {self.phone}
        
        Summary:
        {self.summary}
        
        Education:
        {self.education}
        
        Experience:
        {self.experience}
        """
        return resume


def main():
    name = "Raj Kumar"
    email = "rajkumar@gmail.com"
    phone = "740963962"
    summary = "Experienced professional with expertise in Python programming."
    education = "Bachelor of Science in Computer Science, University of Chandigarh University"
    experience = "Software Engineer, ABC Company, 2015-present\n- Developed Python applications\n- Collaborated with cross-functional teams"

    resume = Resume(name, email, phone, summary, education, experience)
    generated_resume = resume.generate_resume()
    print(generated_resume)


if __name__ == "__main__":
    main()
