doc_text_raw = """
Patient Information System - MentCare

A patient information system to support mental health care is a medical information system that maintains information about patients suffering from mental health problems and the treatments that they have received. Most mental health patients do not require dedicated hospital treatment but need to attend specialist clinics regularly where they can meet a doctor who has detailed knowledge of their problems. To make it easier for patients to attend, these clinics are not just run in hospitals. They may also be held in local medical practices or community centers.

The MHC-PMS (Mental Health Care-Patient Management System) is an information system that is intended for use in clinics. It makes use of a centralized database of patient information but has also been designed to run on a PC, so that it may be accessed and used from sites that do not have secure network connectivity. When the local systems have secure network access, they use patient information in the database but they can download and use local copies of patient records when they are disconnected. The system is not a complete medical records system so does not maintain information about other medical conditions. However, it may interact and exchange data with other clinical information systems. Figure 1.6 illustrates the organization of the MHC-PMS.

The MHC-PMS has two overall goals:
1. To generate management information that allows health service managers to assess performance against local and government targets.
2. To provide medical staff with timely information to support the treatment of patients.

The nature of mental health problems is such that patients are often disorganized so may miss appointments, deliberately or accidentally lose prescriptions and medication, forget instructions, and make unreasonable demands on medical staff. They may drop in on clinics unexpectedly. In a minority of cases, they may be a danger to themselves or to other people. They may regularly change address or may be homeless on a long-term or short-term basis. Where patients are dangerous, they may need to be ‘sectioned’—confined to a secure hospital for treatment and observation.

Users of the system include clinical staff such as doctors, nurses, and health visitors (nurses who visit people at home to check on their treatment). Nonmedical users include receptionists who make appointments, medical records staff who maintain the records system, and administrative staff who generate reports.

The system is used to record information about patients (name, address, age, next of kin, etc.), consultations (date, doctor seen, subjective impressions of the patient, etc.), conditions, and treatments. Reports are generated at regular intervals for medical staff and health authority managers. Typically, reports for medical staff focus on information about individual patients whereas management reports are anonymized and are concerned with conditions, costs of treatment, etc.

The key features of the system are:

1. Individual care management Clinicians can create records for patients, edit the information in the system, view patient history, etc. The system supports data summaries so that doctors who have not previously met a patient can quickly learn about the key problems and treatments that have been prescribed.
2. Patient monitoring The system regularly monitors the records of patients that are involved in treatment and issues warnings if possible problems are detected. Therefore, if a patient has not seen a doctor for some time, a warning may be issued. One of the most important elements of the monitoring system is to keep track of patients who have been sectioned and to ensure that the legally required checks are carried out at the right time.
3. Administrative reporting The system generates monthly management reports showing the number of patients treated at each clinic, the number of patients who have entered and left the care system, number of patients sectioned, the drugs prescribed and their costs, etc.

Two different laws affect the system. These are laws on data protection that govern the confidentiality of personal information and mental health laws that govern the compulsory detention of patients deemed to be a danger to themselves or others. Mental health is unique in this respect as it is the only medical speciality that can recommend the detention of patients against their will. This is subject to very strict legislative safeguards.

One of the aims of the MHC-PMS is to ensure that staff always act in accordance with the law and that their decisions are recorded for judicial review if necessary. As in all medical systems, privacy is a critical system requirement. It is essential that patient information is confidential and is never disclosed to anyone apart from authorized medical staff and the patient themselves. The MHC-PMS is also a safety-critical system. Some mental illnesses cause patients to become suicidal or a danger to other people. Wherever possible, the system should warn medical staff about potentially suicidal or dangerous patients.

The overall design of the system has to take into account privacy and safety requirements. The system must be available when needed otherwise safety may be compromised and it may be impossible to prescribe the correct medication to patients. There is a potential conflict here—privacy is easiest to maintain when there is only a single copy of the system data. However, to ensure availability in the event of server failure or when disconnected from a network, multiple copies of the data should be maintained. I discuss the trade-offs between these requirements in later chapters.

"""


