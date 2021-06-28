import webbrowser as web
print('Hello freinds to chemcity,this is a program which tells you about  blocks of periodic table')

name = input("""What do you want to know about(type'b' if you want to know about a block in periodic table):  """).lower()

if name == 'b':
    print('There are 4 blocks in periodic table.They are S,P,D and F block.')
    block = input('Which block do you want to know about: ').lower()
    if block == 's':
        print("""S block comprises of 2 groups namely alkali metals and alkali earthly metals.The last electron in these
        elements enter in s orbital.Their general valence configuration is ns1–2.
        Alkali metals comprises of Li(Lithium),Na(sodium),K(Potassium),Rb(rubidium),Cs(cesium),Fr(francium).All alkali
         metals have their outermost electron in an s-orbital this shared electron configuration results in their having
        very similar characteristic properties. Indeed, the alkali metals provide the best example of group trends in
           properties in the periodic table, with elements exhibiting well-characterised homologous behaviour. This 
           family of elements is also known as the lithium family after its leading element.
              Alkaline earth metals comprises of Be(berylium),Mg(magnesium),Ca(calcium),Sr(strontium),Ba(barium),
              Ra(radium).They are all shiny, silvery-white, somewhat reactive metals at standard temperature and
               pressure.""")
        user1 = input('Do u want more information about s block(y for yes and n for no: ').lower()
        if user1 == 'y':
            web.open('simple.wikipedia.org/wiki/S-block')
        elif user1 == 'n':
            print('Bye see you later')
        else:
            print('Please check your input')
    elif block == 'p':
        print("""P block consists of 6 groups from 13 to 18.Its groups are:
        1. Boron family(13th group): It consists of B(boron),Al(aluminium),Ga(galium),In(indium),Th(thallium)
        2. Carbon family(14th group): It consists of C(carbon), Si(silicon), Ge(germanium),Sn(tin),Pb(lead)
        3. Nitrogen family(15th group): It consisits of N(nitrogen),P(phosphorous),As(arsenic),Sb(antimony),Bi(bismuth)
        4. Oxygen family(16th group): It consists of O(oxygen),S(sulphur),Ti(titanium),Po(plutonium)
        5. Halogen family(17th group): It consists of F(flourine),Cl(chlorine),Br(bromine),I(iodine),As(astatine)
        6. Noble family(18th group): It consists of He(Helium),Ne(neon),Ar(argon),Kr(krypton),Xe(xenon),Rn(radon)""")
        group = int(input('Which group do you want learn about(type the group number): '))
        if group == 13:
            web.open('www.britannica.com/science/boron-group-element')
        elif group == 14:
            web.open('www.encyclopedia.com/science/encyclopedias-almanacs-transcripts-and-maps/carbon-family')
        elif group == 15:
            web.open('www.encyclopedia.com/science/encyclopedias-almanacs-transcripts-and-maps/nitrogen-family#:~:text=The%20nitrogen%20family%20consists%20of,arsenic%2C%20antimony%2C%20and%20bismuth.&text=Nitrogen%20is%20a%20nonmetallic%20gas,bismuth%20is%20a%20typical%20metal.')
        elif group == 16:
            web.open('www.britannica.com/science/oxygen-group-element')
        elif group == 17:
            web.open('www.chemistryexplained.com/Ge-Hy/Halogens.html')
        elif group == 18:
            web.open('www.chemistryexplained.com/Ge-Hy/Halogens.html')
        else:
            print('Invalid input')
    elif block == 'd':
        print("""D block has elements in which valence electron enters in the d orbital.These elements are also known as
         transition elements.Zinc(Zn),Cadmium(Cd),Mercury(Hg) lie in d block but they are not actually transition elements
         coz they don't have unpaired d orbitals at any oxidation state.D block consists of 3 transition series,they are:
         1. 3d Series : It consists of Sc(scandium),Ti(titanium),V(venadium),Cr(cromium),Mn(manganeese),Fe(iron),Co(cobalt)
         ,Ni(nickel),Cu(copper),Zn(zinc).
         2.4d Series: It consists of Y(yttrium),Zr(zirconium),Nb(niobium),Mo(molbden)um),Tc(techntium),Ru(ruthenium),
         Rh(rhodium),Pd(palladium),Ag(silver),Cd(cadmium).
         3. 5d Series: It consists of La(lanthum),Hf(hofnium),Ta(tantalum),W(tungestein),Re(renium),Os(osmium),Ir(irdium),
         Pt(platinum),Ag(gold),Hg(mercury)""")

        series = input('Do you want to know more(type y for yes and n for no: ').lower()
        if series == 'y' :
            web.open('www.encyclopedia.com/science/news-wires-white-papers-and-books/transition-metals')
        elif series == 'n':
            print('Thanks for using this program...')
        else:
            print('Please check your input')

    elif block == 'f':
        print("""F block comprises of 2 periods namely lanthanoids and actinoids.f-block is also called inner transition
         metals or elements because the electron is added to the deep seated f-orbital with the increasing atomic number
          of lanthanides and actinides. Therefore, the outer orbital contains 6s or 7s-electrons and the inner energy 
          orbital contains f-electrons for lanthanides and actinides.""")
        period = input('Do u want to learn about actinoids or lanthanoids or both: ').lower()
        if period ==  "actinoids":
            web.open('www.britannica.com/science/actinoid-element')
        elif period == 'lanthanoids':
            web.open('chem.libretexts.org/Bookshelves/Inorganic_Chemistry/Supplemental_Modules_and_Websites_(Inorganic_Chemistry)/Descriptive_Chemistry/Elements_Organized_by_Block/4_f-Block_Elements/The_Lanthanides/aLanthanides%3A_Properties_and_Reactions')
        elif period == 'both':
            web.open('qsstudy.com/chemistry/define-f-block-elements')
        else:
            print('Incorrect input')
    else:
        print('Check your input and try again!!')

else:
    print('Incorrect input')
