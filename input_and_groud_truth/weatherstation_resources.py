doc_text_raw = """
A wilderness weather station

To help monitor climate change and to improve the accuracy of weather forecasts in remote areas, the government of a country with large areas of wilderness decides to deploy several hundred weather stations in remote areas. These weather stations collect data from a set of instruments that measure temperature and pressure, sunshine, rainfall, wind speed, and wind direction.

Wilderness weather stations are part of a larger system, which is a weather information system that collects data from weather stations and makes it available to other systems for processing. The systems are:
1. The weather station system This is responsible for collecting weather data, carrying out some initial data processing, and transmitting it to the data management system.
2. The data management and archiving system This system collects the data from all of the wilderness weather stations, carries out data processing and analysis, and archives the data in a form that can be retrieved by other systems, such as weather forecasting systems.
3. The station maintenance system This system can communicate by satellite with all wilderness weather stations to monitor the health of these systems and provide reports of problems. It can update the embedded software in these systems. In the event of system problems, this system can also be used to remotely control a wilderness weather system.

Each system is a collection of components and has identified the separate systems. There is
an exchange of information but, at this stage, there is no need to define them in any more detail.
Each weather station includes a number of instruments that measure weather parameters such as the wind speed and direction, the ground and air temperatures, the barometric pressure, and the rainfall over a 24-hour period. Each of these instruments is controlled by a software system that takes parameter readings periodically and manages the data collected from the instruments.

The weather station system operates by collecting weather observations at frequent intervals—for example, temperatures are measured every minute. However, because the bandwidth to the satellite is relatively narrow, the weather station carries out some local processing and aggregation of the data. It then transmits this aggregated data when requested by the data collection system. If, for whatever reason, it is impossible to make a connection, then the weather station maintains the data locally until communication can be resumed.

Each weather station is battery-powered and must be entirely self-contained—there are no external power or network cables available. All communications are through a relatively slow-speed satellite link and the weather station must include some mechanism (solar or wind power) to charge its batteries. As they are deployed in wilderness areas, they are exposed to severe environmental conditions and may be damaged by animals.

The station software is therefore not just concerned with data collection. It must also:
1. Monitor the instruments, power, and communication hardware and report faults to the management system.
2. Manage the system power, ensuring that batteries are charged whenever the environmental conditions permit but also that generators are shut down in potentially damaging weather conditions, such as high wind.
3. Allow for dynamic reconfiguration where parts of the software are replaced with new versions and where backup instruments are switched into the system in the event of system failure. Because weather stations have to be self-contained and unattended, this means that the software installed is complex, even though the data collection functionality is fairly simple.

    """

expected_requirements = """
1. Collect weather data including wind speed and direction, ground and air temperatures, barometric pressure, and rainfall over a 24-hour period.
2. Perform initial data processing on collected weather data.
3. Transmit aggregated weather data to the Data Management and Archiving System upon request.
4. Store collected weather data locally if satellite communication is unavailable.
5. Monitor the status of weather station instruments, power, and communication hardware.
6. Report any faults or issues in the weather station system to the Station Maintenance System.
7. Manage system power to ensure battery charging during favorable environmental conditions and shut down power during adverse conditions.
8. Facilitate dynamic reconfiguration of the software and hardware components, including updating software and switching backup instruments into operation as needed.
9. Integrate with the Station Maintenance System for remote control and software updates.
10. Ensure data integrity and accuracy during collection, processing, and transmission phases.
11. Perform integration testing to ensure all components of the weather station system work together as intended.
"""

expected_epics = """"
{
    "Epics": [
        {
            "User Story": "Collect weather data including wind speed and direction, ground and air temperatures, barometric pressure, and rainfall over a 24-hour period.",
            "Deliverables": {
                "architecture_design": "Design of the data collection modules for various weather parameters.",
                "database_schema_design": "Schema for storing different types of weather data in the database."
            }
        },
        {
            "User Story": "Perform initial data processing on collected weather data to ensure data integrity and accuracy.",
            "Deliverables": {
                "architecture_design": "Design of data validation and cleaning processes.",
                "unit_tests": "Develop tests to ensure data processing maintains data integrity and accuracy."
            }
        },
        {
            "User Story": "Store collected weather data locally if satellite communication is unavailable and transmit aggregated weather data to the Data Management and Archiving System upon request.",
            "Deliverables": {
                "architecture_design": "Design of local data storage and data transmission modules.",
                "database_schema_design": "Schema for temporary local storage and management of data queues for transmission."
            }
        },
        {
            "User Story": "Monitor the status of weather station instruments, power, and communication hardware, and report any faults or issues to the Station Maintenance System.",
            "Deliverables": {
                "architecture_design": "Design of monitoring systems for hardware and communication status.",
                "production_support_plan": "Plan for ongoing monitoring and maintenance support."
            }
        },
        {
            "User Story": "Manage system power to ensure battery charging during favorable environmental conditions and shut down power during adverse conditions.",
            "Deliverables": {
                "architecture_design": "Design of power management system.",
                "user_training_documentation": "Documentation on managing and troubleshooting the power system."
            }
        },
        {
            "User Story": "Facilitate dynamic reconfiguration of the software and hardware components, including updating software, switching backup instruments into operation as needed, and integrate with the Station Maintenance System for remote control and software updates.",
            "Deliverables": {
                "architecture_design": "Design of system reconfiguration and update mechanisms.",
                "user_training_documentation": "Documentation for system administrators on reconfiguring and updating system components."
            }
        },
        {
            "User Story": "Perform integration testing to ensure all components of the weather station system work together as intended.",
            "Deliverables": {
                "unit_tests": "Develop comprehensive integration tests covering all system components."
            }
        }
    ]
}
"""

