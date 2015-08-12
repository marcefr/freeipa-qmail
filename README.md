# freeipa-qmail

DISCLAIMER: This work is in still-doesn't-work-even-for-me status. Use at your own risk..

Tools and schema to use qmail-ldap against freeipa

To add the necesary schema:
   # ldapmodify -D "cn=directory manager" -W -a -x <qmail.ldif