expected_requirements = """
1. login system to make sure only authorized medical staffs and the patient himself can access the data.
2. Record and maintain detailed patient information including consultations, conditions, and treatments.
3. Regularly monitor patient records and generate alerts for potential issues such as missed appointments or prescription losses.
4. Provide administrative reporting capabilities to generate monthly reports on patient statistics, treatments, and costs.
5. Manage individual patient records, allowing clinicians to view patient histories and access data summaries.
6. Monitor treatment involvement and track sectioned patients to ensure timely legal checks and compliance.
7. Generate reports on clinic activity, patient flow, sectioning, prescriptions, and associated costs.
8. Ensure system compliance with data protection laws to maintain confidentiality of patient information.
9. Identify and alert medical staff about potentially dangerous patients to prevent harm.
10. Maintain system availability and manage data replication to balance privacy and accessibility during network outages or server failures.
11. data access logging system to track access to patient records for privacy laws compliance auditing.
    """

expected_epics = """"{
    "Epics": [
        {
            "User Story": "Implement a login system to ensure that only authorized medical staff and the patient can access patient data, maintaining compliance with data protection laws.",
            "Deliverables": {
                "architecture_design": "Design of secure authentication and authorization mechanisms.",
                "database_schema_design": "Schema for storing user credentials and roles.",
                "unit_tests": "Tests to verify authentication logic and access controls.",
                "user_training_documentation": "Documentation on how to securely log in and manage access.",
                "production_support_plan": "Plan for monitoring and maintaining the login system's performance and security."
            }
        },
        {
            "User Story": "Record, maintain, and manage detailed patient information including consultations, conditions, treatments, and history, with capabilities for clinicians to view comprehensive data summaries.",
            "Deliverables": {
                "architecture_design": "Design of the patient information management system.",
                "database_schema_design": "Schema for patient records, consultations, treatments, and medical history.",
                "unit_tests": "Tests to ensure data integrity and correct data retrieval.",
                "user_training_documentation": "Documentation on how to enter and retrieve patient information."
            }
        },
        {
            "User Story": "Regularly monitor patient records to generate alerts for missed appointments, prescription losses, and identification of potentially dangerous patients to ensure safety and compliance.",
            "Deliverables": {
                "architecture_design": "Design of the alert system for monitoring patient records.",
                "database_schema_design": "Schema to support tracking and alerts for patient activities.",
                "unit_tests": "Tests to verify alert generation and accuracy.",
                "production_support_plan": "Plan for ongoing monitoring and updating of the alert system."
            }
        },
        {
            "User Story": "Provide comprehensive reporting capabilities to generate administrative and clinical reports on patient statistics, treatments, costs, clinic activity, patient flow, and legal compliance.",
            "Deliverables": {
                "architecture_design": "Design of the reporting system.",
                "database_schema_design": "Schema to support complex queries for generating reports.",
                "unit_tests": "Tests to ensure report accuracy and performance.",
                "user_training_documentation": "Documentation on how to generate and interpret reports."
            }
        },
        {
            "User Story": "Ensure system availability, manage data replication, and implement a data access logging system to maintain system integrity, privacy, and accessibility during network outages or server failures, and for compliance auditing.",
            "Deliverables": {
                "architecture_design": "Design of system redundancy, data replication, and logging mechanisms.",
                "database_schema_design": "Schema for logging access and changes to data.",
                "unit_tests": "Tests to ensure system resilience and logging accuracy.",
                "production_support_plan": "Plan for disaster recovery and data integrity checks."
            }
        }
    ]
}
"""