expected_tests = """
{
  "test_cases": [
    {
      "requirement": 1,
      "description": "Collect weather data including wind speed and direction, ground and air temperatures, barometric pressure, and rainfall over a 24-hour period.",
      "test_cases": [
        {
          "case_id": "TC1_1",
          "test_description": "Verify that the system collects wind speed data continuously over a 24-hour period."
        },
        {
          "case_id": "TC1_2",
          "test_description": "Verify that the system collects wind direction data continuously over a 24-hour period."
        },
        {
          "case_id": "TC1_3",
          "test_description": "Verify that the system collects ground temperature data continuously over a 24-hour period."
        },
        {
          "case_id": "TC1_4",
          "test_description": "Verify that the system collects air temperature data continuously over a 24-hour period."
        },
        {
          "case_id": "TC1_5",
          "test_description": "Verify that the system collects barometric pressure data continuously over a 24-hour period."
        },
        {
          "case_id": "TC1_6",
          "test_description": "Verify that the system collects rainfall data continuously over a 24-hour period."
        }
      ]
    },
    {
      "requirement": 2,
      "description": "Perform initial data processing on collected weather data to ensure data integrity and accuracy.",
      "test_cases": [
        {
          "case_id": "TC2_1",
          "test_description": "Verify that the system validates the format and range of the collected wind speed data."
        },
        {
          "case_id": "TC2_2",
          "test_description": "Verify that the system validates the format and range of the collected wind direction data."
        },
        {
          "case_id": "TC2_3",
          "test_description": "Verify that the system validates the format and range of the collected temperature data."
        },
        {
          "case_id": "TC2_4",
          "test_description": "Verify that the system validates the format and range of the collected barometric pressure data."
        },
        {
          "case_id": "TC2_5",
          "test_description": "Verify that the system validates the format and range of the collected rainfall data."
        }
      ]
    },
    {
      "requirement": 3,
      "description": "Store collected weather data locally if satellite communication is unavailable and transmit aggregated weather data to the Data Management and Archiving System upon request.",
      "test_cases": [
        {
          "case_id": "TC3_1",
          "test_description": "Verify that the system stores data locally when satellite communication is unavailable."
        },
        {
          "case_id": "TC3_2",
          "test_description": "Verify that the system transmits stored data to the Data Management and Archiving System when communication is restored."
        }
      ]
    },
    {
      "requirement": 4,
      "description": "Monitor the status of weather station instruments, power, and communication hardware, and report any faults or issues to the Station Maintenance System.",
      "test_cases": [
        {
          "case_id": "TC4_1",
          "test_description": "Verify that the system monitors and reports the operational status of weather station instruments."
        },
        {
          "case_id": "TC4_2",
          "test_description": "Verify that the system monitors and reports the status of power systems."
        },
        {
          "case_id": "TC4_3",
          "test_description": "Verify that the system monitors and reports the status of communication hardware."
        }
      ]
    },
    {
      "requirement": 5,
      "description": "Manage system power to ensure battery charging during favorable environmental conditions and shut down power during adverse conditions.",
      "test_cases": [
        {
          "case_id": "TC5_1",
          "test_description": "Verify that the system charges the battery when environmental conditions are favorable."
        },
        {
          "case_id": "TC5_2",
          "test_description": "Verify that the system shuts down power during adverse environmental conditions."
        }
      ]
    },
    {
      "requirement": 6,
      "description": "Facilitate dynamic reconfiguration of the software and hardware components, including updating software, switching backup instruments into operation as needed, and integrate with the Station Maintenance System for remote control and software updates.",
      "test_cases": [
        {
          "case_id": "TC6_1",
          "test_description": "Verify that the system can update software remotely."
        },
        {
          "case_id": "TC6_2",
          "test_description": "Verify that the system can switch backup instruments into operation without manual intervention."
        },
        {
          "case_id": "TC6_3",
          "test_description": "Verify that the system integrates with the Station Maintenance System for remote control operations."
        }
      ]
    },
    {
      "requirement": 7,
      "description": "Perform integration testing to ensure all components of the weather station system work together as intended.",
      "test_cases": [
        {
          "case_id": "TC7_1",
          "test_description": "Verify that all components of the weather station system work together without conflicts or data loss."
        }
      ]
    }
  ]
}
"""
