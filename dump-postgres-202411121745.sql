PGDMP      -            
    |            postgres    16.4    16.4 F    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                        0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    5    postgres    DATABASE     |   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE postgres;
                postgres    false                       0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    4865                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                pg_database_owner    false                       0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   pg_database_owner    false    5            �            1259    16398    address    TABLE     �   CREATE TABLE public.address (
    id_address integer NOT NULL,
    index integer,
    region character varying(100),
    country character varying(100),
    street character varying(100),
    house integer
);
    DROP TABLE public.address;
       public         heap    postgres    false    5            �            1259    16397    address_id_address_seq    SEQUENCE     �   CREATE SEQUENCE public.address_id_address_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.address_id_address_seq;
       public          postgres    false    5    217                       0    0    address_id_address_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.address_id_address_seq OWNED BY public.address.id_address;
          public          postgres    false    216            �            1259    16455    material_product    TABLE     ~   CREATE TABLE public.material_product (
    id_material_product integer NOT NULL,
    product integer,
    material integer
);
 $   DROP TABLE public.material_product;
       public         heap    postgres    false    5            �            1259    16454 (   material_product_id_material_product_seq    SEQUENCE     �   CREATE SEQUENCE public.material_product_id_material_product_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ?   DROP SEQUENCE public.material_product_id_material_product_seq;
       public          postgres    false    5    229                       0    0 (   material_product_id_material_product_seq    SEQUENCE OWNED BY     u   ALTER SEQUENCE public.material_product_id_material_product_seq OWNED BY public.material_product.id_material_product;
          public          postgres    false    228            �            1259    16448 	   materials    TABLE     �   CREATE TABLE public.materials (
    id_materials integer NOT NULL,
    type_materials character varying(100),
    marriage double precision
);
    DROP TABLE public.materials;
       public         heap    postgres    false    5            �            1259    16447    materials_id_materials_seq    SEQUENCE     �   CREATE SEQUENCE public.materials_id_materials_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.materials_id_materials_seq;
       public          postgres    false    5    227                       0    0    materials_id_materials_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.materials_id_materials_seq OWNED BY public.materials.id_materials;
          public          postgres    false    226            �            1259    16472    partner_product    TABLE     �   CREATE TABLE public.partner_product (
    id_partner_product integer NOT NULL,
    product integer,
    id_partner integer,
    count_product integer,
    date_sale date
);
 #   DROP TABLE public.partner_product;
       public         heap    postgres    false    5            �            1259    16471 &   partner_product_id_partner_product_seq    SEQUENCE     �   CREATE SEQUENCE public.partner_product_id_partner_product_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 =   DROP SEQUENCE public.partner_product_id_partner_product_seq;
       public          postgres    false    5    231                       0    0 &   partner_product_id_partner_product_seq    SEQUENCE OWNED BY     q   ALTER SEQUENCE public.partner_product_id_partner_product_seq OWNED BY public.partner_product.id_partner_product;
          public          postgres    false    230            �            1259    16412    partners    TABLE     7  CREATE TABLE public.partners (
    id_partners integer NOT NULL,
    type_partners integer,
    name_partners character varying(200),
    director character varying(200),
    email character varying(40),
    phone character varying(10),
    address integer,
    inn character varying(10),
    rating integer
);
    DROP TABLE public.partners;
       public         heap    postgres    false    5            �            1259    16411    partners_id_partners_seq    SEQUENCE     �   CREATE SEQUENCE public.partners_id_partners_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.partners_id_partners_seq;
       public          postgres    false    5    221                       0    0    partners_id_partners_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.partners_id_partners_seq OWNED BY public.partners.id_partners;
          public          postgres    false    220            �            1259    16436    products    TABLE     �   CREATE TABLE public.products (
    id_product integer NOT NULL,
    type_product integer,
    name_product character varying(200),
    article character varying(7),
    price double precision,
    size double precision,
    classs integer
);
    DROP TABLE public.products;
       public         heap    postgres    false    5            �            1259    16435    products_id_product_seq    SEQUENCE     �   CREATE SEQUENCE public.products_id_product_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.products_id_product_seq;
       public          postgres    false    225    5            	           0    0    products_id_product_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.products_id_product_seq OWNED BY public.products.id_product;
          public          postgres    false    224            �            1259    16405    type_partners    TABLE     u   CREATE TABLE public.type_partners (
    id_type_partners integer NOT NULL,
    type_partners character varying(5)
);
 !   DROP TABLE public.type_partners;
       public         heap    postgres    false    5            �            1259    16404 "   type_partners_id_type_partners_seq    SEQUENCE     �   CREATE SEQUENCE public.type_partners_id_type_partners_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public.type_partners_id_type_partners_seq;
       public          postgres    false    219    5            
           0    0 "   type_partners_id_type_partners_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE public.type_partners_id_type_partners_seq OWNED BY public.type_partners.id_type_partners;
          public          postgres    false    218            �            1259    16429    type_product    TABLE     �   CREATE TABLE public.type_product (
    id_type_product integer NOT NULL,
    type_product character varying(100),
    ratio double precision
);
     DROP TABLE public.type_product;
       public         heap    postgres    false    5            �            1259    16428     type_product_id_type_product_seq    SEQUENCE     �   CREATE SEQUENCE public.type_product_id_type_product_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.type_product_id_type_product_seq;
       public          postgres    false    5    223                       0    0     type_product_id_type_product_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.type_product_id_type_product_seq OWNED BY public.type_product.id_type_product;
          public          postgres    false    222            >           2604    16401    address id_address    DEFAULT     x   ALTER TABLE ONLY public.address ALTER COLUMN id_address SET DEFAULT nextval('public.address_id_address_seq'::regclass);
 A   ALTER TABLE public.address ALTER COLUMN id_address DROP DEFAULT;
       public          postgres    false    216    217    217            D           2604    16458 $   material_product id_material_product    DEFAULT     �   ALTER TABLE ONLY public.material_product ALTER COLUMN id_material_product SET DEFAULT nextval('public.material_product_id_material_product_seq'::regclass);
 S   ALTER TABLE public.material_product ALTER COLUMN id_material_product DROP DEFAULT;
       public          postgres    false    229    228    229            C           2604    16451    materials id_materials    DEFAULT     �   ALTER TABLE ONLY public.materials ALTER COLUMN id_materials SET DEFAULT nextval('public.materials_id_materials_seq'::regclass);
 E   ALTER TABLE public.materials ALTER COLUMN id_materials DROP DEFAULT;
       public          postgres    false    226    227    227            E           2604    16475 "   partner_product id_partner_product    DEFAULT     �   ALTER TABLE ONLY public.partner_product ALTER COLUMN id_partner_product SET DEFAULT nextval('public.partner_product_id_partner_product_seq'::regclass);
 Q   ALTER TABLE public.partner_product ALTER COLUMN id_partner_product DROP DEFAULT;
       public          postgres    false    231    230    231            @           2604    16415    partners id_partners    DEFAULT     |   ALTER TABLE ONLY public.partners ALTER COLUMN id_partners SET DEFAULT nextval('public.partners_id_partners_seq'::regclass);
 C   ALTER TABLE public.partners ALTER COLUMN id_partners DROP DEFAULT;
       public          postgres    false    221    220    221            B           2604    16439    products id_product    DEFAULT     z   ALTER TABLE ONLY public.products ALTER COLUMN id_product SET DEFAULT nextval('public.products_id_product_seq'::regclass);
 B   ALTER TABLE public.products ALTER COLUMN id_product DROP DEFAULT;
       public          postgres    false    224    225    225            ?           2604    16408    type_partners id_type_partners    DEFAULT     �   ALTER TABLE ONLY public.type_partners ALTER COLUMN id_type_partners SET DEFAULT nextval('public.type_partners_id_type_partners_seq'::regclass);
 M   ALTER TABLE public.type_partners ALTER COLUMN id_type_partners DROP DEFAULT;
       public          postgres    false    218    219    219            A           2604    16432    type_product id_type_product    DEFAULT     �   ALTER TABLE ONLY public.type_product ALTER COLUMN id_type_product SET DEFAULT nextval('public.type_product_id_type_product_seq'::regclass);
 K   ALTER TABLE public.type_product ALTER COLUMN id_type_product DROP DEFAULT;
       public          postgres    false    223    222    223            �          0    16398    address 
   TABLE DATA           T   COPY public.address (id_address, index, region, country, street, house) FROM stdin;
    public          postgres    false    217   RU       �          0    16455    material_product 
   TABLE DATA           R   COPY public.material_product (id_material_product, product, material) FROM stdin;
    public          postgres    false    229   �V       �          0    16448 	   materials 
   TABLE DATA           K   COPY public.materials (id_materials, type_materials, marriage) FROM stdin;
    public          postgres    false    227   "W       �          0    16472    partner_product 
   TABLE DATA           l   COPY public.partner_product (id_partner_product, product, id_partner, count_product, date_sale) FROM stdin;
    public          postgres    false    231   uW       �          0    16412    partners 
   TABLE DATA           {   COPY public.partners (id_partners, type_partners, name_partners, director, email, phone, address, inn, rating) FROM stdin;
    public          postgres    false    221   0X       �          0    16436    products 
   TABLE DATA           h   COPY public.products (id_product, type_product, name_product, article, price, size, classs) FROM stdin;
    public          postgres    false    225   8Z       �          0    16405    type_partners 
   TABLE DATA           H   COPY public.type_partners (id_type_partners, type_partners) FROM stdin;
    public          postgres    false    219   b[       �          0    16429    type_product 
   TABLE DATA           L   COPY public.type_product (id_type_product, type_product, ratio) FROM stdin;
    public          postgres    false    223   �[                  0    0    address_id_address_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.address_id_address_seq', 12, true);
          public          postgres    false    216                       0    0 (   material_product_id_material_product_seq    SEQUENCE SET     W   SELECT pg_catalog.setval('public.material_product_id_material_product_seq', 1, false);
          public          postgres    false    228                       0    0    materials_id_materials_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.materials_id_materials_seq', 1, false);
          public          postgres    false    226                       0    0 &   partner_product_id_partner_product_seq    SEQUENCE SET     U   SELECT pg_catalog.setval('public.partner_product_id_partner_product_seq', 1, false);
          public          postgres    false    230                       0    0    partners_id_partners_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.partners_id_partners_seq', 8, true);
          public          postgres    false    220                       0    0    products_id_product_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.products_id_product_seq', 1, false);
          public          postgres    false    224                       0    0 "   type_partners_id_type_partners_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('public.type_partners_id_type_partners_seq', 1, false);
          public          postgres    false    218                       0    0     type_product_id_type_product_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.type_product_id_type_product_seq', 1, false);
          public          postgres    false    222            G           2606    16403    address address_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.address
    ADD CONSTRAINT address_pkey PRIMARY KEY (id_address);
 >   ALTER TABLE ONLY public.address DROP CONSTRAINT address_pkey;
       public            postgres    false    217            S           2606    16460 &   material_product material_product_pkey 
   CONSTRAINT     u   ALTER TABLE ONLY public.material_product
    ADD CONSTRAINT material_product_pkey PRIMARY KEY (id_material_product);
 P   ALTER TABLE ONLY public.material_product DROP CONSTRAINT material_product_pkey;
       public            postgres    false    229            Q           2606    16453    materials materials_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.materials
    ADD CONSTRAINT materials_pkey PRIMARY KEY (id_materials);
 B   ALTER TABLE ONLY public.materials DROP CONSTRAINT materials_pkey;
       public            postgres    false    227            U           2606    16477 $   partner_product partner_product_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.partner_product
    ADD CONSTRAINT partner_product_pkey PRIMARY KEY (id_partner_product);
 N   ALTER TABLE ONLY public.partner_product DROP CONSTRAINT partner_product_pkey;
       public            postgres    false    231            K           2606    16417    partners partners_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.partners
    ADD CONSTRAINT partners_pkey PRIMARY KEY (id_partners);
 @   ALTER TABLE ONLY public.partners DROP CONSTRAINT partners_pkey;
       public            postgres    false    221            O           2606    16441    products products_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id_product);
 @   ALTER TABLE ONLY public.products DROP CONSTRAINT products_pkey;
       public            postgres    false    225            I           2606    16410     type_partners type_partners_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.type_partners
    ADD CONSTRAINT type_partners_pkey PRIMARY KEY (id_type_partners);
 J   ALTER TABLE ONLY public.type_partners DROP CONSTRAINT type_partners_pkey;
       public            postgres    false    219            M           2606    16434    type_product type_product_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.type_product
    ADD CONSTRAINT type_product_pkey PRIMARY KEY (id_type_product);
 H   ALTER TABLE ONLY public.type_product DROP CONSTRAINT type_product_pkey;
       public            postgres    false    223            Y           2606    16466 /   material_product material_product_material_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.material_product
    ADD CONSTRAINT material_product_material_fkey FOREIGN KEY (material) REFERENCES public.materials(id_materials);
 Y   ALTER TABLE ONLY public.material_product DROP CONSTRAINT material_product_material_fkey;
       public          postgres    false    4689    229    227            Z           2606    16461 .   material_product material_product_product_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.material_product
    ADD CONSTRAINT material_product_product_fkey FOREIGN KEY (product) REFERENCES public.products(id_product);
 X   ALTER TABLE ONLY public.material_product DROP CONSTRAINT material_product_product_fkey;
       public          postgres    false    4687    225    229            [           2606    16483 /   partner_product partner_product_id_partner_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.partner_product
    ADD CONSTRAINT partner_product_id_partner_fkey FOREIGN KEY (id_partner) REFERENCES public.partners(id_partners);
 Y   ALTER TABLE ONLY public.partner_product DROP CONSTRAINT partner_product_id_partner_fkey;
       public          postgres    false    221    4683    231            \           2606    16478 ,   partner_product partner_product_product_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.partner_product
    ADD CONSTRAINT partner_product_product_fkey FOREIGN KEY (product) REFERENCES public.products(id_product);
 V   ALTER TABLE ONLY public.partner_product DROP CONSTRAINT partner_product_product_fkey;
       public          postgres    false    231    4687    225            V           2606    16423    partners partners_address_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.partners
    ADD CONSTRAINT partners_address_fkey FOREIGN KEY (address) REFERENCES public.address(id_address);
 H   ALTER TABLE ONLY public.partners DROP CONSTRAINT partners_address_fkey;
       public          postgres    false    4679    217    221            W           2606    16418 $   partners partners_type_partners_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.partners
    ADD CONSTRAINT partners_type_partners_fkey FOREIGN KEY (type_partners) REFERENCES public.type_partners(id_type_partners);
 N   ALTER TABLE ONLY public.partners DROP CONSTRAINT partners_type_partners_fkey;
       public          postgres    false    221    4681    219            X           2606    16442 #   products products_type_product_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_type_product_fkey FOREIGN KEY (type_product) REFERENCES public.type_product(id_type_product);
 M   ALTER TABLE ONLY public.products DROP CONSTRAINT products_type_product_fkey;
       public          postgres    false    225    4685    223            �   �  x��RmJ�@���9�dw�����iZ�B���
Ղ�Ob�bk���퍜}Q+H��M6;�y�&ϐN��K?�S�������/��+����wn�-��ω��oy�G v��\ ������֑t�,ny�Q�Gm�sbŻ�k�>qW��6�CA|@F��tb�����=8���'���9�ٸ���z*<��`�����oB�*����Q�Rgb��O��;}^s%q���BN����C����Q/�_E��N}�^��K��x����0
fdl��8�`���c�*G�V��&�\bU�D�����K��U�ԹXg��[�2�[��D��㓟HB)BiMY�]��6�9�u��V�w+�ZiCy�&��Q�WJ�/�.�      �   &   x�3�4�4�2�B.cNc i�i$M9M9��b���� K�-      �   C   x�3估�bㅭ�^��4�3�2�0�b�@��)�1�Y�]�t�H��^���W� q�(      �   �   x�U�Ar1��Rh��/��;��uJ��jf�<�]�#��"5$G������Y�o{�o�Rx�%��_W�p&<�4,E�������%�]� 0��}���#Z*�̅�⻓*:c����i�����Ĵ�P��˞�t�����Z�$��-s�c~E�6�"��c�t�.��GU�;�      �   �  x�}�An�P���S��߳_���	����Ve�ɋ����,@�(Bb)� $qq�^a|#���(l�"%�g2���yE�?��?��]{�s���5�-oxA|��_��%/|�"t�(4�����.��]������r�{�U�pT��E��:�_�1:�&&�R����`�=�	������ť,�;�
����Mg�$�j��h���6�C��1:?
H��'��-V0�3�t�m{C�U|�h��(Vy�^u���{�}Zd�t|V�y%G9�OB��ȜĠ"��bO�&�C��ȷ�6t"���y�]ʀ6�7���:��d��J��:Rbc� �,��I�RH�)�Ɍ+Ȑ�2�ߤ��=ւ���X�N�SW�*���kU�]�`�A�� 4�Z	z޾mߋK��2I�V����J��ϋ|8J�b�ʍ�ƑQ
��t���Kx�q�=���{�ϣ����8�ַ�8��q����+��,1qE�O�iuj�&����@��      �     x�u�MN�0���S�X��}	N�ä��JlX �`�=)���$\a|#ޤ�U�h2��>�i��p_;��O�4x�k�zͯ(
Ou�1.<���O�3D��8_�|��Rɥ@އK�����RV8OP��H�?��z�{�;{Pn��q������΂SH9$��5&�l��%~����E��d�w�������lchl��Ɯ�s���g�dC�[�R׺�`&מ�
F�'r)7Ʒ��*,[G�Pѽ�-��Tu�$Dk@Ă�W!�AP������;
>4&d��~e�R?��W      �   &   x�3�0��9/̿0�0������1z\\\ ��      �   u   x�e���0�wUP�I�v7|�H �a	��ia�#V��:������|Q|��b�^�2M>�o���aG#8Q$[�/#I��.%�I%*o��_�Ï�����,�`�zo�Q�     