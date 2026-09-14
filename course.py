class Course:
    # Class variable to count how many courses have been created
    course_count = 0

    def __init__(self, name, instructor, duration, price):
        self.name = name
        self.instructor = instructor
        self.duration = duration
        self.price = price
        Course.course_count += 1

    @classmethod
    def get_course_count(cls):
        """Class method to return the total number of courses created."""
        return cls.course_count

    def show_course_details(self):
        """Displays the details of the course."""
        print(f"Course Name: {self.name}")
        print(f"Instructor: {self.instructor}")
        print(f"Duration: {self.duration} weeks")
        print(f"Price: ${self.price:.2f}")

    def calculate_discount(self, discount_percentage):
        """Calculates and returns the discounted price."""
        discount_amount = self.price * (discount_percentage / 100)
        return self.price - discount_amount


class PremiumCourse(Course):
    def __init__(self, name, instructor, duration, price, mentor_support, live_sessions):
        # Call the __init__ of the parent class (Course)
        super().__init__(name, instructor, duration, price)
        # Add new attributes specific to PremiumCourse
        self.mentor_support = mentor_support
        self.live_sessions = live_sessions

    def show_course_details(self):
        """Overridden method to display premium course details including new attributes."""
        # Optionally, you could call super().show_course_details() here instead of re-writing
        super().show_course_details()
        print(f"Mentor Support: {'Yes' if self.mentor_support else 'No'}")
        print(f"Live Sessions: {self.live_sessions}")


# --- Demonstration of the OOP model ---
if __name__ == "__main__":
    print(f"Initial Course Count: {Course.get_course_count()}\n")

    # Creating a standard course
    course1 = Course("Introduction to Python", "Alice Smith", 4, 49.99)
    print("--- Standard Course Details ---")
    course1.show_course_details()
    print(f"Discounted Price (10% off): ${course1.calculate_discount(10):.2f}\n")

    # Creating a premium course
    premium_course1 = PremiumCourse(
        name="Advanced Machine Learning",
        instructor="Dr. Bob Jones",
        duration=12,
        price=199.99,
        mentor_support=True,
        live_sessions=5
    )
    print("--- Premium Course Details ---")
    premium_course1.show_course_details()
    print(f"Discounted Price (20% off): ${premium_course1.calculate_discount(20):.2f}\n")

    # Check total courses created
    print(f"Total Courses Created: {Course.get_course_count()}")
