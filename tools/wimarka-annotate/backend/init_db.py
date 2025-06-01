from database import SessionLocal, create_tables, User, Sentence
from auth import get_password_hash

def init_database():
    create_tables()
    db = SessionLocal()
    
    # Create admin user
    admin_user = db.query(User).filter(User.email == "admin@example.com").first()
    if not admin_user:
        admin_user = User(
            email="admin@example.com",
            username="admin",
            first_name="Admin",
            last_name="User",
            hashed_password=get_password_hash("admin123"),
            is_admin=True
        )
        db.add(admin_user)
        db.commit()
        print("Admin user created: admin@example.com / admin123")
    
    # Add sample sentences
    sample_sentences = [
        {
            "source_text": "The cat sat on the mat.",
            "tagalog_source_text": "Ang pusa ay umupo sa banig.",
            "machine_translation": "Le chat s'est assis sur le tapis.",
            "reference_translation": "Le chat était assis sur le tapis.",
            "source_language": "en",
            "target_language": "fr",
            "domain": "general"
        },
        {
            "source_text": "I need to go to the hospital urgently.",
            "tagalog_source_text": "Kailangan kong pumunta sa ospital nang madalian.",
            "machine_translation": "Je dois aller à l'hôpital d'urgence.",
            "reference_translation": "Je dois me rendre à l'hôpital de toute urgence.",
            "source_language": "en",
            "target_language": "fr",
            "domain": "medical"
        },
        {
            "source_text": "The contract must be signed by both parties.",
            "tagalog_source_text": "Ang kontrata ay dapat na pirmahan ng dalawang panig.",
            "machine_translation": "Le contrat doit être signé par les deux parties.",
            "reference_translation": "Le contrat doit être signé par les deux parties.",
            "source_language": "en",
            "target_language": "fr",
            "domain": "legal"
        },
        {
            "source_text": "Please restart your computer to complete the installation.",
            "tagalog_source_text": "Pakisubukan mong i-restart ang inyong computer upang makumpleto ang pag-install.",
            "machine_translation": "Veuillez redémarrer votre ordinateur pour terminer l'installation.",
            "reference_translation": "Veuillez redémarrer votre ordinateur pour compléter l'installation.",
            "source_language": "en",
            "target_language": "fr",
            "domain": "technical"
        },
        {
            "source_text": "The weather is beautiful today.",
            "tagalog_source_text": "Maganda ang panahon ngayon.",
            "machine_translation": "Le temps est beau aujourd'hui.",
            "reference_translation": "Il fait beau aujourd'hui.",
            "source_language": "en",
            "target_language": "fr",
            "domain": "general"
        },
        # Philippine Languages
        # English to Tagalog
        {
            "source_text": "Good morning! How are you today?",
            "tagalog_source_text": "Magandang umaga! Kumusta ka ngayon?",
            "machine_translation": "Magandang umaga! Kumusta ka ngayong araw?",
            "reference_translation": "Magandang umaga! Kumusta ka ngayon?",
            "source_language": "en",
            "target_language": "tagalog",
            "domain": "general"
        },
        {
            "source_text": "Please help me carry this heavy bag.",
            "tagalog_source_text": "Pakitulungan mo ako na buhatin ang mabigat na bag na ito.",
            "machine_translation": "Pakitulong sa akin na buhatin ang mabigat na bag na ito.",
            "reference_translation": "Tulungan mo naman akong buhatin ang mabigat na bag na ito.",
            "source_language": "en",
            "target_language": "tagalog",
            "domain": "general"
        },
        # English to Cebuano
        {
            "source_text": "Where is the nearest hospital?",
            "tagalog_source_text": "Saan ang pinakamalapit na ospital?",
            "machine_translation": "Asa man ang pinaka-duol nga ospital?",
            "reference_translation": "Asa man ang duol nga tambalanan?",
            "source_language": "en",
            "target_language": "cebuano",
            "domain": "medical"
        },
        {
            "source_text": "Thank you very much for your help.",
            "tagalog_source_text": "Maraming salamat sa inyong tulong.",
            "machine_translation": "Salamat kaayo sa imong tabang.",
            "reference_translation": "Daghang salamat sa imong tabang.",
            "source_language": "en",
            "target_language": "cebuano",
            "domain": "general"
        },
        # English to Ilocano
        {
            "source_text": "What time does the store open?",
            "tagalog_source_text": "Anong oras bubukas ang tindahan?",
            "machine_translation": "Ania nga oras ti panaglukat ti tienda?",
            "reference_translation": "Mano nga oras ti panaglukat ti tienda?",
            "source_language": "en",
            "target_language": "ilocano",
            "domain": "general"
        },
        # English to Hiligaynon
        {
            "source_text": "I need to buy some food for dinner.",
            "tagalog_source_text": "Kailangan kong bumili ng pagkain para sa hapunan.",
            "machine_translation": "Kinahanglan ko nga mamakal sang pagkaon para sa panihapon.",
            "reference_translation": "Dapat ako magbakal sang kaon para sa panihapon.",
            "source_language": "en",
            "target_language": "hiligaynon",
            "domain": "general"
        },
        # English to Bicolano
        {
            "source_text": "The weather is very hot today.",
            "tagalog_source_text": "Sobrang init ng panahon ngayon.",
            "machine_translation": "Maaninit na maray an panahon ngonyan.",
            "reference_translation": "Malasakit na an panahon ngonyan.",
            "source_language": "en",
            "target_language": "bicolano",
            "domain": "general"
        },
        # English to Waray
        {
            "source_text": "Can you speak English?",
            "tagalog_source_text": "Marunong ka bang mag-English?",
            "machine_translation": "Makakayani ka ba nga magsulti hin Iningles?",
            "reference_translation": "Makakabasol ka ba hin Iningles?",
            "source_language": "en",
            "target_language": "waray",
            "domain": "general"
        },
        # English to Pampangan
        {
            "source_text": "How much does this cost?",
            "tagalog_source_text": "Magkano ito?",
            "machine_translation": "Magkanu ya ini?",
            "reference_translation": "Pila ya ini?",
            "source_language": "en",
            "target_language": "pampangan",
            "domain": "general"
        },
        # English to Pangasinan
        {
            "source_text": "Please wait for me here.",
            "tagalog_source_text": "Pakihintay mo ako dito.",
            "machine_translation": "Pakiayat ak diad toy lugar.",
            "reference_translation": "Pakiuray ak diad toy lugar.",
            "source_language": "en",
            "target_language": "pangasinan",
            "domain": "general"
        }
    ]
    
    existing_sentences = db.query(Sentence).count()
    if existing_sentences == 0:
        for sentence_data in sample_sentences:
            sentence = Sentence(**sentence_data)
            db.add(sentence)
        db.commit()
        print(f"Added {len(sample_sentences)} sample sentences")
    
    db.close()
    print("Database initialization completed!")

if __name__ == "__main__":
    init_database() 