import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
def analyze_text(text):
    tokens = enc.encode(text)
    token_pieces = [enc.decode_single_token_bytes(t).decode('utf-8',
    errors='replace')
    for t in tokens]
    print("Original text:", text)
    print("Number of characters:", len(text))
    print("Number of tokens:", len(tokens))
    print("Tokens:", tokens)
    print("Token pieces:", token_pieces)
    print("-" * 60)

if __name__ == "__main__":
    # everyDayEnglish = "What is the weather like today?"
    # engineeringSentance = "What is the Vcc and Vdd pins on this microcontroller?"
    # mathUnits = "What is the speed of light in uS, years, and $$\\\\\\\\picoS$$?"
    # prompts = [everyDayEnglish, engineeringSentance, mathUnits]
    # for prompt in prompts:
    #     analyze_text(prompt)

    # microcontrollerPrompt = "How do I set the register value for an MSP430-FR23355 to turn off all interrupts?"
    # controlsystemPrompt = "Please provide the code required to simulate a self-tuning regulator. This should solve the PID constants."
    # machinelearningPrompt = "Please provide a detailed analysis on how the transformer machine learning architecture works."
    # matlabcodePrompt = "Please create MATLAB code that will plot the training results found in the data structure 'results.mat'."
    # electricitymagnatismPrompt = "Please use Coloumbs law to solve for two electrically charged particals place 1nm apart, with a charge of 10c."
    # motorPrompt = "Given a motor with a Kv of 523, stall torque of 4.21 amps, and an efficiency of 82% what is the torque production at stall?"
    # engineeringPrompts = [microcontrollerPrompt, controlsystemPrompt, machinelearningPrompt, 
    #                      matlabcodePrompt, electricitymagnatismPrompt, motorPrompt]

    # for engineeringPrompt in engineeringPrompts:
    #     analyze_text(engineeringPrompt)

    engineeringReportParagraph = """
        %----------------------------------------------------------------------------------------
        %	SECTION A:  Document declaration and packages used for Latex Compile
        %----------------------------------------------------------------------------------------
        \\documentclass[10pt]{report}
        \\usepackage{matlab-prettifier}

        \\usepackage{graphicx} 						% Required for the inclusion of images
        \\usepackage{geometry}                		% See geometry.pdf to learn the layout options. There are lots.
        \\geometry{letterpaper}                   		% ... or a4paper or a5paper or ...
        \\usepackage{amssymb,amsmath}		% Math packages
        \\usepackage{epstopdf}							% encapsulated postscript to pdf
        \\usepackage{color}	
        \\usepackage{rotating}
        \\usepackage{appendix}
        \\usepackage[capposition=top]{floatrow}
        \\usepackage{placeins}
        \\usepackage{enumitem}
        \\usepackage{listings}
        \\usepackage{gensymb}
        \\usepackage{cite}

        %----------------------------------------------------------------------------------------
        %	SECTION B:  New commands defined for use in this document, examples given, you may change
        %----------------------------------------------------------------------------------------
        \\newcommand{\\blu}[1]{\\textcolor{blue}{#1}}                     			% \\blu{} will make your font blue
        \\newcommand{\\red}[1]{\\textcolor{red}{#1}}
        \\definecolor{light-gray}{gray}{0.8}
        \\definecolor{orange}{rgb}{1,0.5,0}
        \\newcommand{\\gray}[1]{\\textcolor{light-gray}{#1}}

        %----------------------------------------------------------------------------------------
        %	SECTION C:  Lab Title
        %----------------------------------------------------------------------------------------
        \\title{Power Conversion Devices EELE 355\\\\ Transformers} 		% Title
        \\author{Drew Currie} 													% Author name
        \\date{\\today} 	

        \\begin{document}
        \\maketitle
        \\newpage

        %----------------------------------------------------------------------------------------
        %	SECTION D:  Contents
        %----------------------------------------------------------------------------------------
        \\tableofcontents 
        \\newpage
        %----------------------------------------------------------------------------------------
        %	Chapter 1:  Introduction
        %----------------------------------------------------------------------------------------

        \\chapter{Introduction}

        \\section{Objective}

        The goal of these labs was to test single and three-phase transformers under a variety of circumstances. The theory of each style of transformer was tested against the measured results using the Lucas N\\"{u}lle Lab Soft in conjuncture with the Lab Soft transformer work stations to allow for the creation of high voltage circuits. Through these labs, the various common configurations of transformers were created and tested. The measurements were collected with a digital multi-meter, and a desktop digital multi-meter. These tools allowed for the measurement of current and voltage across the circuits. The figures through this report will use notation in the circuit diagrams to represent where each multi-meter was connected to perform the measurements. 

        \\newpage
        \\chapter{Single-Phase Transformers}

        \\section{Single-phase transformers}
        The object of the Single-phase transformers section of the laboratory experiments are to verify the properties of single phase transformers by measuring the open-circuit voltage, and no-load current. 
        \\section{Open circuit voltage and current}
        This was achieved by creating the circuit shown below in figure 2.1. During this experiment, the hand-held multi-meter was used to measure current and the desktop multi-meter was used to measure the voltage. This setup provided a turns ratio of approximately 37:1. This is determined by the input voltage of approximately 4.44 volts and an output voltage of approximately 164V. Further experimental data is shown below in table 2.1. 

        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 75mm, keepaspectratio]{SinglePhaseTransformer1.png}
        \\caption{Open Circuit, No-Load Test Circuit}
        \\end{figure}
        This wiring linked the CO3636-7A transformer L2 on the Lab Soft transformer work stations with no load attached to the secondary side. As there was no load on the secondary side, this experiment measured the Open-Circuit Voltage on the secondary side  and No-Load current on the primary side. This resulted in the values shown below in Table 2.1. This worked to prove that although the ideal model of a transformer is convenient to use for approximations, it is not a suitable model for real transformers. 

        \\begin{center}
        \\begin{table}[!h]
        \\caption{Open Circuit, No-Load Test Circuit Experimental Data}
        \\begin{tabular}{ ||c|c|| } 
        \\hline
        Measured property &  Value \\\\
        \\hline
        Open-Circuit Current ($I_o$) & 29 mA \\\\
        \\hline
        Peak Open-Circuit Value (\\^{I}$_o$) & 41 mA \\\\
        \\hline
        Magnetomotive  Force Peak Value ($\\theta$) & 35 A \\\\
        \\hline
        Field Intensity Peak Value (\\^{H}) & 252 A/m \\\\
        \\hline\\
        Magnetic Flux Density Peak (B) & 1.3 T \\\\
        \\hline
        Open-Circuit voltage ($V_o$) & 164 V \\\\
        \\hline
        
        \\hline
        \\end{tabular}
        \\end{table}
        \\end{center}

        The methodology for collecting this data was to use the hand-held multi-meter to measure the No-Load current and the desktop Multi-Meter to measure the Open-Circuit voltage on the secondary side. Through measuring the current and voltage, $I_{in}$ and $V_o$ could be measured directly. However, all other values were calculated. These calculations are shown in the appendix under Calculations. 


        \\section{Turn Ratio}
        The mutual inductance property of coils based on Faraday's Law shows that a change in flux linkage in one coil of wire directly effects the flux linkage in a second coil of wire. This is the fundamental property that transformers operate on. The ratio of turns between these two coils of wire, Turn Ratio, determine the relationship between the Voltage and Current in one coil to the Voltage and Current in the second coil. Through this property, the coil of wire based on the number of turns is able to induce a voltage and current in a second coil, by using a ferromagnetic core of the wires, this energy transfer is increased. By calculating the turns ratio of the transformer a linear approximation can be determined for ideal transformers that is: 
        
        \\begin{equation}
            \\frac{N_1}{N_2} = \\frac{V_1}{V_2} = \\frac{I_2}{I_1}
        \\end{equation}

        Through this fundamental property more complex transformer loads and analysis can be done. As such it is imperative to determine the turns ratio accurately for a real transformer and not an ideal transformer. 
        
        \\subsection{Practical Transformer Model}
        During this section of the experiment, the transformer turns ratio was calculated and tested. This proved that while the ideal model is not exact to a real transformer it can be used to produce a close approximation when primary and secondary side coil resistances are very low relative to the input voltage and core has a high resistance and high impedance. Under these circumstances, the ideal model of a transformer more accurately predicts the behavior of the real transformer as the models are similar. This approximation is shown below in Figure 2.2. 

        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 55mm, keepaspectratio]{PracticalTransformerDiagram.jpg}
        \\caption{Practical Transformer Circuit Diagram}
        \\end{figure}

        As shown in the Circuit Diagram above, if the complex impedance of the $R_{FE}$ resistor and the $L_m$ inductor are sufficiently large the transform will approximate a model more similar to the ideal transformer. To reach the ideal transformer model, the primary and secondary side resistors, $R_p$ and $R_s$ respectively, must also be sufficiently small compared to the voltages in the system. This would decrease the magnetic fields lost to the core in eddy currents and power lost to ohmic heating of the resistors. If the inductors of in the primary and secondary coils are small the loss of magnetic fields to the surrounding environment will also be small. By making these assumptions, the ideal transformer model is created. By using the ideal transformer model in this way, the voltage on the secondary coil can be related to the primary through:
        \\newline 
        \\begin{equation}
            V_{in} = \\frac{N_{primary}}{N_{secondary}}*V_o
        \\end{equation}

        where $N_{primary}$ and $N_{secondary}$ are the number of turns in the primary and secondary coils respectively. 

        By applying this model of the ideal transformer to the Lab Soft transformer work station, the number of turns on the primary is set to 680 and the secondary is set to 2 * 682. This will create a turns ratio that is approximately 0.498. The transformer was setup as shown in the circuit diagram below. This was done to create an input voltage at approximately mains power, and an output voltage that is approximately twice the amplitude. 

        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 55mm, keepaspectratio]{TurnsRatioSinglePhaseTransformer.png}
        \\caption{Circuit diagram for measuring turns ratio}
        \\end{figure}
        \\subsection{Turn Ratio Experiment Methodology}
        During this setup, the hand-held multi-meter was connected across the primary coil of the transformer to measure the input voltage, while the desktop multi-meter was connected across the secondary coil of the transformer to measure the output voltage. The input voltage was measured to be 122.5V and the output voltage to be 243.6v. This would indicate a turns ratio of approximately 0.502. This is higher than the expected value of 0.498 based on the properties of the transformer. This shows some of the imperfections of using the ideal model of the transformer. The ideal model would have predicted an output voltage of 245.72V, this is only a $0.86\\%$ error compared to the expected value however, this is due to the high voltage and comparatively low resistances and inductance's of the transformer. 

        \\section{No-load characteristic}
        To measure the no-load characteristics of the transformer, the hand-held multi-meter was setup to measure the current through the primary side coil and the desktop multi-meter was setup to measure the voltage across the primary side coil. To measure the output voltage with respect to the input voltage, the input voltage was increased to calculate the output voltage using equation (2.2). A plot was generated shown in Fig. 2.4, this plot relates $V_o$ and $I_o$. 

        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 55mm, keepaspectratio]{OutputCurrentVsOutputVoltage.png}
        \\caption{Output Current ($I_o$) vs. Output Voltage ($V_o$)}
        \\end{figure}

        This plot shows the non-linear correlation of the transformer. The output current and output voltage do not linearly scale to the input voltage and current. With an ideal transformer this would scale linearly as the Ideal Transformer Model predicts a linear ratio of current and voltage across the transformer. The non-linear behavior of the system shows that the losses due to the coil impedance's and core impedance's have a larger impact at a low input voltage. A more concentrated diagram is shown below in Fig 2.5 of the low input voltages, 0 to 40V. 

        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 55mm, keepaspectratio]{OutputCurrentVsOutputVoltage0-40v.png}
        \\caption{Concentrated Output Current ($I_o$) vs. Output Voltage ($V_o$)}
        \\end{figure}

        At the lower input voltages, the resistors create a significant voltage drop in series with the primary coil and secondary coil compared to the high voltages where the voltage drop is less noticeable. This is because at lower voltages, the voltage divider that is created reduces the voltages as the input voltage is not high enough to deliver the full voltage to the primary coil. 


        \\section{Load types and parameters}

        The goal of this experiment was to determine how practical transformers respond under various loads attached to the secondary side. When viewing the equivalent circuit of the practical transformer, shown below, the impedance of the secondary side load will effect the voltage and current of the transformer.  

        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 55mm, keepaspectratio]{TransformerEquivelantCircuit.jpg}
        \\caption{Transformer Equivalent Circuit}
        \\end{figure}

        As shown in the circuit diagram above, the load impedance, Z, would create varying electrical properties in the transformer. This equivalent circuit shows the secondary side of the transformer reflected over to the primary side. This allows for more traditional circuit analysis to be performed on the transformer. By changing load type, the circuit response to the input voltage will change. If the secondary side is an open circuit, the power required to hold the secondary side voltage is low, this changes when adding resistive elements and reactive power elements. 

        \\subsection{No Load}

        To test a no load scenario, the transformer at the Lab Soft Workstation was configured as shown in Fig 2.7. This allowed for measuring the current through the secondary side, and voltage across the secondary side of the transformer. 

        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 55mm, keepaspectratio]{No-LoadLoadTypesCircuitDiagram.png}
        \\caption{No Load Load Type}
        \\end{figure}

        \\subsection{No Load Experiment Methodology}
        To measure the no load characteristics of the secondary side, the hand-held multi-meter was used in series with the secondary coil to measure the secondary coil current with no load. The desktop multi-meter was connected across the transformer to measure the voltage across the secondary side. These measurements are shown in table 2.2. 

        \\begin{center}
        \\begin{table}[!h]
        \\caption{Open Circuit, No-Load Test Circuit Experimental Data}
        \\begin{tabular}{ ||c|c|| } 
        \\hline
        Measured property &  Value \\\\
        \\hline
        Open-Circuit Current ($I_{secondary}$) & 0.2 mA \\\\
        \\hline
        Open-Circuit Voltage ($V_{secondary}$) & 241 V \\\\
        \\hline
        \\end{tabular}
        \\end{table}
        \\end{center}

        The expected results would have been no current measured on the secondary side, however, due to the completion of the circuit with the multi-meters and the ability for the secondary side to leak current a small current was measured. Compared to the secondary side voltage of 241v, the power loss is approximated to be:

        
        \\begin{equation}
            Power_{loss} = 241v * 0.0002A = 0.0482Watts
        \\end{equation}

        This loss of power is negligible compared to the input voltage of system at 120V$_{ac}$. With the small current measured through the secondary side, it can be assumed that this experiment closely follows the expected results of the open circuit load. In the Transformer Equivalent Circuit Diagram, Fig. 2.6,  if there is no load, an open circuit is created. This would allow the transformer circuit to hold a consistent voltage with minimal power draw. 

        \\subsection{Resistive Load}
        A resistive load will only use active power this prevents the reactive power of a load from creating reverse voltage or current during the voltage change of the AC input voltage. However, unlike the no-load scenario the resistive load will require more power to maintain the output voltage. The current measured through the secondary side transformer is expected to increase in order to hold the desired output voltage. 

        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 55mm, keepaspectratio]{ResistiveLoadLoadTypeCircuitDiagram.png}
        \\caption{Resistive Load Load Type}
        \\end{figure}

        \\subsection{Resistive Load Experiment Methodology}

        To measure the properties of a transformer with a resistive load on the secondary side, an incandescent light bulb was attached across the secondary coil. The hand-held multi-meter was connected in series with the light bulb in order to measure the current used by the resistive load on the secondary side. The desktop multi-meter was connected in parallel with the secondary side coil to measure the voltage across the coil and light bulb. As expected, to meet the power requirements of the resistive load at the secondary side voltage, the current increased. The current was measured to be 100mA in this experiment. Calculating the power using the same process as equation (2.3), the active power is 22w. This is to meet the required power of the light bulb to turn on. The measured values are shown in the table below.  



        \\begin{center}
        \\begin{table}[!h]
        \\caption{Open Circuit, No-Load Test Circuit Experimental Data}
        \\begin{tabular}{ ||c|c|| } 
        \\hline
        Measured property &  Value \\\\
        \\hline
        Resistive Load Current ($I_{secondary}$) & 100 mA \\\\
        \\hline
        Resistive Load Voltage ($V_{secondary}$) & 220 V \\\\
        \\hline
        \\end{tabular}
        \\end{table}
        \\end{center}

        A drop of approximately 20V$_{ac}$ is measured on the resistive load compared to the Open Circuit/No Load test case. This is because of the increased current draw on the secondary side. The transformer is no longer able to maintain a consistent 241v$_{ac}$ on the output as the current draw has increased to meet power demands. This shows one of the downsides to the ideal model, if an ideal voltage source is used for calculating expected values, the measured values will decrease as current draw increases in the system. An extreme example of this would be shorting the secondary side coil as the current draw would rapidly increase while the voltage would decrease to conserve power.  

        \\subsection{Inductive Load}

        An inductive load will only use reactive power this is because the inductor is assumed to be an ideal inductor without any series resistance. The reactive power of the system is due to the fundamental properties of the inductor under AC voltage at steady state. During steady state operation with AC analysis, the inductor will only allow for DC components of the AC voltage to pass through. When the voltage changes during AC operation, the inductor will create an opposing current preventing the flow of current. As such the active power usage of an ideal inductor is considered to be 0. The inductor will still dissipate some power through the series resistance of real inductors and through the reactive power of the inductor. As such, the voltage on the secondary coil is expected to decrease as the current increases to meet this power dissipation. 



        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 55mm, keepaspectratio]{ResistiveLoadLoadTypeCircuitDiagram.png}
        \\caption{Inductive Load Load Type}
        \\end{figure}

        \\subsection{Inductive Load Experiment Methodology}

        To measure the behavior of the transformer with an inductive load, the secondary side was connected to an inductor. The hand-held multi-meter was connected in series with this inductor to measure current. The desktop multi-meter was connected in parallel to the inductor to measure the voltage across the inductor. This circuit is shown in Fig. 2.9. In reference to the Transformer Equivalent Circuit, when the system reaches steady state for an AC voltage, the current through the inductor is expected to decrease. This is due to the fundamental properties of inductors, during steady state operation with AC circuits, the inductor will prevent the rapid change of current by creating an opposing current. Through this it is expected the secondary side voltage will be higher than the resistive load but lower than the open circuit load. This is because although the input voltage is AC it still has a small DC component which will flow through the inductor at steady state. The measured current was 80 mA and the measured voltage was 230V$_{ac}$. This is shown in the table 2.4. 

        \\begin{center}
        \\begin{table}[!h]
        \\caption{Open Circuit, No-Load Test Circuit Experimental Data}
        \\begin{tabular}{ ||c|c|| } 
        \\hline
        Measured property &  Value \\\\
        \\hline
        Inductive Load Current ($I_{secondary}$) & 80 mA \\\\
        \\hline
        Inductive Load Voltage ($V_{secondary}$) & 230 V \\\\
        \\hline
        \\end{tabular}
        \\end{table}
        \\end{center}

        A decrease of 10v$_{ac}$ was observed for the inductive load compared to the Open Circuit/No Load test. This is because of the increased reactive power of the inductor. The reactive power of the load can be determined with the equation below. The calculation for the reactance of the inductor is shown in the Appendix in the Calculations section. 

        
        \\begin{equation}
            Q_{load} = \\frac{230^2}{2639.94} = 20.04 VAR
        \\end{equation}

        This shows the reactive power of the inductor as a load on the secondary side of the transformer. As this is assuming the ideal model of an inductor, the active power dissipated for the series resistance of the inductor is considered to be 0. Due to the reactive power of the inductor, the voltage decreases on the secondary side as the current increased due to the load. This is to conserve total energy in the system.  

        \\newpage
        \\subsection{Capacitive Load}
        A capacitive load will only use reactive power, this is because the capacitor is assumed to be an ideal capacitor. The reactive power is due to the fundamental properties of the capacitor. At AC steady state the capacitor will allow for AC current to pass through acting as a short circuit. However, given that the capacitor used in Lab Soft Work Bench is only a 1$uF$ capacitor, it will not show these properties as the frequency is too low at 60$hz$ compared to the capacitance of the capacitor. This means the capacitor will be able to fully charge before the AC voltage has changed polarity. 


        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 55mm, keepaspectratio]{CapactiveLoadLoadTypeCircuitDiagram.png}
        \\caption{Capacitive Load Load Type}
        \\end{figure}

        \\subsection{Capacitive Load Experiment Methodology}
        Measuring the properties of the transformer with a capactive load was achieved by, connecting the hand-held multi-meter in series with the capacitor and the desktop multi-meter in parallel with the capacitor. The hand-held multi-meter was set to measure the current through the capacitor and the desktop multi-meter to measure the voltage across the capacitor. As the desktop multi-meter was measuring in DC mode, the change in the voltage across the capacitor would not be reflected in the 60$hz$ AC voltage. This is shown in Fig. 2.10. While a higher capacity capacitor would not change voltage a 1$uf$ capacitor would change voltage during the rise and fall of the AC 60$hz$ input voltage. The current was measured at 84mA and the voltage to be 255v. This is a reasonable measurement as the capacitor will dissipate some power through the reactive power of the capacitor. However, the voltage on the output side was shown to increase. This is due to the capacitor being able to charge above the input voltage for AC circuits. The recorded values are shown in the table 2.5. 


        \\begin{center}
        \\begin{table}[!h]
        \\caption{Open Circuit, No-Load Test Circuit Experimental Data}
        \\begin{tabular}{ ||c|c|| } 
        \\hline
        Measured property &  Value \\\\
        \\hline
        Capacitive Load Current ($I_{secondary}$) & 84 mA \\\\
        \\hline 
        Capacitive Load Voltage ($V_{secondary}$) & 255 V \\\\
        \\hline
        \\end{tabular}
        \\end{table}
        \\end{center}

        An increase of 15v$_ac$ was observed for the capactive load compared to the Open Circuit/No Load test. This is because of the increased reactive power of the capacitor. The reactive power of the load can be determined with the equation below. The calculation for the reactance of the capacitor is shown in the Appendix in the Calculations section. 

        
        \\begin{equation}
            Q_{load} = \\frac{255^2}{-2652.58} = -24.51 VAR
        \\end{equation}

        This shows how the reactive power of the capacitor can decrease the power draw of the load by producing a negative reactive power. By using a combination of capacitors and inductors, transformers can be constructed that maximize resistive load power delivery. This decreases the power lost to the load when using transformers. 


        \\chapter{Three-phase transformers}

        Three phase transformers build on the same fundamental properties of the single phase transformer. This system works by connecting each phase to a coil on a common core. An example of this wiring is shown below.

        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 75mm, keepaspectratio]{WyeBlanacedLoad.png}
        \\caption{3 Phase Transformer: Balanced Wye configuration}
        \\end{figure}

        In the balanced Wye configuration shown in Fig. 3.1, both the primary and secondary side of the transformer are connected in the Wye configuration. The properties of this configuration will be covered in the next section of this report. Alternatively to a Wye configuration a three phase transformer can connected in a Delta configuration. An example of a balanced Delta configuration three phase transformer primary side with a Wye configuration secondary side is shown below. 

        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 75mm, keepaspectratio]{DeltaWyeBalancedLoad.png}
        \\caption{3 Phase Transformer: Balanced Delta, Wye configuration}
        \\end{figure}

        This configuration, Fig. 3.2, of the Delta configuration on the primary and Wye configuration on the secondary allows for the voltages to be more easily measured on the secondary side. Additionally, as this was a balanced load, it can be proven that mixing configuration types can still result in a balanced transformer. This will be covered in the Delta Configuration Transformer section. 


        \\section{Wye Configuration Transformers}
        The advantage of using a Wye Configuration for the primary side of a transformer is that the Wye Configuration allows for multiple voltages to be applied to each phase independently. This creates a transformer where multiple output voltages can be created on the secondary side for different load types. Additionally, if one coil of the primary side does not work, the Wye configuration will still continue to supply some voltage to each of the other two transformer coils on the primary side. This creates an output where two phases will have voltage while the third, broken phase, will have no voltage. As such some loads will still function properly at a reduced capacity. The downside is that some loads will not function at all without the third phase which renders the system useless. 


        \\subsection{Balanced Load}

        In the case of a balanced load, it is expected that each of the output voltages and current will be similar to each other. This is because each coil on the transformer acts as an independent transformer for that load, each supplying the same input voltage and frequency. In this lab experiment for the Wye configuration transformers this was 120v$_{ac}$. 

        \\subsection{Balanced Load Experiment Methodology}
        The Lab Soft Work Station was wired as per the wiring diagram shown in Fig. 3.3. The hand-held multi-meter was connected to the primary side phase one input to measure the current through this phase. The Desktop multi-meter was set to measure across the output voltage of the phase one secondary side transformer. A resistive load was connected to each phase of the secondary side transformer. This created a balanced resistive load on each phase, this was achieved with the use of an incandescent light bulb on each phase. 


        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 75mm, keepaspectratio]{WyeBlanacedLoad.png}
        \\caption{3 Phase Transformer: Balanced  Wye configuration}
        \\end{figure}



        By repeating this process and measuring each phase the output voltage versus input current was recorded in the table shown in table 3.1. If the transformer, input voltage, and resistive loads were all ideal each phase of the transformer would be identical in magnitude. However, there were slight differences measured due to this imperfections. 

        \\begin{center}
        \\begin{table}[!h]
        \\caption{Open Circuit, No-Load Test Circuit Experimental Data}
        \\begin{tabular}{ ||c|c|| } 
        \\hline
        Measured property  and Phase &  Value \\\\
        \\hline
        V$_{2U}$ & 221 V \\\\
        \\hline 
        V$_{2V}$ & 220.7 V \\\\
        \\hline
        V$_{2W}$ & 216 V \\\\
        \\hline 
        I$_{1U}$ & 220 mA \\\\
        \\hline 
        I$_{1V}$ & 214 mA \\\\
        \\hline
        I$_{1W}$ & 225.5 mA \\\\
        \\hline 
        \\end{tabular}
        \\end{table}
        \\end{center}


        \\subsection{Unbalanced Load}
        An unbalanced load was created in the laboratory experiment by connecting two phases of the secondary side transformer to resistive loads while leaving one phase as an open-circuit. This created an unbalanced load on the secondary side. A similar methodology was used to the balanced load to measure the current and voltage on each phase. 

        \\subsection{Unbalanced Load Experiment Methodology: 2 Load}
        To test each phase of the transformer in an unbalanced load configuration, the circuit shown in Fig. 3.4, was created on the Lab Soft Work Station. The hand-held multi-meter was connected to to measure the current through the primary side of the phase and the desktop multi-meter was connected to measure the voltage across the output phase. 



        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 75mm, keepaspectratio]{WyeUnbalancedLoad.png}
        \\caption{3 Phase Transformer: Unbalanced Two Load  Wye configuration}
        \\end{figure}

        As expected from the properties of the Wye configuration and previous Open Circuit experiments, the Wye configuration had less current draw on the phase with no load. This is because the power required to maintain the output voltage on that phase is much lower than the other phases. The difference in power draw is similar to that of the single phase transformer load comparing the no load to resistive load. The data collected is shown in table 3.2. 


        \\begin{center}
        \\begin{table}[!h]
        \\caption{One load, Two No-Load Test Circuit Experimental Data}
        \\begin{tabular}{ ||c|c|| } 
        \\hline
        Measured property  and Phase &  Value \\\\
        \\hline
        V$_{2U}$ & 224 V \\\\
        \\hline 
        V$_{2V}$ & 222 V \\\\
        \\hline
        V$_{2W}$ & 235 V \\\\
        \\hline 
        I$_{1U}$ & 186 mA \\\\
        \\hline 
        I$_{1V}$ & 196 mA \\\\
        \\hline
        I$_{1W}$ & 95.5 mA \\\\
        \\hline 
        \\end{tabular}
        \\end{table}
        \\end{center}

        \\subsection{Unbalanced Load Experiment Methodology: 1 Load}

        To test each of the Wye configuration phases with an unbalanced one load, two no load configuration, the circuit shown below was created on the Lab Soft Work Station. The hand-held multi-meter was used to measure the current through the primary side for each phase. The desktop multi-meter was used to measure the voltage at each phase of the secondary side. This circuit diagram is shown in Fig. 3.5. This process was repeated one phase at a time to collect experimental data for each phase. As expected for Wye configuration transformer, the phase with the load, U, had a higher current draw and less voltage than the other phase

        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 75mm, keepaspectratio]{SingleLoadWyeConfiguration.png}
        \\caption{3 Phase Transformer: Unbalanced One Load  Wye configuration}
        \\end{figure}

        The data collected for this transformer circuit is shown in table 3.3. The data matches the expected change in voltage and current for the phases with no load compared to the phase with the load. This makes sense as the phase with the resistive load would require more power to hold the output voltage compared to the phases without a load. 


        \\begin{center}
        \\begin{table}[!h]
        \\caption{Two load, No-Load Test Circuit Experimental Data}
        \\begin{tabular}{ ||c|c|| } 
        \\hline
        Measured property  and Phase &  Value \\\\
        \\hline
        V$_{2U}$ & 225.5 V \\\\
        \\hline 
        V$_{2V}$ & 240 V \\\\
        \\hline
        V$_{2W}$ & 240 V \\\\
        \\hline 
        I$_{1U}$ & 155 mA \\\\
        \\hline 
        I$_{1V}$ & 93.4 mA \\\\
        \\hline
        I$_{1W}$ & 67.2 mA \\\\
        \\hline 
        \\end{tabular}
        \\end{table}
        \\end{center}

        \\newpage
        \\section{Delta Configuration Transformer}
        The advantage of using the Delta configuration for the primary side of the transformer is that the Delta configuration is more reliable for producing the correct output voltage on the secondary side of the transformer. If one phase of the Delta configuration primary side transformer is not working, the secondary side will still receive the full voltage on each phase. This makes a Delta configuration more robust and able to withstand more environmental disturbances. 

        \\subsection{Balanced Load}


        In the case of a balanced load, it is expected that each of the output voltages and current will be similar to each other. This is because each coil on the transformer acts to equalize the secondary side voltages and currents in a primary side Delta configuration and Wye configuration secondary side. This was measured to be true as each phase of the output voltage was 220v and the current through each phase was approximately 227mA. 

        \\subsection{Balanced Load Experiment Methodology}
        The Lab Soft Work Station was wired as per the wiring diagram shown in Fig. 3.6. The hand-held multi-meter was connected to the primary side phase one input to measure the current through this phase. The Desktop multi-meter was set to measure across the output voltage of the phase one secondary side transformer. A resistive load was connected to each phase of the secondary side transformer. This created a balanced resistive load on each phase, this was achieved with the use of an incandescent light bulb on each phase. 


        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 75mm, keepaspectratio]{DeltaWyeBalancedLoad.png}
        \\caption{3 Phase Transformer: Balanced  Delta, Wye configuration}
        \\end{figure}

        Measuring each phase was repeated for the output voltage and input current. 
        By repeating this process and measuring each phase the output voltage versus input current was recorded in table 3.4. If the transformer, input voltage, and resistive loads were all ideal each phase of the transformer would be identical in magnitude. The difference between the Wye and Delta configuration primary side input was that the Delta configuration was able to handle the slight differences on each phase better by maintaining a consistent output voltage and input current on each phase. 

        \\begin{center}
        \\begin{table}[!h]
        \\caption{Open Circuit, No-Load Test Circuit Experimental Data}
        \\begin{tabular}{ ||c|c|| } 
        \\hline
        Measured property  and Phase &  Value \\\\
        \\hline
        V$_{2U}$ & 220 V \\\\
        \\hline 
        V$_{2V}$ & 220 V \\\\
        \\hline
        V$_{2W}$ & 220 V \\\\
        \\hline 
        I$_{1U}$ & 227 mA \\\\
        \\hline 
        I$_{1V}$ & 227 mA \\\\
        \\hline
        I$_{1W}$ & 227 mA \\\\
        \\hline 
        \\end{tabular}
        \\end{table}
        \\end{center}

        As shown by the collected data, the delta configuration was able to maintain the same voltage on the secondary of each phase. This is why Delta configurations are more robust for use in power transmission system. By equalizing the output voltages the system will reliably produce the same output regardless of the slight variations in the loads and imperfections in the transmissions lines and transformer. 


        \\subsection{Unbalanced Load}
        An unbalanced load was crated in the laboratory experiment in the same way that the unbalanced load of the Wye configuration was created. The test methodology was the same as for the unbalanced Wye configuration systems. 

        \\subsection{Unbalanced Load Experiment Methodology: 2 Load}
        To test each phase of the Delta, Wye configuration unbalanced load, the circuit shown in Fig. 3.7, was created on the Lab Soft Work Station. The hand-held multi-meter was used to measure the current through one phase of the primary at a time and the desktop multi-meter was used to measure the output voltage of each phase. The Delta configuration is expected in this case to have a varying load voltage as the Delta configuration will attempt to supply the same voltage to each phase of the secondary side but due to the different power requirements for each phase will be unable to provide the appropriate voltage to each phase as current draw increases. 

        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 75mm, keepaspectratio]{TwoLoadDeltaConfiguration.png}
        \\caption{3 Phase Transformer: Unbalanced One Load  Delta, Wye configuration}
        \\end{figure}

        As expected from the properties of the Delta, Wye configuration and previous Open Circuit and unbalanced load experiments, the voltage varies slightly on each output phase. This is due to the various output power requirements of each load. The Delta configuration on the primary side will attempt to equalize the voltage and current through each phase to match the total power requirements of each phase. Given the ideal model for a three-phase transformer with a delta, Wye configuration, this increased power draw is expected for the total system. 

        \\begin{center}
        \\begin{table}[!h]
        \\caption{Two load, One No-Load Test Circuit Experimental Data}
        \\begin{tabular}{ ||c|c|| } 
        \\hline
        Measured property  and Phase &  Value \\\\
        \\hline
        V$_{2U}$ & 225 V \\\\
        \\hline 
        V$_{2V}$ & 220 V \\\\
        \\hline
        V$_{2W}$ & 235 V \\\\
        \\hline 
        I$_{1U}$ & 128 mA \\\\
        \\hline 
        I$_{1V}$ & 215 mA \\\\
        \\hline
        I$_{1W}$ & 140 mA \\\\
        \\hline 
        \\end{tabular}
        \\end{table}
        \\end{center}

        As expected the Delta configuration is attempting to normalize the voltage across all the phases as there is an increase of current through the phases with no load. This is due to the conservation of energy and the properties of the Delta configuration. 


        %Update starting here!
        \\subsection{Unbalanced Load Experiment Methodology: 1 Load}
        In order to test each of the Delta configuration phases with an unbalanced one load, two no load configuration, the circuit shown in Fig. 3.8, was created. This put one resistive load on a single phase and two open circuits on the other phases. The hand-held multi-meter was used to measure the current through the primary side phases and the desktop multi-meter was used to measure the voltage at each secondary phase. Repeating this measurement for each of the phases, the table below of experimental data was collected. As expected the Delta configuration was able to handle the single load unbalanced load better than the two load unbalanced load. The voltages across each phase were more consistent with only the phase with the single load decreasing. 

        \\begin{figure}[!h]
        \\centering
        \\includegraphics[height = 75mm, keepaspectratio]{DeltaWyeUnbalancedLoadOneLoad.png}
        \\caption{3 Phase Transformer: Unbalanced One Load  Delta, Wye configuration}
        \\end{figure}

        The experimental data for this transformer circuit is shown in table 3.6.  This data matches the predicted ability for the Delta, Wye configuration to better handle the unbalanced load with two open circuits. This is because the Delta configuration will attempt to supply the same voltage to each phase which divides the power requirements across each phase of the Delta configuration primary side. 


        \\begin{center}
        \\begin{table}[!h]
        \\caption{One load, Two No-Load Test Circuit Experimental Data}
        \\begin{tabular}{ ||c|c|| } 
        \\hline
        Measured property  and Phase &  Value \\\\
        \\hline
        V$_{2U}$ & 225 V \\\\
        \\hline 
        V$_{2V}$ & 240 V \\\\
        \\hline
        V$_{2W}$ & 242 V \\\\
        \\hline 
        I$_{1U}$ & 150 mA \\\\
        \\hline 
        I$_{1V}$ & 140 mA \\\\
        \\hline
        I$_{1W}$ & 30 mA \\\\
        \\hline 
        \\end{tabular}
        \\end{table}
        \\end{center}
        %Through here!

        \\chapter{Conclusions}

        Through the experiments with both single and three phase transformers, it is shown that transformers are an efficient way to transmit power between to isolated systems. By using the property of mutual inductance with two coils of wire. As Faraday's law proved in 1831, part of a magnetic field in one coil of wire can induce a voltage in another coil of wire proportional to number of turns in each coil. This is further improved by using a ferromagnetic core for the coils to focus the transfer of the magnetic energy.  By doing so the ideal model for the transformer was created. During the open circuit models for the transformer it was proven that the ideal model while not accurate of a real transformer is a useful tool to predict the expected behavior of the transformer. In high voltage applications, it was shown that the ideal model more accurately reflects the real transformer. This is because the series voltage drops of the complex impedance's of the coils of wire have less effect on the final voltage.  

        With three phase transformers various configurations in balanced and unbalanced loads were tested to verify the fundamental physics of each. Additionally, this served to prove why a Delta or Wye configuration may be used in power systems. Using either system has advantages with either reliability or load variants. The benefits of these systems to efficiently transfer power across large distances contribute to the fundamental back bone of the power grid. Without being able to use three phase transformers to efficiently change voltages with varying load types, the power grid would not be able to function. Using Wye transformers power per phase can be delivered based on the per phase usage while Delta, Wye transformers can be used to provide an equal starting voltage for to each phase for making consistent grid power. 

        \\noindent


        \\clearpage
        \\chapter{Appendix}
        \\section{References}

        [1] R. Linnertz, “ILA - Course ‘Single-phase and three-phase transformers’ ENT5,” Lucas-Nülle GmbH, Mar. 2024.s
        \\newline
        \\noindent
        [2] Kwan Yau Tang, Alternating-current Circuits. 1947.
        \\newline
        \\noindent
        [3] “Why Wye Connection? Why Delta Connection?,” Pumps and Systems Magazine, May 21, 2013. https://www.pumpsandsystems.com/why-wye-connection-why-delta-connection
        \\newpage
        \\section{Calculations}
        \\subsection{Open Circuit voltage and current }
        \\begin{center}
        \\^{I}$_o  = \\sqrt{2}*I_0 = 41 mA$
        \\newline

        $\\theta = $\\^{I}$_o * N_2 = 35 A$
        \\newline

        \\^{H} $ = \\frac{\\theta}{I_{FE}} = 252 \\frac{A}{m}$
        \\newline

        $V_0 = 4.44 * B * A * f * N_2 = 164 V$
        \\newline
        \\end{center}
        \\subsection{Reactive Power Loads}
        \\begin{center}
        $X_L = 2* \\pi * f * L $

        $X_c =  \\frac{-1}{2*\\pi*f*c}$

        \\end{center}
\\end{document}
    """
    analyze_text(engineeringReportParagraph)