:::mermaid
graph TD
  subgraph cluster_GUI
    A[Create GUI]
    B[Set up buttons]
    C[Define hover effects]
    D[Define start_tracker function]
    E[Define stop_tracker function]
    F[Define update_variable function]
    G[Define show_page function]
    H[Define show_main_page function]
    I[Initialize App]
  end

  subgraph cluster_keycounter
    J[Import keyboard module]
    K[Define KeyCounter class]
    L[Initialize variables]
    M[Register key release callback]
    N[Define on_key_release function]
    O[Define print_variables function]
    P[Define run function]
    Q[Define stop function]
  end

  A -->|Initialize| I
  I -->|Create Buttons| B
  B -->|Define Hover Effects| C
  B -->|Define start_tracker function| D
  B -->|Define stop_tracker function| E
  B -->|Define update_variable function| F
  B -->|Define show_page function| G
  B -->|Define show_main_page function| H
  B -->|Pack main buttons| I

  J -->|Import| K
  K -->|Initialize| L
  L -->|Set up variables| M
  M -->|Register callback| N
  N -->|Define on_key_release function| O
  O -->|Define print_variables function| P
  P -->|Define run function| Q

  G -->|Show Page| H
  H -->|Show Main Page| I

  F -->|Schedule update| F
  F -->|Update Variable| Q
  D -->|Start Tracking| Q
  E -->|Stop Tracking| Q