expected_tests ="""
{
  "test_cases": [
    {
      "requirement": "Implement a login system to ensure that only authorized medical staff and the patient can access patient data.",
      "test_cases": [
        {
          "case_id": "TC1_1",
          "description": "Verify that a valid medical staff member can log in using correct credentials.",
          "steps": ["Enter valid username and password for a medical staff member", "Submit login form"],
          "expected_result": "Login is successful and access to authorized patient data is granted."
        },
        {
          "case_id": "TC1_2",
          "description": "Verify that a valid patient can log in using correct credentials.",
          "steps": ["Enter valid username and password for a patient", "Submit login form"],
          "expected_result": "Login is successful and access to their own patient data is granted."
        },
        {
          "case_id": "TC1_3",
          "description": "Verify that users with invalid credentials cannot log in.",
          "steps": ["Enter invalid username and/or password", "Submit login form"],
          "expected_result": "Login is unsuccessful and access is denied with an error message displayed."
        },
        {
          "case_id": "TC1_4",
          "description": "Verify that logged in users cannot access data for which they are not authorized.",
          "steps": ["Log in as a specific user", "Attempt to access data not authorized for their user type"],
          "expected_result": "Access to the data is denied."
        }
      ]
    },
    {
      "requirement": "Record and maintain comprehensive patient information including consultations, conditions, treatments, and history.",
      "test_cases": [
        {
          "case_id": "TC2_1",
          "description": "Verify that new patient information can be added and saved correctly.",
          "steps": ["Log in as authorized medical staff", "Navigate to add new patient information page", "Enter all required patient details", "Submit the information"],
          "expected_result": "New patient information is saved correctly and can be retrieved accurately."
        },
        {
          "case_id": "TC2_2",
          "description": "Verify that existing patient information can be updated.",
          "steps": ["Log in as authorized medical staff", "Navigate to an existing patient's information page", "Update necessary details", "Submit the updated information"],
          "expected_result": "Patient information is updated correctly and changes are reflected immediately."
        }
      ]
    },
    {
      "requirement": "Regularly monitor patient records to generate alerts for missed appointments, prescription losses, and identify potentially dangerous patients.",
      "test_cases": [
        {
          "case_id": "TC3_1",
          "description": "Verify that the system generates alerts for missed appointments.",
          "steps": ["Simulate a missed appointment scenario", "Check for alerts in the system"],
          "expected_result": "An alert for the missed appointment is generated and visible to authorized staff."
        },
        {
          "case_id": "TC3_2",
          "description": "Verify that alerts are generated for prescription losses.",
          "steps": ["Record a prescription as lost in the system", "Check for alerts"],
          "expected_result": "An alert for the lost prescription is generated and visible."
        },
        {
          "case_id": "TC3_3",
          "description": "Verify that the system identifies and flags potentially dangerous patients.",
          "steps": ["Enter data for a potentially dangerous patient", "Check for flags or alerts associated with the patient profile"],
          "expected_result": "The system flags the patient as potentially dangerous and alerts the medical staff."
        }
      ]
    },
    {
      "requirement": "Provide administrative reporting capabilities to generate detailed reports on clinic activity, patient statistics, treatments, costs, patient flow, sectioning, and prescriptions.",
      "test_cases": [
        {
          "case_id": "TC4_1",
          "description": "Verify that the system can generate a report on clinic activity.",
          "steps": ["Log in as an administrator", "Navigate to the reporting section", "Select clinic activity report", "Generate the report"],
          "expected_result": "A detailed report on clinic activity is generated and contains accurate information."
        },
        {
          "case_id": "TC4_2",
          "description": "Verify that reports can be generated for patient statistics and treatments.",
          "steps": ["Log in as an administrator", "Navigate to the reporting section", "Select patient statistics and treatments report", "Generate the report"],
          "expected_result": "The report is generated and includes comprehensive details on patient statistics and treatments."
        }
      ]
    },
    {
      "requirement": "Ensure system compliance with data protection laws, maintain confidentiality of patient information, and implement a data access logging system for compliance auditing.",
      "test_cases": [
        {
          "case_id": "TC5_1",
          "description": "Verify that all data access is logged.",
          "steps": ["Access patient data", "Check the data access logs"],
          "expected_result": "All access to patient data is logged with details including who accessed the data and when."
        },
        {
          "case_id": "TC5_2",
          "description": "Verify that patient information is confidential and only accessible by authorized personnel.",
          "steps": ["Attempt to access patient information as an unauthorized user", "Check access control"],
          "expected_result": "Access is denied and the attempt is logged."
        }
      ]
    },
    {
      "requirement": "Maintain system availability, manage data replication, and ensure system resilience during network outages or server failures to balance privacy and accessibility.",
      "test_cases": [
        {
          "case_id": "TC6_1",
          "description": "Verify that the system remains available during a simulated network outage.",
          "steps": ["Simulate a network outage", "Attempt to access the system"],
          "expected_result": "System remains accessible using replicated data."
        },
        {
          "case_id": "TC6_2",
          "description": "Verify that data replication is functioning correctly.",
          "steps": ["Make changes to data in the primary system", "Check if changes are replicated to the backup system"],
          "expected_result": "Changes are replicated accurately and in a timely manner."
        }
      ]
    },
    {
      "requirement": "Monitor treatment involvement and track sectioned patients to ensure timely legal checks and compliance.",
      "test_cases": [
        {
          "case_id": "TC7_1",
          "description": "Verify that sectioned patients are tracked and monitored for legal checks.",
          "steps": ["Log in as authorized medical staff", "Navigate to the sectioned patients monitoring module", "Check compliance status and alerts"],
          "expected_result": "All sectioned patients are correctly tracked, and the system alerts for any required legal checks."
        }
      ]
    }
  ]
}
"""
