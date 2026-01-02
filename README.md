# BNG Blaster Controller WUI

------

## 1. Scope & Core Logic

The Web User Interface (WUI) acts as a **mediation layer between the web browser and the BNG Blaster controller interface**.

Its primary responsibilities are to:

- Manage BNG Blaster **Instances**
- Provide CRUD (Create / Read / Update / Delete) operations for configurations
- Control the instance lifecycle (Create / Delete / Start / Stop / Kill)
- Display execution status and test results

The WUI does not replace the controller logic but exposes it in a structured, user-friendly way while maintaining a strict mapping to the controller’s domain model.

------

## 2. Functional Modules

------

## 2.1 Instance & Lifecycle Management

The WUI directly implements the controller’s `Repository` interface logic within the Reflex `State`.

### Instance Discovery

- **Instance Gallery**
  - Grid or table view of all detected instances
  - Displays instance name and basic state information

------

### Provisioning

- **Create**
  - Modal dialog to define an instance `name`
  - Upload or generate a JSON `config`
- **Delete**
  - Removes configuration files from `ConfigFolder()`
  - Disabled while an instance is running

------

### Runtime Execution

- **Start Configuration**
  - UI form mapped to the `RunningConfig` structure
  - Includes toggles and inputs for:
    - `Report`
    - `Logging`
    - `PCAPCapture`
    - `SessionCount` overrides
- **Execution Flags**
  - Multi-select chips for:
    - `LoggingFlags` (e.g. `debug`, `igmp`, `pppoe`)
    - `MetricFlags` (e.g. `session_counters`, `interfaces`)
- **Process Control**
  - Distinct control buttons:
    - **Stop** (graceful termination)
    - **Kill** (forced termination)

------

## 2.2 Config Builder

The Config Builder is derived from and constrained by the `RunningConfig` data model.

Its primary goal is to **simplify the creation of valid BNG Blaster configurations** by exposing BNG Blaster–specific options through structured UI elements rather than free-form input.

### Design Principles

- BNG Blaster–specific options are presented using:
  - Dropdown menus
  - Checkboxes
  - Toggle switches
- Users select from **predefined, valid options**, reducing configuration errors.
- The UI does not hardcode protocol-, scenario-, or feature-specific values.

------

### Configuration Option Management (Config-Driven UI Definition)

All selectable UI options are defined in a **dedicated BBL-WUI configuration file (YAML)**.

This file acts as a **UI definition catalog**, not a test configuration.

It defines:

- Dropdown menu contents
- Checkbox and toggle groups
- Default values
- Optional help texts and descriptions
- Conditional visibility rules (e.g. scenario-based fields)
- Validation and constraint rules

The BBL-WUI configuration file:

- Is independent from controller logic and test configurations
- Can be updated without modifying UI or backend code
- Allows rapid adaptation to new BNG Blaster features

This approach ensures:

- Easy maintainability
- Reduced UI complexity
- Clear separation of concerns:
  - **Controller** → execution logic
  - **Config Builder** → guided configuration
  - **BBL-WUI config file** → domain knowledge and valid option sets

------

### Supported Configuration Areas

#### Generic Start and Logging Parameters

- Logging enable/disable (checkbox)
- Logging level and logging flags (multi-select dropdown)
- Report and PCAP capture toggles

#### PPPoE and DHCP–Specific Parameters

- **BNG Blaster scenario selection via dropdown menus**
  - L2-BSA
  - L3-BSA
- **Scenario-driven UI behavior**
  - Protocol- and scenario-specific parameters are shown or hidden dynamically
- **Externalized option definitions**
  - All selectable values, defaults, and constraints are sourced from the BBL-WUI configuration file

#### Interface Configuration

- Interface selection via dropdown menus
- Interface role assignment (Access / Network)
- Interface attributes configured via checkboxes and selectors
- Validation rules based on predefined interface types and scenario constraints

------

### Planned Extensions (Not in Initial Scope)

- Stream configuration
  - Stream profiles and parameters selectable via dropdown menus
- Protocol configuration
  - BGP
  - IS-IS

These extensions will follow the same design pattern:

- UI elements fully driven by the BBL-WUI configuration file
- No protocol-specific logic hardcoded into the UI

------

## 2.3 Result Viewer

The Result Viewer provides structured access to execution results and runtime data.

### Display Capabilities

- Session summary and session details
- Stream summary and stream details
- Log summary (aggregated and filtered views)

### Planned Extensions

- Download of capture files (PCAP)
  - Support will be added at a later stage

------

## 3. Non-Goals (Initial Version)

- Advanced stream configuration editing
- Protocol-level configuration (BGP, IS-IS)
- PCAP file inspection or visualization in the browser
