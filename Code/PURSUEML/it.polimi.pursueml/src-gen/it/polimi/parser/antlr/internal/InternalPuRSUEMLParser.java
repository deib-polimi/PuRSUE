package it.polimi.parser.antlr.internal;

import org.eclipse.xtext.*;
import org.eclipse.xtext.parser.*;
import org.eclipse.xtext.parser.impl.*;
import org.eclipse.emf.ecore.util.EcoreUtil;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.xtext.parser.antlr.AbstractInternalAntlrParser;
import org.eclipse.xtext.parser.antlr.XtextTokenStream;
import org.eclipse.xtext.parser.antlr.XtextTokenStream.HiddenTokens;
import org.eclipse.xtext.parser.antlr.AntlrDatatypeRuleToken;
import it.polimi.services.PuRSUEMLGrammarAccess;



import org.antlr.runtime.*;
import java.util.Stack;
import java.util.List;
import java.util.ArrayList;

@SuppressWarnings("all")
public class InternalPuRSUEMLParser extends AbstractInternalAntlrParser {
    public static final String[] tokenNames = new String[] {
        "<invalid>", "<EOR>", "<DOWN>", "<UP>", "RULE_STRING", "RULE_ID", "RULE_INT", "RULE_ML_COMMENT", "RULE_SL_COMMENT", "RULE_WS", "RULE_ANY_OTHER", "'objective:'", "'reach_objective:'", "'poi'", "'connect'", "'and'", "'distance'", "'event'", "'collaborative'", "'location'", "'duration'", "'rule'", "':'", "'('", "')'", "'before'", "'or'", "'state'", "'initially'", "'true'", "'false'", "','", "'true_if'", "'false_if'", "'stateDependency:'", "'only_if'", "'is_true'", "'is_false'", "'agent'", "'controllable'", "'mobile'", "'can_do'", "'reacts_to'", "'if'", "'then'", "'within'", "'avoid'", "'do'", "'after'"
    };
    public static final int T__19=19;
    public static final int T__15=15;
    public static final int T__16=16;
    public static final int T__17=17;
    public static final int T__18=18;
    public static final int T__11=11;
    public static final int T__12=12;
    public static final int T__13=13;
    public static final int T__14=14;
    public static final int RULE_ID=5;
    public static final int T__26=26;
    public static final int T__27=27;
    public static final int T__28=28;
    public static final int RULE_INT=6;
    public static final int T__29=29;
    public static final int T__22=22;
    public static final int RULE_ML_COMMENT=7;
    public static final int T__23=23;
    public static final int T__24=24;
    public static final int T__25=25;
    public static final int T__20=20;
    public static final int T__21=21;
    public static final int RULE_STRING=4;
    public static final int RULE_SL_COMMENT=8;
    public static final int T__37=37;
    public static final int T__38=38;
    public static final int T__39=39;
    public static final int T__33=33;
    public static final int T__34=34;
    public static final int T__35=35;
    public static final int T__36=36;
    public static final int EOF=-1;
    public static final int T__30=30;
    public static final int T__31=31;
    public static final int T__32=32;
    public static final int RULE_WS=9;
    public static final int RULE_ANY_OTHER=10;
    public static final int T__48=48;
    public static final int T__44=44;
    public static final int T__45=45;
    public static final int T__46=46;
    public static final int T__47=47;
    public static final int T__40=40;
    public static final int T__41=41;
    public static final int T__42=42;
    public static final int T__43=43;

    // delegates
    // delegators


        public InternalPuRSUEMLParser(TokenStream input) {
            this(input, new RecognizerSharedState());
        }
        public InternalPuRSUEMLParser(TokenStream input, RecognizerSharedState state) {
            super(input, state);
             
        }
        

    public String[] getTokenNames() { return InternalPuRSUEMLParser.tokenNames; }
    public String getGrammarFileName() { return "InternalPuRSUEML.g"; }



     	private PuRSUEMLGrammarAccess grammarAccess;

        public InternalPuRSUEMLParser(TokenStream input, PuRSUEMLGrammarAccess grammarAccess) {
            this(input);
            this.grammarAccess = grammarAccess;
            registerRules(grammarAccess.getGrammar());
        }

        @Override
        protected String getFirstRuleName() {
        	return "PuRSUEML";
       	}

       	@Override
       	protected PuRSUEMLGrammarAccess getGrammarAccess() {
       		return grammarAccess;
       	}




    // $ANTLR start "entryRulePuRSUEML"
    // InternalPuRSUEML.g:64:1: entryRulePuRSUEML returns [EObject current=null] : iv_rulePuRSUEML= rulePuRSUEML EOF ;
    public final EObject entryRulePuRSUEML() throws RecognitionException {
        EObject current = null;

        EObject iv_rulePuRSUEML = null;


        try {
            // InternalPuRSUEML.g:64:49: (iv_rulePuRSUEML= rulePuRSUEML EOF )
            // InternalPuRSUEML.g:65:2: iv_rulePuRSUEML= rulePuRSUEML EOF
            {
             newCompositeNode(grammarAccess.getPuRSUEMLRule()); 
            pushFollow(FOLLOW_1);
            iv_rulePuRSUEML=rulePuRSUEML();

            state._fsp--;

             current =iv_rulePuRSUEML; 
            match(input,EOF,FOLLOW_2); 

            }

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "entryRulePuRSUEML"


    // $ANTLR start "rulePuRSUEML"
    // InternalPuRSUEML.g:71:1: rulePuRSUEML returns [EObject current=null] : ( ( (lv_locations_0_0= rulePdi ) )* ( (lv_connections_1_0= ruleconnection ) )* ( (lv_events_2_0= ruleEvent ) )* ( (lv_regole_3_0= ruleRegola ) )* ( (lv_stati_4_0= ruleStato ) )* ( (lv_dipendenze_5_0= ruleStateDep ) )* ( (lv_agents_6_0= ruleAgent ) )* ( ( (lv_have_obj_7_0= 'objective:' ) ) ( (lv_objective_8_0= ruleObjective ) ) )? ( ( (lv_have_reach_obj_9_0= 'reach_objective:' ) ) ( (lv_reachobjective_10_0= ruleReachObjective ) ) )? ) ;
    public final EObject rulePuRSUEML() throws RecognitionException {
        EObject current = null;

        Token lv_have_obj_7_0=null;
        Token lv_have_reach_obj_9_0=null;
        EObject lv_locations_0_0 = null;

        EObject lv_connections_1_0 = null;

        EObject lv_events_2_0 = null;

        EObject lv_regole_3_0 = null;

        EObject lv_stati_4_0 = null;

        EObject lv_dipendenze_5_0 = null;

        EObject lv_agents_6_0 = null;

        EObject lv_objective_8_0 = null;

        EObject lv_reachobjective_10_0 = null;



        	enterRule();

        try {
            // InternalPuRSUEML.g:77:2: ( ( ( (lv_locations_0_0= rulePdi ) )* ( (lv_connections_1_0= ruleconnection ) )* ( (lv_events_2_0= ruleEvent ) )* ( (lv_regole_3_0= ruleRegola ) )* ( (lv_stati_4_0= ruleStato ) )* ( (lv_dipendenze_5_0= ruleStateDep ) )* ( (lv_agents_6_0= ruleAgent ) )* ( ( (lv_have_obj_7_0= 'objective:' ) ) ( (lv_objective_8_0= ruleObjective ) ) )? ( ( (lv_have_reach_obj_9_0= 'reach_objective:' ) ) ( (lv_reachobjective_10_0= ruleReachObjective ) ) )? ) )
            // InternalPuRSUEML.g:78:2: ( ( (lv_locations_0_0= rulePdi ) )* ( (lv_connections_1_0= ruleconnection ) )* ( (lv_events_2_0= ruleEvent ) )* ( (lv_regole_3_0= ruleRegola ) )* ( (lv_stati_4_0= ruleStato ) )* ( (lv_dipendenze_5_0= ruleStateDep ) )* ( (lv_agents_6_0= ruleAgent ) )* ( ( (lv_have_obj_7_0= 'objective:' ) ) ( (lv_objective_8_0= ruleObjective ) ) )? ( ( (lv_have_reach_obj_9_0= 'reach_objective:' ) ) ( (lv_reachobjective_10_0= ruleReachObjective ) ) )? )
            {
            // InternalPuRSUEML.g:78:2: ( ( (lv_locations_0_0= rulePdi ) )* ( (lv_connections_1_0= ruleconnection ) )* ( (lv_events_2_0= ruleEvent ) )* ( (lv_regole_3_0= ruleRegola ) )* ( (lv_stati_4_0= ruleStato ) )* ( (lv_dipendenze_5_0= ruleStateDep ) )* ( (lv_agents_6_0= ruleAgent ) )* ( ( (lv_have_obj_7_0= 'objective:' ) ) ( (lv_objective_8_0= ruleObjective ) ) )? ( ( (lv_have_reach_obj_9_0= 'reach_objective:' ) ) ( (lv_reachobjective_10_0= ruleReachObjective ) ) )? )
            // InternalPuRSUEML.g:79:3: ( (lv_locations_0_0= rulePdi ) )* ( (lv_connections_1_0= ruleconnection ) )* ( (lv_events_2_0= ruleEvent ) )* ( (lv_regole_3_0= ruleRegola ) )* ( (lv_stati_4_0= ruleStato ) )* ( (lv_dipendenze_5_0= ruleStateDep ) )* ( (lv_agents_6_0= ruleAgent ) )* ( ( (lv_have_obj_7_0= 'objective:' ) ) ( (lv_objective_8_0= ruleObjective ) ) )? ( ( (lv_have_reach_obj_9_0= 'reach_objective:' ) ) ( (lv_reachobjective_10_0= ruleReachObjective ) ) )?
            {
            // InternalPuRSUEML.g:79:3: ( (lv_locations_0_0= rulePdi ) )*
            loop1:
            do {
                int alt1=2;
                int LA1_0 = input.LA(1);

                if ( (LA1_0==13) ) {
                    alt1=1;
                }


                switch (alt1) {
            	case 1 :
            	    // InternalPuRSUEML.g:80:4: (lv_locations_0_0= rulePdi )
            	    {
            	    // InternalPuRSUEML.g:80:4: (lv_locations_0_0= rulePdi )
            	    // InternalPuRSUEML.g:81:5: lv_locations_0_0= rulePdi
            	    {

            	    					newCompositeNode(grammarAccess.getPuRSUEMLAccess().getLocationsPdiParserRuleCall_0_0());
            	    				
            	    pushFollow(FOLLOW_3);
            	    lv_locations_0_0=rulePdi();

            	    state._fsp--;


            	    					if (current==null) {
            	    						current = createModelElementForParent(grammarAccess.getPuRSUEMLRule());
            	    					}
            	    					add(
            	    						current,
            	    						"locations",
            	    						lv_locations_0_0,
            	    						"it.polimi.PuRSUEML.Pdi");
            	    					afterParserOrEnumRuleCall();
            	    				

            	    }


            	    }
            	    break;

            	default :
            	    break loop1;
                }
            } while (true);

            // InternalPuRSUEML.g:98:3: ( (lv_connections_1_0= ruleconnection ) )*
            loop2:
            do {
                int alt2=2;
                int LA2_0 = input.LA(1);

                if ( (LA2_0==14) ) {
                    alt2=1;
                }


                switch (alt2) {
            	case 1 :
            	    // InternalPuRSUEML.g:99:4: (lv_connections_1_0= ruleconnection )
            	    {
            	    // InternalPuRSUEML.g:99:4: (lv_connections_1_0= ruleconnection )
            	    // InternalPuRSUEML.g:100:5: lv_connections_1_0= ruleconnection
            	    {

            	    					newCompositeNode(grammarAccess.getPuRSUEMLAccess().getConnectionsConnectionParserRuleCall_1_0());
            	    				
            	    pushFollow(FOLLOW_4);
            	    lv_connections_1_0=ruleconnection();

            	    state._fsp--;


            	    					if (current==null) {
            	    						current = createModelElementForParent(grammarAccess.getPuRSUEMLRule());
            	    					}
            	    					add(
            	    						current,
            	    						"connections",
            	    						lv_connections_1_0,
            	    						"it.polimi.PuRSUEML.connection");
            	    					afterParserOrEnumRuleCall();
            	    				

            	    }


            	    }
            	    break;

            	default :
            	    break loop2;
                }
            } while (true);

            // InternalPuRSUEML.g:117:3: ( (lv_events_2_0= ruleEvent ) )*
            loop3:
            do {
                int alt3=2;
                int LA3_0 = input.LA(1);

                if ( (LA3_0==17) ) {
                    alt3=1;
                }


                switch (alt3) {
            	case 1 :
            	    // InternalPuRSUEML.g:118:4: (lv_events_2_0= ruleEvent )
            	    {
            	    // InternalPuRSUEML.g:118:4: (lv_events_2_0= ruleEvent )
            	    // InternalPuRSUEML.g:119:5: lv_events_2_0= ruleEvent
            	    {

            	    					newCompositeNode(grammarAccess.getPuRSUEMLAccess().getEventsEventParserRuleCall_2_0());
            	    				
            	    pushFollow(FOLLOW_5);
            	    lv_events_2_0=ruleEvent();

            	    state._fsp--;


            	    					if (current==null) {
            	    						current = createModelElementForParent(grammarAccess.getPuRSUEMLRule());
            	    					}
            	    					add(
            	    						current,
            	    						"events",
            	    						lv_events_2_0,
            	    						"it.polimi.PuRSUEML.Event");
            	    					afterParserOrEnumRuleCall();
            	    				

            	    }


            	    }
            	    break;

            	default :
            	    break loop3;
                }
            } while (true);

            // InternalPuRSUEML.g:136:3: ( (lv_regole_3_0= ruleRegola ) )*
            loop4:
            do {
                int alt4=2;
                int LA4_0 = input.LA(1);

                if ( (LA4_0==21) ) {
                    alt4=1;
                }


                switch (alt4) {
            	case 1 :
            	    // InternalPuRSUEML.g:137:4: (lv_regole_3_0= ruleRegola )
            	    {
            	    // InternalPuRSUEML.g:137:4: (lv_regole_3_0= ruleRegola )
            	    // InternalPuRSUEML.g:138:5: lv_regole_3_0= ruleRegola
            	    {

            	    					newCompositeNode(grammarAccess.getPuRSUEMLAccess().getRegoleRegolaParserRuleCall_3_0());
            	    				
            	    pushFollow(FOLLOW_6);
            	    lv_regole_3_0=ruleRegola();

            	    state._fsp--;


            	    					if (current==null) {
            	    						current = createModelElementForParent(grammarAccess.getPuRSUEMLRule());
            	    					}
            	    					add(
            	    						current,
            	    						"regole",
            	    						lv_regole_3_0,
            	    						"it.polimi.PuRSUEML.Regola");
            	    					afterParserOrEnumRuleCall();
            	    				

            	    }


            	    }
            	    break;

            	default :
            	    break loop4;
                }
            } while (true);

            // InternalPuRSUEML.g:155:3: ( (lv_stati_4_0= ruleStato ) )*
            loop5:
            do {
                int alt5=2;
                int LA5_0 = input.LA(1);

                if ( (LA5_0==27) ) {
                    alt5=1;
                }


                switch (alt5) {
            	case 1 :
            	    // InternalPuRSUEML.g:156:4: (lv_stati_4_0= ruleStato )
            	    {
            	    // InternalPuRSUEML.g:156:4: (lv_stati_4_0= ruleStato )
            	    // InternalPuRSUEML.g:157:5: lv_stati_4_0= ruleStato
            	    {

            	    					newCompositeNode(grammarAccess.getPuRSUEMLAccess().getStatiStatoParserRuleCall_4_0());
            	    				
            	    pushFollow(FOLLOW_7);
            	    lv_stati_4_0=ruleStato();

            	    state._fsp--;


            	    					if (current==null) {
            	    						current = createModelElementForParent(grammarAccess.getPuRSUEMLRule());
            	    					}
            	    					add(
            	    						current,
            	    						"stati",
            	    						lv_stati_4_0,
            	    						"it.polimi.PuRSUEML.Stato");
            	    					afterParserOrEnumRuleCall();
            	    				

            	    }


            	    }
            	    break;

            	default :
            	    break loop5;
                }
            } while (true);

            // InternalPuRSUEML.g:174:3: ( (lv_dipendenze_5_0= ruleStateDep ) )*
            loop6:
            do {
                int alt6=2;
                int LA6_0 = input.LA(1);

                if ( (LA6_0==34) ) {
                    alt6=1;
                }


                switch (alt6) {
            	case 1 :
            	    // InternalPuRSUEML.g:175:4: (lv_dipendenze_5_0= ruleStateDep )
            	    {
            	    // InternalPuRSUEML.g:175:4: (lv_dipendenze_5_0= ruleStateDep )
            	    // InternalPuRSUEML.g:176:5: lv_dipendenze_5_0= ruleStateDep
            	    {

            	    					newCompositeNode(grammarAccess.getPuRSUEMLAccess().getDipendenzeStateDepParserRuleCall_5_0());
            	    				
            	    pushFollow(FOLLOW_8);
            	    lv_dipendenze_5_0=ruleStateDep();

            	    state._fsp--;


            	    					if (current==null) {
            	    						current = createModelElementForParent(grammarAccess.getPuRSUEMLRule());
            	    					}
            	    					add(
            	    						current,
            	    						"dipendenze",
            	    						lv_dipendenze_5_0,
            	    						"it.polimi.PuRSUEML.StateDep");
            	    					afterParserOrEnumRuleCall();
            	    				

            	    }


            	    }
            	    break;

            	default :
            	    break loop6;
                }
            } while (true);

            // InternalPuRSUEML.g:193:3: ( (lv_agents_6_0= ruleAgent ) )*
            loop7:
            do {
                int alt7=2;
                int LA7_0 = input.LA(1);

                if ( (LA7_0==38) ) {
                    alt7=1;
                }


                switch (alt7) {
            	case 1 :
            	    // InternalPuRSUEML.g:194:4: (lv_agents_6_0= ruleAgent )
            	    {
            	    // InternalPuRSUEML.g:194:4: (lv_agents_6_0= ruleAgent )
            	    // InternalPuRSUEML.g:195:5: lv_agents_6_0= ruleAgent
            	    {

            	    					newCompositeNode(grammarAccess.getPuRSUEMLAccess().getAgentsAgentParserRuleCall_6_0());
            	    				
            	    pushFollow(FOLLOW_9);
            	    lv_agents_6_0=ruleAgent();

            	    state._fsp--;


            	    					if (current==null) {
            	    						current = createModelElementForParent(grammarAccess.getPuRSUEMLRule());
            	    					}
            	    					add(
            	    						current,
            	    						"agents",
            	    						lv_agents_6_0,
            	    						"it.polimi.PuRSUEML.Agent");
            	    					afterParserOrEnumRuleCall();
            	    				

            	    }


            	    }
            	    break;

            	default :
            	    break loop7;
                }
            } while (true);

            // InternalPuRSUEML.g:212:3: ( ( (lv_have_obj_7_0= 'objective:' ) ) ( (lv_objective_8_0= ruleObjective ) ) )?
            int alt8=2;
            int LA8_0 = input.LA(1);

            if ( (LA8_0==11) ) {
                alt8=1;
            }
            switch (alt8) {
                case 1 :
                    // InternalPuRSUEML.g:213:4: ( (lv_have_obj_7_0= 'objective:' ) ) ( (lv_objective_8_0= ruleObjective ) )
                    {
                    // InternalPuRSUEML.g:213:4: ( (lv_have_obj_7_0= 'objective:' ) )
                    // InternalPuRSUEML.g:214:5: (lv_have_obj_7_0= 'objective:' )
                    {
                    // InternalPuRSUEML.g:214:5: (lv_have_obj_7_0= 'objective:' )
                    // InternalPuRSUEML.g:215:6: lv_have_obj_7_0= 'objective:'
                    {
                    lv_have_obj_7_0=(Token)match(input,11,FOLLOW_10); 

                    						newLeafNode(lv_have_obj_7_0, grammarAccess.getPuRSUEMLAccess().getHave_objObjectiveKeyword_7_0_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getPuRSUEMLRule());
                    						}
                    						setWithLastConsumed(current, "have_obj", true, "objective:");
                    					

                    }


                    }

                    // InternalPuRSUEML.g:227:4: ( (lv_objective_8_0= ruleObjective ) )
                    // InternalPuRSUEML.g:228:5: (lv_objective_8_0= ruleObjective )
                    {
                    // InternalPuRSUEML.g:228:5: (lv_objective_8_0= ruleObjective )
                    // InternalPuRSUEML.g:229:6: lv_objective_8_0= ruleObjective
                    {

                    						newCompositeNode(grammarAccess.getPuRSUEMLAccess().getObjectiveObjectiveParserRuleCall_7_1_0());
                    					
                    pushFollow(FOLLOW_11);
                    lv_objective_8_0=ruleObjective();

                    state._fsp--;


                    						if (current==null) {
                    							current = createModelElementForParent(grammarAccess.getPuRSUEMLRule());
                    						}
                    						set(
                    							current,
                    							"objective",
                    							lv_objective_8_0,
                    							"it.polimi.PuRSUEML.Objective");
                    						afterParserOrEnumRuleCall();
                    					

                    }


                    }


                    }
                    break;

            }

            // InternalPuRSUEML.g:247:3: ( ( (lv_have_reach_obj_9_0= 'reach_objective:' ) ) ( (lv_reachobjective_10_0= ruleReachObjective ) ) )?
            int alt9=2;
            int LA9_0 = input.LA(1);

            if ( (LA9_0==12) ) {
                alt9=1;
            }
            switch (alt9) {
                case 1 :
                    // InternalPuRSUEML.g:248:4: ( (lv_have_reach_obj_9_0= 'reach_objective:' ) ) ( (lv_reachobjective_10_0= ruleReachObjective ) )
                    {
                    // InternalPuRSUEML.g:248:4: ( (lv_have_reach_obj_9_0= 'reach_objective:' ) )
                    // InternalPuRSUEML.g:249:5: (lv_have_reach_obj_9_0= 'reach_objective:' )
                    {
                    // InternalPuRSUEML.g:249:5: (lv_have_reach_obj_9_0= 'reach_objective:' )
                    // InternalPuRSUEML.g:250:6: lv_have_reach_obj_9_0= 'reach_objective:'
                    {
                    lv_have_reach_obj_9_0=(Token)match(input,12,FOLLOW_12); 

                    						newLeafNode(lv_have_reach_obj_9_0, grammarAccess.getPuRSUEMLAccess().getHave_reach_objReach_objectiveKeyword_8_0_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getPuRSUEMLRule());
                    						}
                    						setWithLastConsumed(current, "have_reach_obj", true, "reach_objective:");
                    					

                    }


                    }

                    // InternalPuRSUEML.g:262:4: ( (lv_reachobjective_10_0= ruleReachObjective ) )
                    // InternalPuRSUEML.g:263:5: (lv_reachobjective_10_0= ruleReachObjective )
                    {
                    // InternalPuRSUEML.g:263:5: (lv_reachobjective_10_0= ruleReachObjective )
                    // InternalPuRSUEML.g:264:6: lv_reachobjective_10_0= ruleReachObjective
                    {

                    						newCompositeNode(grammarAccess.getPuRSUEMLAccess().getReachobjectiveReachObjectiveParserRuleCall_8_1_0());
                    					
                    pushFollow(FOLLOW_2);
                    lv_reachobjective_10_0=ruleReachObjective();

                    state._fsp--;


                    						if (current==null) {
                    							current = createModelElementForParent(grammarAccess.getPuRSUEMLRule());
                    						}
                    						set(
                    							current,
                    							"reachobjective",
                    							lv_reachobjective_10_0,
                    							"it.polimi.PuRSUEML.ReachObjective");
                    						afterParserOrEnumRuleCall();
                    					

                    }


                    }


                    }
                    break;

            }


            }


            }


            	leaveRule();

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "rulePuRSUEML"


    // $ANTLR start "entryRulePdi"
    // InternalPuRSUEML.g:286:1: entryRulePdi returns [EObject current=null] : iv_rulePdi= rulePdi EOF ;
    public final EObject entryRulePdi() throws RecognitionException {
        EObject current = null;

        EObject iv_rulePdi = null;


        try {
            // InternalPuRSUEML.g:286:44: (iv_rulePdi= rulePdi EOF )
            // InternalPuRSUEML.g:287:2: iv_rulePdi= rulePdi EOF
            {
             newCompositeNode(grammarAccess.getPdiRule()); 
            pushFollow(FOLLOW_1);
            iv_rulePdi=rulePdi();

            state._fsp--;

             current =iv_rulePdi; 
            match(input,EOF,FOLLOW_2); 

            }

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "entryRulePdi"


    // $ANTLR start "rulePdi"
    // InternalPuRSUEML.g:293:1: rulePdi returns [EObject current=null] : (otherlv_0= 'poi' ( (lv_name_1_0= RULE_STRING ) ) ) ;
    public final EObject rulePdi() throws RecognitionException {
        EObject current = null;

        Token otherlv_0=null;
        Token lv_name_1_0=null;


        	enterRule();

        try {
            // InternalPuRSUEML.g:299:2: ( (otherlv_0= 'poi' ( (lv_name_1_0= RULE_STRING ) ) ) )
            // InternalPuRSUEML.g:300:2: (otherlv_0= 'poi' ( (lv_name_1_0= RULE_STRING ) ) )
            {
            // InternalPuRSUEML.g:300:2: (otherlv_0= 'poi' ( (lv_name_1_0= RULE_STRING ) ) )
            // InternalPuRSUEML.g:301:3: otherlv_0= 'poi' ( (lv_name_1_0= RULE_STRING ) )
            {
            otherlv_0=(Token)match(input,13,FOLLOW_13); 

            			newLeafNode(otherlv_0, grammarAccess.getPdiAccess().getPoiKeyword_0());
            		
            // InternalPuRSUEML.g:305:3: ( (lv_name_1_0= RULE_STRING ) )
            // InternalPuRSUEML.g:306:4: (lv_name_1_0= RULE_STRING )
            {
            // InternalPuRSUEML.g:306:4: (lv_name_1_0= RULE_STRING )
            // InternalPuRSUEML.g:307:5: lv_name_1_0= RULE_STRING
            {
            lv_name_1_0=(Token)match(input,RULE_STRING,FOLLOW_2); 

            					newLeafNode(lv_name_1_0, grammarAccess.getPdiAccess().getNameSTRINGTerminalRuleCall_1_0());
            				

            					if (current==null) {
            						current = createModelElement(grammarAccess.getPdiRule());
            					}
            					setWithLastConsumed(
            						current,
            						"name",
            						lv_name_1_0,
            						"org.eclipse.xtext.common.Terminals.STRING");
            				

            }


            }


            }


            }


            	leaveRule();

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "rulePdi"


    // $ANTLR start "entryRuleconnection"
    // InternalPuRSUEML.g:327:1: entryRuleconnection returns [EObject current=null] : iv_ruleconnection= ruleconnection EOF ;
    public final EObject entryRuleconnection() throws RecognitionException {
        EObject current = null;

        EObject iv_ruleconnection = null;


        try {
            // InternalPuRSUEML.g:327:51: (iv_ruleconnection= ruleconnection EOF )
            // InternalPuRSUEML.g:328:2: iv_ruleconnection= ruleconnection EOF
            {
             newCompositeNode(grammarAccess.getConnectionRule()); 
            pushFollow(FOLLOW_1);
            iv_ruleconnection=ruleconnection();

            state._fsp--;

             current =iv_ruleconnection; 
            match(input,EOF,FOLLOW_2); 

            }

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "entryRuleconnection"


    // $ANTLR start "ruleconnection"
    // InternalPuRSUEML.g:334:1: ruleconnection returns [EObject current=null] : (otherlv_0= 'connect' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'and' ( (otherlv_3= RULE_ID ) ) otherlv_4= 'distance' ( (lv_distance_5_0= RULE_INT ) ) ) ;
    public final EObject ruleconnection() throws RecognitionException {
        EObject current = null;

        Token otherlv_0=null;
        Token otherlv_1=null;
        Token otherlv_2=null;
        Token otherlv_3=null;
        Token otherlv_4=null;
        Token lv_distance_5_0=null;


        	enterRule();

        try {
            // InternalPuRSUEML.g:340:2: ( (otherlv_0= 'connect' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'and' ( (otherlv_3= RULE_ID ) ) otherlv_4= 'distance' ( (lv_distance_5_0= RULE_INT ) ) ) )
            // InternalPuRSUEML.g:341:2: (otherlv_0= 'connect' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'and' ( (otherlv_3= RULE_ID ) ) otherlv_4= 'distance' ( (lv_distance_5_0= RULE_INT ) ) )
            {
            // InternalPuRSUEML.g:341:2: (otherlv_0= 'connect' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'and' ( (otherlv_3= RULE_ID ) ) otherlv_4= 'distance' ( (lv_distance_5_0= RULE_INT ) ) )
            // InternalPuRSUEML.g:342:3: otherlv_0= 'connect' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'and' ( (otherlv_3= RULE_ID ) ) otherlv_4= 'distance' ( (lv_distance_5_0= RULE_INT ) )
            {
            otherlv_0=(Token)match(input,14,FOLLOW_14); 

            			newLeafNode(otherlv_0, grammarAccess.getConnectionAccess().getConnectKeyword_0());
            		
            // InternalPuRSUEML.g:346:3: ( (otherlv_1= RULE_ID ) )
            // InternalPuRSUEML.g:347:4: (otherlv_1= RULE_ID )
            {
            // InternalPuRSUEML.g:347:4: (otherlv_1= RULE_ID )
            // InternalPuRSUEML.g:348:5: otherlv_1= RULE_ID
            {

            					if (current==null) {
            						current = createModelElement(grammarAccess.getConnectionRule());
            					}
            				
            otherlv_1=(Token)match(input,RULE_ID,FOLLOW_15); 

            					newLeafNode(otherlv_1, grammarAccess.getConnectionAccess().getPdi1PdiCrossReference_1_0());
            				

            }


            }

            otherlv_2=(Token)match(input,15,FOLLOW_14); 

            			newLeafNode(otherlv_2, grammarAccess.getConnectionAccess().getAndKeyword_2());
            		
            // InternalPuRSUEML.g:363:3: ( (otherlv_3= RULE_ID ) )
            // InternalPuRSUEML.g:364:4: (otherlv_3= RULE_ID )
            {
            // InternalPuRSUEML.g:364:4: (otherlv_3= RULE_ID )
            // InternalPuRSUEML.g:365:5: otherlv_3= RULE_ID
            {

            					if (current==null) {
            						current = createModelElement(grammarAccess.getConnectionRule());
            					}
            				
            otherlv_3=(Token)match(input,RULE_ID,FOLLOW_16); 

            					newLeafNode(otherlv_3, grammarAccess.getConnectionAccess().getPdi2PdiCrossReference_3_0());
            				

            }


            }

            otherlv_4=(Token)match(input,16,FOLLOW_17); 

            			newLeafNode(otherlv_4, grammarAccess.getConnectionAccess().getDistanceKeyword_4());
            		
            // InternalPuRSUEML.g:380:3: ( (lv_distance_5_0= RULE_INT ) )
            // InternalPuRSUEML.g:381:4: (lv_distance_5_0= RULE_INT )
            {
            // InternalPuRSUEML.g:381:4: (lv_distance_5_0= RULE_INT )
            // InternalPuRSUEML.g:382:5: lv_distance_5_0= RULE_INT
            {
            lv_distance_5_0=(Token)match(input,RULE_INT,FOLLOW_2); 

            					newLeafNode(lv_distance_5_0, grammarAccess.getConnectionAccess().getDistanceINTTerminalRuleCall_5_0());
            				

            					if (current==null) {
            						current = createModelElement(grammarAccess.getConnectionRule());
            					}
            					setWithLastConsumed(
            						current,
            						"distance",
            						lv_distance_5_0,
            						"org.eclipse.xtext.common.Terminals.INT");
            				

            }


            }


            }


            }


            	leaveRule();

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "ruleconnection"


    // $ANTLR start "entryRuleEvent"
    // InternalPuRSUEML.g:402:1: entryRuleEvent returns [EObject current=null] : iv_ruleEvent= ruleEvent EOF ;
    public final EObject entryRuleEvent() throws RecognitionException {
        EObject current = null;

        EObject iv_ruleEvent = null;


        try {
            // InternalPuRSUEML.g:402:46: (iv_ruleEvent= ruleEvent EOF )
            // InternalPuRSUEML.g:403:2: iv_ruleEvent= ruleEvent EOF
            {
             newCompositeNode(grammarAccess.getEventRule()); 
            pushFollow(FOLLOW_1);
            iv_ruleEvent=ruleEvent();

            state._fsp--;

             current =iv_ruleEvent; 
            match(input,EOF,FOLLOW_2); 

            }

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "entryRuleEvent"


    // $ANTLR start "ruleEvent"
    // InternalPuRSUEML.g:409:1: ruleEvent returns [EObject current=null] : (otherlv_0= 'event' ( (lv_name_1_0= RULE_STRING ) ) ( (lv_collaborative_2_0= 'collaborative' ) )? ( ( (lv_location_specific_3_0= 'location' ) ) ( (otherlv_4= RULE_ID ) ) )? ( ( (lv_has_duration_5_0= 'duration' ) ) ( (lv_duration_6_0= RULE_INT ) ) )? ) ;
    public final EObject ruleEvent() throws RecognitionException {
        EObject current = null;

        Token otherlv_0=null;
        Token lv_name_1_0=null;
        Token lv_collaborative_2_0=null;
        Token lv_location_specific_3_0=null;
        Token otherlv_4=null;
        Token lv_has_duration_5_0=null;
        Token lv_duration_6_0=null;


        	enterRule();

        try {
            // InternalPuRSUEML.g:415:2: ( (otherlv_0= 'event' ( (lv_name_1_0= RULE_STRING ) ) ( (lv_collaborative_2_0= 'collaborative' ) )? ( ( (lv_location_specific_3_0= 'location' ) ) ( (otherlv_4= RULE_ID ) ) )? ( ( (lv_has_duration_5_0= 'duration' ) ) ( (lv_duration_6_0= RULE_INT ) ) )? ) )
            // InternalPuRSUEML.g:416:2: (otherlv_0= 'event' ( (lv_name_1_0= RULE_STRING ) ) ( (lv_collaborative_2_0= 'collaborative' ) )? ( ( (lv_location_specific_3_0= 'location' ) ) ( (otherlv_4= RULE_ID ) ) )? ( ( (lv_has_duration_5_0= 'duration' ) ) ( (lv_duration_6_0= RULE_INT ) ) )? )
            {
            // InternalPuRSUEML.g:416:2: (otherlv_0= 'event' ( (lv_name_1_0= RULE_STRING ) ) ( (lv_collaborative_2_0= 'collaborative' ) )? ( ( (lv_location_specific_3_0= 'location' ) ) ( (otherlv_4= RULE_ID ) ) )? ( ( (lv_has_duration_5_0= 'duration' ) ) ( (lv_duration_6_0= RULE_INT ) ) )? )
            // InternalPuRSUEML.g:417:3: otherlv_0= 'event' ( (lv_name_1_0= RULE_STRING ) ) ( (lv_collaborative_2_0= 'collaborative' ) )? ( ( (lv_location_specific_3_0= 'location' ) ) ( (otherlv_4= RULE_ID ) ) )? ( ( (lv_has_duration_5_0= 'duration' ) ) ( (lv_duration_6_0= RULE_INT ) ) )?
            {
            otherlv_0=(Token)match(input,17,FOLLOW_13); 

            			newLeafNode(otherlv_0, grammarAccess.getEventAccess().getEventKeyword_0());
            		
            // InternalPuRSUEML.g:421:3: ( (lv_name_1_0= RULE_STRING ) )
            // InternalPuRSUEML.g:422:4: (lv_name_1_0= RULE_STRING )
            {
            // InternalPuRSUEML.g:422:4: (lv_name_1_0= RULE_STRING )
            // InternalPuRSUEML.g:423:5: lv_name_1_0= RULE_STRING
            {
            lv_name_1_0=(Token)match(input,RULE_STRING,FOLLOW_18); 

            					newLeafNode(lv_name_1_0, grammarAccess.getEventAccess().getNameSTRINGTerminalRuleCall_1_0());
            				

            					if (current==null) {
            						current = createModelElement(grammarAccess.getEventRule());
            					}
            					setWithLastConsumed(
            						current,
            						"name",
            						lv_name_1_0,
            						"org.eclipse.xtext.common.Terminals.STRING");
            				

            }


            }

            // InternalPuRSUEML.g:439:3: ( (lv_collaborative_2_0= 'collaborative' ) )?
            int alt10=2;
            int LA10_0 = input.LA(1);

            if ( (LA10_0==18) ) {
                alt10=1;
            }
            switch (alt10) {
                case 1 :
                    // InternalPuRSUEML.g:440:4: (lv_collaborative_2_0= 'collaborative' )
                    {
                    // InternalPuRSUEML.g:440:4: (lv_collaborative_2_0= 'collaborative' )
                    // InternalPuRSUEML.g:441:5: lv_collaborative_2_0= 'collaborative'
                    {
                    lv_collaborative_2_0=(Token)match(input,18,FOLLOW_19); 

                    					newLeafNode(lv_collaborative_2_0, grammarAccess.getEventAccess().getCollaborativeCollaborativeKeyword_2_0());
                    				

                    					if (current==null) {
                    						current = createModelElement(grammarAccess.getEventRule());
                    					}
                    					setWithLastConsumed(current, "collaborative", true, "collaborative");
                    				

                    }


                    }
                    break;

            }

            // InternalPuRSUEML.g:453:3: ( ( (lv_location_specific_3_0= 'location' ) ) ( (otherlv_4= RULE_ID ) ) )?
            int alt11=2;
            int LA11_0 = input.LA(1);

            if ( (LA11_0==19) ) {
                alt11=1;
            }
            switch (alt11) {
                case 1 :
                    // InternalPuRSUEML.g:454:4: ( (lv_location_specific_3_0= 'location' ) ) ( (otherlv_4= RULE_ID ) )
                    {
                    // InternalPuRSUEML.g:454:4: ( (lv_location_specific_3_0= 'location' ) )
                    // InternalPuRSUEML.g:455:5: (lv_location_specific_3_0= 'location' )
                    {
                    // InternalPuRSUEML.g:455:5: (lv_location_specific_3_0= 'location' )
                    // InternalPuRSUEML.g:456:6: lv_location_specific_3_0= 'location'
                    {
                    lv_location_specific_3_0=(Token)match(input,19,FOLLOW_14); 

                    						newLeafNode(lv_location_specific_3_0, grammarAccess.getEventAccess().getLocation_specificLocationKeyword_3_0_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getEventRule());
                    						}
                    						setWithLastConsumed(current, "location_specific", true, "location");
                    					

                    }


                    }

                    // InternalPuRSUEML.g:468:4: ( (otherlv_4= RULE_ID ) )
                    // InternalPuRSUEML.g:469:5: (otherlv_4= RULE_ID )
                    {
                    // InternalPuRSUEML.g:469:5: (otherlv_4= RULE_ID )
                    // InternalPuRSUEML.g:470:6: otherlv_4= RULE_ID
                    {

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getEventRule());
                    						}
                    					
                    otherlv_4=(Token)match(input,RULE_ID,FOLLOW_20); 

                    						newLeafNode(otherlv_4, grammarAccess.getEventAccess().getLocationPdiCrossReference_3_1_0());
                    					

                    }


                    }


                    }
                    break;

            }

            // InternalPuRSUEML.g:482:3: ( ( (lv_has_duration_5_0= 'duration' ) ) ( (lv_duration_6_0= RULE_INT ) ) )?
            int alt12=2;
            int LA12_0 = input.LA(1);

            if ( (LA12_0==20) ) {
                alt12=1;
            }
            switch (alt12) {
                case 1 :
                    // InternalPuRSUEML.g:483:4: ( (lv_has_duration_5_0= 'duration' ) ) ( (lv_duration_6_0= RULE_INT ) )
                    {
                    // InternalPuRSUEML.g:483:4: ( (lv_has_duration_5_0= 'duration' ) )
                    // InternalPuRSUEML.g:484:5: (lv_has_duration_5_0= 'duration' )
                    {
                    // InternalPuRSUEML.g:484:5: (lv_has_duration_5_0= 'duration' )
                    // InternalPuRSUEML.g:485:6: lv_has_duration_5_0= 'duration'
                    {
                    lv_has_duration_5_0=(Token)match(input,20,FOLLOW_17); 

                    						newLeafNode(lv_has_duration_5_0, grammarAccess.getEventAccess().getHas_durationDurationKeyword_4_0_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getEventRule());
                    						}
                    						setWithLastConsumed(current, "has_duration", true, "duration");
                    					

                    }


                    }

                    // InternalPuRSUEML.g:497:4: ( (lv_duration_6_0= RULE_INT ) )
                    // InternalPuRSUEML.g:498:5: (lv_duration_6_0= RULE_INT )
                    {
                    // InternalPuRSUEML.g:498:5: (lv_duration_6_0= RULE_INT )
                    // InternalPuRSUEML.g:499:6: lv_duration_6_0= RULE_INT
                    {
                    lv_duration_6_0=(Token)match(input,RULE_INT,FOLLOW_2); 

                    						newLeafNode(lv_duration_6_0, grammarAccess.getEventAccess().getDurationINTTerminalRuleCall_4_1_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getEventRule());
                    						}
                    						setWithLastConsumed(
                    							current,
                    							"duration",
                    							lv_duration_6_0,
                    							"org.eclipse.xtext.common.Terminals.INT");
                    					

                    }


                    }


                    }
                    break;

            }


            }


            }


            	leaveRule();

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "ruleEvent"


    // $ANTLR start "entryRuleRegola"
    // InternalPuRSUEML.g:520:1: entryRuleRegola returns [EObject current=null] : iv_ruleRegola= ruleRegola EOF ;
    public final EObject entryRuleRegola() throws RecognitionException {
        EObject current = null;

        EObject iv_ruleRegola = null;


        try {
            // InternalPuRSUEML.g:520:47: (iv_ruleRegola= ruleRegola EOF )
            // InternalPuRSUEML.g:521:2: iv_ruleRegola= ruleRegola EOF
            {
             newCompositeNode(grammarAccess.getRegolaRule()); 
            pushFollow(FOLLOW_1);
            iv_ruleRegola=ruleRegola();

            state._fsp--;

             current =iv_ruleRegola; 
            match(input,EOF,FOLLOW_2); 

            }

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "entryRuleRegola"


    // $ANTLR start "ruleRegola"
    // InternalPuRSUEML.g:527:1: ruleRegola returns [EObject current=null] : (otherlv_0= 'rule' ( (lv_name_1_0= RULE_STRING ) ) otherlv_2= ':' ( ( (otherlv_3= RULE_ID ) ) | ( ( (lv_is_seq1_4_0= '(' ) ) ( (lv_first_seq_5_0= ruleSequence ) ) otherlv_6= ')' ) ) ( ( (lv_then_7_0= 'before' ) ) | ( (lv_or_8_0= 'or' ) ) ) ( ( (otherlv_9= RULE_ID ) ) | ( ( (lv_is_seq2_10_0= '(' ) ) ( (lv_second_seq_11_0= ruleSequence ) ) otherlv_12= ')' ) ) ) ;
    public final EObject ruleRegola() throws RecognitionException {
        EObject current = null;

        Token otherlv_0=null;
        Token lv_name_1_0=null;
        Token otherlv_2=null;
        Token otherlv_3=null;
        Token lv_is_seq1_4_0=null;
        Token otherlv_6=null;
        Token lv_then_7_0=null;
        Token lv_or_8_0=null;
        Token otherlv_9=null;
        Token lv_is_seq2_10_0=null;
        Token otherlv_12=null;
        EObject lv_first_seq_5_0 = null;

        EObject lv_second_seq_11_0 = null;



        	enterRule();

        try {
            // InternalPuRSUEML.g:533:2: ( (otherlv_0= 'rule' ( (lv_name_1_0= RULE_STRING ) ) otherlv_2= ':' ( ( (otherlv_3= RULE_ID ) ) | ( ( (lv_is_seq1_4_0= '(' ) ) ( (lv_first_seq_5_0= ruleSequence ) ) otherlv_6= ')' ) ) ( ( (lv_then_7_0= 'before' ) ) | ( (lv_or_8_0= 'or' ) ) ) ( ( (otherlv_9= RULE_ID ) ) | ( ( (lv_is_seq2_10_0= '(' ) ) ( (lv_second_seq_11_0= ruleSequence ) ) otherlv_12= ')' ) ) ) )
            // InternalPuRSUEML.g:534:2: (otherlv_0= 'rule' ( (lv_name_1_0= RULE_STRING ) ) otherlv_2= ':' ( ( (otherlv_3= RULE_ID ) ) | ( ( (lv_is_seq1_4_0= '(' ) ) ( (lv_first_seq_5_0= ruleSequence ) ) otherlv_6= ')' ) ) ( ( (lv_then_7_0= 'before' ) ) | ( (lv_or_8_0= 'or' ) ) ) ( ( (otherlv_9= RULE_ID ) ) | ( ( (lv_is_seq2_10_0= '(' ) ) ( (lv_second_seq_11_0= ruleSequence ) ) otherlv_12= ')' ) ) )
            {
            // InternalPuRSUEML.g:534:2: (otherlv_0= 'rule' ( (lv_name_1_0= RULE_STRING ) ) otherlv_2= ':' ( ( (otherlv_3= RULE_ID ) ) | ( ( (lv_is_seq1_4_0= '(' ) ) ( (lv_first_seq_5_0= ruleSequence ) ) otherlv_6= ')' ) ) ( ( (lv_then_7_0= 'before' ) ) | ( (lv_or_8_0= 'or' ) ) ) ( ( (otherlv_9= RULE_ID ) ) | ( ( (lv_is_seq2_10_0= '(' ) ) ( (lv_second_seq_11_0= ruleSequence ) ) otherlv_12= ')' ) ) )
            // InternalPuRSUEML.g:535:3: otherlv_0= 'rule' ( (lv_name_1_0= RULE_STRING ) ) otherlv_2= ':' ( ( (otherlv_3= RULE_ID ) ) | ( ( (lv_is_seq1_4_0= '(' ) ) ( (lv_first_seq_5_0= ruleSequence ) ) otherlv_6= ')' ) ) ( ( (lv_then_7_0= 'before' ) ) | ( (lv_or_8_0= 'or' ) ) ) ( ( (otherlv_9= RULE_ID ) ) | ( ( (lv_is_seq2_10_0= '(' ) ) ( (lv_second_seq_11_0= ruleSequence ) ) otherlv_12= ')' ) )
            {
            otherlv_0=(Token)match(input,21,FOLLOW_13); 

            			newLeafNode(otherlv_0, grammarAccess.getRegolaAccess().getRuleKeyword_0());
            		
            // InternalPuRSUEML.g:539:3: ( (lv_name_1_0= RULE_STRING ) )
            // InternalPuRSUEML.g:540:4: (lv_name_1_0= RULE_STRING )
            {
            // InternalPuRSUEML.g:540:4: (lv_name_1_0= RULE_STRING )
            // InternalPuRSUEML.g:541:5: lv_name_1_0= RULE_STRING
            {
            lv_name_1_0=(Token)match(input,RULE_STRING,FOLLOW_21); 

            					newLeafNode(lv_name_1_0, grammarAccess.getRegolaAccess().getNameSTRINGTerminalRuleCall_1_0());
            				

            					if (current==null) {
            						current = createModelElement(grammarAccess.getRegolaRule());
            					}
            					setWithLastConsumed(
            						current,
            						"name",
            						lv_name_1_0,
            						"org.eclipse.xtext.common.Terminals.STRING");
            				

            }


            }

            otherlv_2=(Token)match(input,22,FOLLOW_22); 

            			newLeafNode(otherlv_2, grammarAccess.getRegolaAccess().getColonKeyword_2());
            		
            // InternalPuRSUEML.g:561:3: ( ( (otherlv_3= RULE_ID ) ) | ( ( (lv_is_seq1_4_0= '(' ) ) ( (lv_first_seq_5_0= ruleSequence ) ) otherlv_6= ')' ) )
            int alt13=2;
            int LA13_0 = input.LA(1);

            if ( (LA13_0==RULE_ID) ) {
                alt13=1;
            }
            else if ( (LA13_0==23) ) {
                alt13=2;
            }
            else {
                NoViableAltException nvae =
                    new NoViableAltException("", 13, 0, input);

                throw nvae;
            }
            switch (alt13) {
                case 1 :
                    // InternalPuRSUEML.g:562:4: ( (otherlv_3= RULE_ID ) )
                    {
                    // InternalPuRSUEML.g:562:4: ( (otherlv_3= RULE_ID ) )
                    // InternalPuRSUEML.g:563:5: (otherlv_3= RULE_ID )
                    {
                    // InternalPuRSUEML.g:563:5: (otherlv_3= RULE_ID )
                    // InternalPuRSUEML.g:564:6: otherlv_3= RULE_ID
                    {

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getRegolaRule());
                    						}
                    					
                    otherlv_3=(Token)match(input,RULE_ID,FOLLOW_23); 

                    						newLeafNode(otherlv_3, grammarAccess.getRegolaAccess().getFirst_evEventCrossReference_3_0_0());
                    					

                    }


                    }


                    }
                    break;
                case 2 :
                    // InternalPuRSUEML.g:576:4: ( ( (lv_is_seq1_4_0= '(' ) ) ( (lv_first_seq_5_0= ruleSequence ) ) otherlv_6= ')' )
                    {
                    // InternalPuRSUEML.g:576:4: ( ( (lv_is_seq1_4_0= '(' ) ) ( (lv_first_seq_5_0= ruleSequence ) ) otherlv_6= ')' )
                    // InternalPuRSUEML.g:577:5: ( (lv_is_seq1_4_0= '(' ) ) ( (lv_first_seq_5_0= ruleSequence ) ) otherlv_6= ')'
                    {
                    // InternalPuRSUEML.g:577:5: ( (lv_is_seq1_4_0= '(' ) )
                    // InternalPuRSUEML.g:578:6: (lv_is_seq1_4_0= '(' )
                    {
                    // InternalPuRSUEML.g:578:6: (lv_is_seq1_4_0= '(' )
                    // InternalPuRSUEML.g:579:7: lv_is_seq1_4_0= '('
                    {
                    lv_is_seq1_4_0=(Token)match(input,23,FOLLOW_22); 

                    							newLeafNode(lv_is_seq1_4_0, grammarAccess.getRegolaAccess().getIs_seq1LeftParenthesisKeyword_3_1_0_0());
                    						

                    							if (current==null) {
                    								current = createModelElement(grammarAccess.getRegolaRule());
                    							}
                    							setWithLastConsumed(current, "is_seq1", true, "(");
                    						

                    }


                    }

                    // InternalPuRSUEML.g:591:5: ( (lv_first_seq_5_0= ruleSequence ) )
                    // InternalPuRSUEML.g:592:6: (lv_first_seq_5_0= ruleSequence )
                    {
                    // InternalPuRSUEML.g:592:6: (lv_first_seq_5_0= ruleSequence )
                    // InternalPuRSUEML.g:593:7: lv_first_seq_5_0= ruleSequence
                    {

                    							newCompositeNode(grammarAccess.getRegolaAccess().getFirst_seqSequenceParserRuleCall_3_1_1_0());
                    						
                    pushFollow(FOLLOW_24);
                    lv_first_seq_5_0=ruleSequence();

                    state._fsp--;


                    							if (current==null) {
                    								current = createModelElementForParent(grammarAccess.getRegolaRule());
                    							}
                    							set(
                    								current,
                    								"first_seq",
                    								lv_first_seq_5_0,
                    								"it.polimi.PuRSUEML.Sequence");
                    							afterParserOrEnumRuleCall();
                    						

                    }


                    }

                    otherlv_6=(Token)match(input,24,FOLLOW_23); 

                    					newLeafNode(otherlv_6, grammarAccess.getRegolaAccess().getRightParenthesisKeyword_3_1_2());
                    				

                    }


                    }
                    break;

            }

            // InternalPuRSUEML.g:616:3: ( ( (lv_then_7_0= 'before' ) ) | ( (lv_or_8_0= 'or' ) ) )
            int alt14=2;
            int LA14_0 = input.LA(1);

            if ( (LA14_0==25) ) {
                alt14=1;
            }
            else if ( (LA14_0==26) ) {
                alt14=2;
            }
            else {
                NoViableAltException nvae =
                    new NoViableAltException("", 14, 0, input);

                throw nvae;
            }
            switch (alt14) {
                case 1 :
                    // InternalPuRSUEML.g:617:4: ( (lv_then_7_0= 'before' ) )
                    {
                    // InternalPuRSUEML.g:617:4: ( (lv_then_7_0= 'before' ) )
                    // InternalPuRSUEML.g:618:5: (lv_then_7_0= 'before' )
                    {
                    // InternalPuRSUEML.g:618:5: (lv_then_7_0= 'before' )
                    // InternalPuRSUEML.g:619:6: lv_then_7_0= 'before'
                    {
                    lv_then_7_0=(Token)match(input,25,FOLLOW_22); 

                    						newLeafNode(lv_then_7_0, grammarAccess.getRegolaAccess().getThenBeforeKeyword_4_0_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getRegolaRule());
                    						}
                    						setWithLastConsumed(current, "then", true, "before");
                    					

                    }


                    }


                    }
                    break;
                case 2 :
                    // InternalPuRSUEML.g:632:4: ( (lv_or_8_0= 'or' ) )
                    {
                    // InternalPuRSUEML.g:632:4: ( (lv_or_8_0= 'or' ) )
                    // InternalPuRSUEML.g:633:5: (lv_or_8_0= 'or' )
                    {
                    // InternalPuRSUEML.g:633:5: (lv_or_8_0= 'or' )
                    // InternalPuRSUEML.g:634:6: lv_or_8_0= 'or'
                    {
                    lv_or_8_0=(Token)match(input,26,FOLLOW_22); 

                    						newLeafNode(lv_or_8_0, grammarAccess.getRegolaAccess().getOrOrKeyword_4_1_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getRegolaRule());
                    						}
                    						setWithLastConsumed(current, "or", true, "or");
                    					

                    }


                    }


                    }
                    break;

            }

            // InternalPuRSUEML.g:647:3: ( ( (otherlv_9= RULE_ID ) ) | ( ( (lv_is_seq2_10_0= '(' ) ) ( (lv_second_seq_11_0= ruleSequence ) ) otherlv_12= ')' ) )
            int alt15=2;
            int LA15_0 = input.LA(1);

            if ( (LA15_0==RULE_ID) ) {
                alt15=1;
            }
            else if ( (LA15_0==23) ) {
                alt15=2;
            }
            else {
                NoViableAltException nvae =
                    new NoViableAltException("", 15, 0, input);

                throw nvae;
            }
            switch (alt15) {
                case 1 :
                    // InternalPuRSUEML.g:648:4: ( (otherlv_9= RULE_ID ) )
                    {
                    // InternalPuRSUEML.g:648:4: ( (otherlv_9= RULE_ID ) )
                    // InternalPuRSUEML.g:649:5: (otherlv_9= RULE_ID )
                    {
                    // InternalPuRSUEML.g:649:5: (otherlv_9= RULE_ID )
                    // InternalPuRSUEML.g:650:6: otherlv_9= RULE_ID
                    {

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getRegolaRule());
                    						}
                    					
                    otherlv_9=(Token)match(input,RULE_ID,FOLLOW_2); 

                    						newLeafNode(otherlv_9, grammarAccess.getRegolaAccess().getSecond_evEventCrossReference_5_0_0());
                    					

                    }


                    }


                    }
                    break;
                case 2 :
                    // InternalPuRSUEML.g:662:4: ( ( (lv_is_seq2_10_0= '(' ) ) ( (lv_second_seq_11_0= ruleSequence ) ) otherlv_12= ')' )
                    {
                    // InternalPuRSUEML.g:662:4: ( ( (lv_is_seq2_10_0= '(' ) ) ( (lv_second_seq_11_0= ruleSequence ) ) otherlv_12= ')' )
                    // InternalPuRSUEML.g:663:5: ( (lv_is_seq2_10_0= '(' ) ) ( (lv_second_seq_11_0= ruleSequence ) ) otherlv_12= ')'
                    {
                    // InternalPuRSUEML.g:663:5: ( (lv_is_seq2_10_0= '(' ) )
                    // InternalPuRSUEML.g:664:6: (lv_is_seq2_10_0= '(' )
                    {
                    // InternalPuRSUEML.g:664:6: (lv_is_seq2_10_0= '(' )
                    // InternalPuRSUEML.g:665:7: lv_is_seq2_10_0= '('
                    {
                    lv_is_seq2_10_0=(Token)match(input,23,FOLLOW_22); 

                    							newLeafNode(lv_is_seq2_10_0, grammarAccess.getRegolaAccess().getIs_seq2LeftParenthesisKeyword_5_1_0_0());
                    						

                    							if (current==null) {
                    								current = createModelElement(grammarAccess.getRegolaRule());
                    							}
                    							setWithLastConsumed(current, "is_seq2", true, "(");
                    						

                    }


                    }

                    // InternalPuRSUEML.g:677:5: ( (lv_second_seq_11_0= ruleSequence ) )
                    // InternalPuRSUEML.g:678:6: (lv_second_seq_11_0= ruleSequence )
                    {
                    // InternalPuRSUEML.g:678:6: (lv_second_seq_11_0= ruleSequence )
                    // InternalPuRSUEML.g:679:7: lv_second_seq_11_0= ruleSequence
                    {

                    							newCompositeNode(grammarAccess.getRegolaAccess().getSecond_seqSequenceParserRuleCall_5_1_1_0());
                    						
                    pushFollow(FOLLOW_24);
                    lv_second_seq_11_0=ruleSequence();

                    state._fsp--;


                    							if (current==null) {
                    								current = createModelElementForParent(grammarAccess.getRegolaRule());
                    							}
                    							set(
                    								current,
                    								"second_seq",
                    								lv_second_seq_11_0,
                    								"it.polimi.PuRSUEML.Sequence");
                    							afterParserOrEnumRuleCall();
                    						

                    }


                    }

                    otherlv_12=(Token)match(input,24,FOLLOW_2); 

                    					newLeafNode(otherlv_12, grammarAccess.getRegolaAccess().getRightParenthesisKeyword_5_1_2());
                    				

                    }


                    }
                    break;

            }


            }


            }


            	leaveRule();

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "ruleRegola"


    // $ANTLR start "entryRuleSequence"
    // InternalPuRSUEML.g:706:1: entryRuleSequence returns [EObject current=null] : iv_ruleSequence= ruleSequence EOF ;
    public final EObject entryRuleSequence() throws RecognitionException {
        EObject current = null;

        EObject iv_ruleSequence = null;


        try {
            // InternalPuRSUEML.g:706:49: (iv_ruleSequence= ruleSequence EOF )
            // InternalPuRSUEML.g:707:2: iv_ruleSequence= ruleSequence EOF
            {
             newCompositeNode(grammarAccess.getSequenceRule()); 
            pushFollow(FOLLOW_1);
            iv_ruleSequence=ruleSequence();

            state._fsp--;

             current =iv_ruleSequence; 
            match(input,EOF,FOLLOW_2); 

            }

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "entryRuleSequence"


    // $ANTLR start "ruleSequence"
    // InternalPuRSUEML.g:713:1: ruleSequence returns [EObject current=null] : ( ( ( (otherlv_0= RULE_ID ) ) | ( ( (lv_is_seq1_1_0= '(' ) ) ( (lv_first_seq_2_0= ruleSequence ) ) otherlv_3= ')' ) ) ( ( (lv_then_4_0= 'before' ) ) | ( (lv_or_5_0= 'or' ) ) ) ( ( (otherlv_6= RULE_ID ) ) | ( ( (lv_is_seq2_7_0= '(' ) ) ( (lv_second_seq_8_0= ruleSequence ) ) otherlv_9= ')' ) ) ) ;
    public final EObject ruleSequence() throws RecognitionException {
        EObject current = null;

        Token otherlv_0=null;
        Token lv_is_seq1_1_0=null;
        Token otherlv_3=null;
        Token lv_then_4_0=null;
        Token lv_or_5_0=null;
        Token otherlv_6=null;
        Token lv_is_seq2_7_0=null;
        Token otherlv_9=null;
        EObject lv_first_seq_2_0 = null;

        EObject lv_second_seq_8_0 = null;



        	enterRule();

        try {
            // InternalPuRSUEML.g:719:2: ( ( ( ( (otherlv_0= RULE_ID ) ) | ( ( (lv_is_seq1_1_0= '(' ) ) ( (lv_first_seq_2_0= ruleSequence ) ) otherlv_3= ')' ) ) ( ( (lv_then_4_0= 'before' ) ) | ( (lv_or_5_0= 'or' ) ) ) ( ( (otherlv_6= RULE_ID ) ) | ( ( (lv_is_seq2_7_0= '(' ) ) ( (lv_second_seq_8_0= ruleSequence ) ) otherlv_9= ')' ) ) ) )
            // InternalPuRSUEML.g:720:2: ( ( ( (otherlv_0= RULE_ID ) ) | ( ( (lv_is_seq1_1_0= '(' ) ) ( (lv_first_seq_2_0= ruleSequence ) ) otherlv_3= ')' ) ) ( ( (lv_then_4_0= 'before' ) ) | ( (lv_or_5_0= 'or' ) ) ) ( ( (otherlv_6= RULE_ID ) ) | ( ( (lv_is_seq2_7_0= '(' ) ) ( (lv_second_seq_8_0= ruleSequence ) ) otherlv_9= ')' ) ) )
            {
            // InternalPuRSUEML.g:720:2: ( ( ( (otherlv_0= RULE_ID ) ) | ( ( (lv_is_seq1_1_0= '(' ) ) ( (lv_first_seq_2_0= ruleSequence ) ) otherlv_3= ')' ) ) ( ( (lv_then_4_0= 'before' ) ) | ( (lv_or_5_0= 'or' ) ) ) ( ( (otherlv_6= RULE_ID ) ) | ( ( (lv_is_seq2_7_0= '(' ) ) ( (lv_second_seq_8_0= ruleSequence ) ) otherlv_9= ')' ) ) )
            // InternalPuRSUEML.g:721:3: ( ( (otherlv_0= RULE_ID ) ) | ( ( (lv_is_seq1_1_0= '(' ) ) ( (lv_first_seq_2_0= ruleSequence ) ) otherlv_3= ')' ) ) ( ( (lv_then_4_0= 'before' ) ) | ( (lv_or_5_0= 'or' ) ) ) ( ( (otherlv_6= RULE_ID ) ) | ( ( (lv_is_seq2_7_0= '(' ) ) ( (lv_second_seq_8_0= ruleSequence ) ) otherlv_9= ')' ) )
            {
            // InternalPuRSUEML.g:721:3: ( ( (otherlv_0= RULE_ID ) ) | ( ( (lv_is_seq1_1_0= '(' ) ) ( (lv_first_seq_2_0= ruleSequence ) ) otherlv_3= ')' ) )
            int alt16=2;
            int LA16_0 = input.LA(1);

            if ( (LA16_0==RULE_ID) ) {
                alt16=1;
            }
            else if ( (LA16_0==23) ) {
                alt16=2;
            }
            else {
                NoViableAltException nvae =
                    new NoViableAltException("", 16, 0, input);

                throw nvae;
            }
            switch (alt16) {
                case 1 :
                    // InternalPuRSUEML.g:722:4: ( (otherlv_0= RULE_ID ) )
                    {
                    // InternalPuRSUEML.g:722:4: ( (otherlv_0= RULE_ID ) )
                    // InternalPuRSUEML.g:723:5: (otherlv_0= RULE_ID )
                    {
                    // InternalPuRSUEML.g:723:5: (otherlv_0= RULE_ID )
                    // InternalPuRSUEML.g:724:6: otherlv_0= RULE_ID
                    {

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getSequenceRule());
                    						}
                    					
                    otherlv_0=(Token)match(input,RULE_ID,FOLLOW_23); 

                    						newLeafNode(otherlv_0, grammarAccess.getSequenceAccess().getFirst_evEventCrossReference_0_0_0());
                    					

                    }


                    }


                    }
                    break;
                case 2 :
                    // InternalPuRSUEML.g:736:4: ( ( (lv_is_seq1_1_0= '(' ) ) ( (lv_first_seq_2_0= ruleSequence ) ) otherlv_3= ')' )
                    {
                    // InternalPuRSUEML.g:736:4: ( ( (lv_is_seq1_1_0= '(' ) ) ( (lv_first_seq_2_0= ruleSequence ) ) otherlv_3= ')' )
                    // InternalPuRSUEML.g:737:5: ( (lv_is_seq1_1_0= '(' ) ) ( (lv_first_seq_2_0= ruleSequence ) ) otherlv_3= ')'
                    {
                    // InternalPuRSUEML.g:737:5: ( (lv_is_seq1_1_0= '(' ) )
                    // InternalPuRSUEML.g:738:6: (lv_is_seq1_1_0= '(' )
                    {
                    // InternalPuRSUEML.g:738:6: (lv_is_seq1_1_0= '(' )
                    // InternalPuRSUEML.g:739:7: lv_is_seq1_1_0= '('
                    {
                    lv_is_seq1_1_0=(Token)match(input,23,FOLLOW_22); 

                    							newLeafNode(lv_is_seq1_1_0, grammarAccess.getSequenceAccess().getIs_seq1LeftParenthesisKeyword_0_1_0_0());
                    						

                    							if (current==null) {
                    								current = createModelElement(grammarAccess.getSequenceRule());
                    							}
                    							setWithLastConsumed(current, "is_seq1", true, "(");
                    						

                    }


                    }

                    // InternalPuRSUEML.g:751:5: ( (lv_first_seq_2_0= ruleSequence ) )
                    // InternalPuRSUEML.g:752:6: (lv_first_seq_2_0= ruleSequence )
                    {
                    // InternalPuRSUEML.g:752:6: (lv_first_seq_2_0= ruleSequence )
                    // InternalPuRSUEML.g:753:7: lv_first_seq_2_0= ruleSequence
                    {

                    							newCompositeNode(grammarAccess.getSequenceAccess().getFirst_seqSequenceParserRuleCall_0_1_1_0());
                    						
                    pushFollow(FOLLOW_24);
                    lv_first_seq_2_0=ruleSequence();

                    state._fsp--;


                    							if (current==null) {
                    								current = createModelElementForParent(grammarAccess.getSequenceRule());
                    							}
                    							set(
                    								current,
                    								"first_seq",
                    								lv_first_seq_2_0,
                    								"it.polimi.PuRSUEML.Sequence");
                    							afterParserOrEnumRuleCall();
                    						

                    }


                    }

                    otherlv_3=(Token)match(input,24,FOLLOW_23); 

                    					newLeafNode(otherlv_3, grammarAccess.getSequenceAccess().getRightParenthesisKeyword_0_1_2());
                    				

                    }


                    }
                    break;

            }

            // InternalPuRSUEML.g:776:3: ( ( (lv_then_4_0= 'before' ) ) | ( (lv_or_5_0= 'or' ) ) )
            int alt17=2;
            int LA17_0 = input.LA(1);

            if ( (LA17_0==25) ) {
                alt17=1;
            }
            else if ( (LA17_0==26) ) {
                alt17=2;
            }
            else {
                NoViableAltException nvae =
                    new NoViableAltException("", 17, 0, input);

                throw nvae;
            }
            switch (alt17) {
                case 1 :
                    // InternalPuRSUEML.g:777:4: ( (lv_then_4_0= 'before' ) )
                    {
                    // InternalPuRSUEML.g:777:4: ( (lv_then_4_0= 'before' ) )
                    // InternalPuRSUEML.g:778:5: (lv_then_4_0= 'before' )
                    {
                    // InternalPuRSUEML.g:778:5: (lv_then_4_0= 'before' )
                    // InternalPuRSUEML.g:779:6: lv_then_4_0= 'before'
                    {
                    lv_then_4_0=(Token)match(input,25,FOLLOW_22); 

                    						newLeafNode(lv_then_4_0, grammarAccess.getSequenceAccess().getThenBeforeKeyword_1_0_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getSequenceRule());
                    						}
                    						setWithLastConsumed(current, "then", true, "before");
                    					

                    }


                    }


                    }
                    break;
                case 2 :
                    // InternalPuRSUEML.g:792:4: ( (lv_or_5_0= 'or' ) )
                    {
                    // InternalPuRSUEML.g:792:4: ( (lv_or_5_0= 'or' ) )
                    // InternalPuRSUEML.g:793:5: (lv_or_5_0= 'or' )
                    {
                    // InternalPuRSUEML.g:793:5: (lv_or_5_0= 'or' )
                    // InternalPuRSUEML.g:794:6: lv_or_5_0= 'or'
                    {
                    lv_or_5_0=(Token)match(input,26,FOLLOW_22); 

                    						newLeafNode(lv_or_5_0, grammarAccess.getSequenceAccess().getOrOrKeyword_1_1_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getSequenceRule());
                    						}
                    						setWithLastConsumed(current, "or", true, "or");
                    					

                    }


                    }


                    }
                    break;

            }

            // InternalPuRSUEML.g:807:3: ( ( (otherlv_6= RULE_ID ) ) | ( ( (lv_is_seq2_7_0= '(' ) ) ( (lv_second_seq_8_0= ruleSequence ) ) otherlv_9= ')' ) )
            int alt18=2;
            int LA18_0 = input.LA(1);

            if ( (LA18_0==RULE_ID) ) {
                alt18=1;
            }
            else if ( (LA18_0==23) ) {
                alt18=2;
            }
            else {
                NoViableAltException nvae =
                    new NoViableAltException("", 18, 0, input);

                throw nvae;
            }
            switch (alt18) {
                case 1 :
                    // InternalPuRSUEML.g:808:4: ( (otherlv_6= RULE_ID ) )
                    {
                    // InternalPuRSUEML.g:808:4: ( (otherlv_6= RULE_ID ) )
                    // InternalPuRSUEML.g:809:5: (otherlv_6= RULE_ID )
                    {
                    // InternalPuRSUEML.g:809:5: (otherlv_6= RULE_ID )
                    // InternalPuRSUEML.g:810:6: otherlv_6= RULE_ID
                    {

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getSequenceRule());
                    						}
                    					
                    otherlv_6=(Token)match(input,RULE_ID,FOLLOW_2); 

                    						newLeafNode(otherlv_6, grammarAccess.getSequenceAccess().getSecond_evEventCrossReference_2_0_0());
                    					

                    }


                    }


                    }
                    break;
                case 2 :
                    // InternalPuRSUEML.g:822:4: ( ( (lv_is_seq2_7_0= '(' ) ) ( (lv_second_seq_8_0= ruleSequence ) ) otherlv_9= ')' )
                    {
                    // InternalPuRSUEML.g:822:4: ( ( (lv_is_seq2_7_0= '(' ) ) ( (lv_second_seq_8_0= ruleSequence ) ) otherlv_9= ')' )
                    // InternalPuRSUEML.g:823:5: ( (lv_is_seq2_7_0= '(' ) ) ( (lv_second_seq_8_0= ruleSequence ) ) otherlv_9= ')'
                    {
                    // InternalPuRSUEML.g:823:5: ( (lv_is_seq2_7_0= '(' ) )
                    // InternalPuRSUEML.g:824:6: (lv_is_seq2_7_0= '(' )
                    {
                    // InternalPuRSUEML.g:824:6: (lv_is_seq2_7_0= '(' )
                    // InternalPuRSUEML.g:825:7: lv_is_seq2_7_0= '('
                    {
                    lv_is_seq2_7_0=(Token)match(input,23,FOLLOW_22); 

                    							newLeafNode(lv_is_seq2_7_0, grammarAccess.getSequenceAccess().getIs_seq2LeftParenthesisKeyword_2_1_0_0());
                    						

                    							if (current==null) {
                    								current = createModelElement(grammarAccess.getSequenceRule());
                    							}
                    							setWithLastConsumed(current, "is_seq2", true, "(");
                    						

                    }


                    }

                    // InternalPuRSUEML.g:837:5: ( (lv_second_seq_8_0= ruleSequence ) )
                    // InternalPuRSUEML.g:838:6: (lv_second_seq_8_0= ruleSequence )
                    {
                    // InternalPuRSUEML.g:838:6: (lv_second_seq_8_0= ruleSequence )
                    // InternalPuRSUEML.g:839:7: lv_second_seq_8_0= ruleSequence
                    {

                    							newCompositeNode(grammarAccess.getSequenceAccess().getSecond_seqSequenceParserRuleCall_2_1_1_0());
                    						
                    pushFollow(FOLLOW_24);
                    lv_second_seq_8_0=ruleSequence();

                    state._fsp--;


                    							if (current==null) {
                    								current = createModelElementForParent(grammarAccess.getSequenceRule());
                    							}
                    							set(
                    								current,
                    								"second_seq",
                    								lv_second_seq_8_0,
                    								"it.polimi.PuRSUEML.Sequence");
                    							afterParserOrEnumRuleCall();
                    						

                    }


                    }

                    otherlv_9=(Token)match(input,24,FOLLOW_2); 

                    					newLeafNode(otherlv_9, grammarAccess.getSequenceAccess().getRightParenthesisKeyword_2_1_2());
                    				

                    }


                    }
                    break;

            }


            }


            }


            	leaveRule();

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "ruleSequence"


    // $ANTLR start "entryRuleStato"
    // InternalPuRSUEML.g:866:1: entryRuleStato returns [EObject current=null] : iv_ruleStato= ruleStato EOF ;
    public final EObject entryRuleStato() throws RecognitionException {
        EObject current = null;

        EObject iv_ruleStato = null;


        try {
            // InternalPuRSUEML.g:866:46: (iv_ruleStato= ruleStato EOF )
            // InternalPuRSUEML.g:867:2: iv_ruleStato= ruleStato EOF
            {
             newCompositeNode(grammarAccess.getStatoRule()); 
            pushFollow(FOLLOW_1);
            iv_ruleStato=ruleStato();

            state._fsp--;

             current =iv_ruleStato; 
            match(input,EOF,FOLLOW_2); 

            }

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "entryRuleStato"


    // $ANTLR start "ruleStato"
    // InternalPuRSUEML.g:873:1: ruleStato returns [EObject current=null] : (otherlv_0= 'state' ( (lv_name_1_0= RULE_STRING ) ) otherlv_2= ':' otherlv_3= 'initially' ( ( (lv_tr_4_0= 'true' ) ) | ( (lv_fl_5_0= 'false' ) ) ) otherlv_6= ',' otherlv_7= 'true_if' ( ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )* ) otherlv_11= 'false_if' ( ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )* ) ) ;
    public final EObject ruleStato() throws RecognitionException {
        EObject current = null;

        Token otherlv_0=null;
        Token lv_name_1_0=null;
        Token otherlv_2=null;
        Token otherlv_3=null;
        Token lv_tr_4_0=null;
        Token lv_fl_5_0=null;
        Token otherlv_6=null;
        Token otherlv_7=null;
        Token otherlv_8=null;
        Token otherlv_9=null;
        Token otherlv_10=null;
        Token otherlv_11=null;
        Token otherlv_12=null;
        Token otherlv_13=null;
        Token otherlv_14=null;


        	enterRule();

        try {
            // InternalPuRSUEML.g:879:2: ( (otherlv_0= 'state' ( (lv_name_1_0= RULE_STRING ) ) otherlv_2= ':' otherlv_3= 'initially' ( ( (lv_tr_4_0= 'true' ) ) | ( (lv_fl_5_0= 'false' ) ) ) otherlv_6= ',' otherlv_7= 'true_if' ( ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )* ) otherlv_11= 'false_if' ( ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )* ) ) )
            // InternalPuRSUEML.g:880:2: (otherlv_0= 'state' ( (lv_name_1_0= RULE_STRING ) ) otherlv_2= ':' otherlv_3= 'initially' ( ( (lv_tr_4_0= 'true' ) ) | ( (lv_fl_5_0= 'false' ) ) ) otherlv_6= ',' otherlv_7= 'true_if' ( ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )* ) otherlv_11= 'false_if' ( ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )* ) )
            {
            // InternalPuRSUEML.g:880:2: (otherlv_0= 'state' ( (lv_name_1_0= RULE_STRING ) ) otherlv_2= ':' otherlv_3= 'initially' ( ( (lv_tr_4_0= 'true' ) ) | ( (lv_fl_5_0= 'false' ) ) ) otherlv_6= ',' otherlv_7= 'true_if' ( ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )* ) otherlv_11= 'false_if' ( ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )* ) )
            // InternalPuRSUEML.g:881:3: otherlv_0= 'state' ( (lv_name_1_0= RULE_STRING ) ) otherlv_2= ':' otherlv_3= 'initially' ( ( (lv_tr_4_0= 'true' ) ) | ( (lv_fl_5_0= 'false' ) ) ) otherlv_6= ',' otherlv_7= 'true_if' ( ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )* ) otherlv_11= 'false_if' ( ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )* )
            {
            otherlv_0=(Token)match(input,27,FOLLOW_13); 

            			newLeafNode(otherlv_0, grammarAccess.getStatoAccess().getStateKeyword_0());
            		
            // InternalPuRSUEML.g:885:3: ( (lv_name_1_0= RULE_STRING ) )
            // InternalPuRSUEML.g:886:4: (lv_name_1_0= RULE_STRING )
            {
            // InternalPuRSUEML.g:886:4: (lv_name_1_0= RULE_STRING )
            // InternalPuRSUEML.g:887:5: lv_name_1_0= RULE_STRING
            {
            lv_name_1_0=(Token)match(input,RULE_STRING,FOLLOW_21); 

            					newLeafNode(lv_name_1_0, grammarAccess.getStatoAccess().getNameSTRINGTerminalRuleCall_1_0());
            				

            					if (current==null) {
            						current = createModelElement(grammarAccess.getStatoRule());
            					}
            					setWithLastConsumed(
            						current,
            						"name",
            						lv_name_1_0,
            						"org.eclipse.xtext.common.Terminals.STRING");
            				

            }


            }

            otherlv_2=(Token)match(input,22,FOLLOW_25); 

            			newLeafNode(otherlv_2, grammarAccess.getStatoAccess().getColonKeyword_2());
            		
            otherlv_3=(Token)match(input,28,FOLLOW_26); 

            			newLeafNode(otherlv_3, grammarAccess.getStatoAccess().getInitiallyKeyword_3());
            		
            // InternalPuRSUEML.g:911:3: ( ( (lv_tr_4_0= 'true' ) ) | ( (lv_fl_5_0= 'false' ) ) )
            int alt19=2;
            int LA19_0 = input.LA(1);

            if ( (LA19_0==29) ) {
                alt19=1;
            }
            else if ( (LA19_0==30) ) {
                alt19=2;
            }
            else {
                NoViableAltException nvae =
                    new NoViableAltException("", 19, 0, input);

                throw nvae;
            }
            switch (alt19) {
                case 1 :
                    // InternalPuRSUEML.g:912:4: ( (lv_tr_4_0= 'true' ) )
                    {
                    // InternalPuRSUEML.g:912:4: ( (lv_tr_4_0= 'true' ) )
                    // InternalPuRSUEML.g:913:5: (lv_tr_4_0= 'true' )
                    {
                    // InternalPuRSUEML.g:913:5: (lv_tr_4_0= 'true' )
                    // InternalPuRSUEML.g:914:6: lv_tr_4_0= 'true'
                    {
                    lv_tr_4_0=(Token)match(input,29,FOLLOW_27); 

                    						newLeafNode(lv_tr_4_0, grammarAccess.getStatoAccess().getTrTrueKeyword_4_0_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getStatoRule());
                    						}
                    						setWithLastConsumed(current, "tr", true, "true");
                    					

                    }


                    }


                    }
                    break;
                case 2 :
                    // InternalPuRSUEML.g:927:4: ( (lv_fl_5_0= 'false' ) )
                    {
                    // InternalPuRSUEML.g:927:4: ( (lv_fl_5_0= 'false' ) )
                    // InternalPuRSUEML.g:928:5: (lv_fl_5_0= 'false' )
                    {
                    // InternalPuRSUEML.g:928:5: (lv_fl_5_0= 'false' )
                    // InternalPuRSUEML.g:929:6: lv_fl_5_0= 'false'
                    {
                    lv_fl_5_0=(Token)match(input,30,FOLLOW_27); 

                    						newLeafNode(lv_fl_5_0, grammarAccess.getStatoAccess().getFlFalseKeyword_4_1_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getStatoRule());
                    						}
                    						setWithLastConsumed(current, "fl", true, "false");
                    					

                    }


                    }


                    }
                    break;

            }

            otherlv_6=(Token)match(input,31,FOLLOW_28); 

            			newLeafNode(otherlv_6, grammarAccess.getStatoAccess().getCommaKeyword_5());
            		
            otherlv_7=(Token)match(input,32,FOLLOW_14); 

            			newLeafNode(otherlv_7, grammarAccess.getStatoAccess().getTrue_ifKeyword_6());
            		
            // InternalPuRSUEML.g:950:3: ( ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )* )
            // InternalPuRSUEML.g:951:4: ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )*
            {
            // InternalPuRSUEML.g:951:4: ( (otherlv_8= RULE_ID ) )
            // InternalPuRSUEML.g:952:5: (otherlv_8= RULE_ID )
            {
            // InternalPuRSUEML.g:952:5: (otherlv_8= RULE_ID )
            // InternalPuRSUEML.g:953:6: otherlv_8= RULE_ID
            {

            						if (current==null) {
            							current = createModelElement(grammarAccess.getStatoRule());
            						}
            					
            otherlv_8=(Token)match(input,RULE_ID,FOLLOW_29); 

            						newLeafNode(otherlv_8, grammarAccess.getStatoAccess().getTrue_eventsEventCrossReference_7_0_0());
            					

            }


            }

            // InternalPuRSUEML.g:964:4: (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )*
            loop20:
            do {
                int alt20=2;
                int LA20_0 = input.LA(1);

                if ( (LA20_0==31) ) {
                    alt20=1;
                }


                switch (alt20) {
            	case 1 :
            	    // InternalPuRSUEML.g:965:5: otherlv_9= ',' ( (otherlv_10= RULE_ID ) )
            	    {
            	    otherlv_9=(Token)match(input,31,FOLLOW_14); 

            	    					newLeafNode(otherlv_9, grammarAccess.getStatoAccess().getCommaKeyword_7_1_0());
            	    				
            	    // InternalPuRSUEML.g:969:5: ( (otherlv_10= RULE_ID ) )
            	    // InternalPuRSUEML.g:970:6: (otherlv_10= RULE_ID )
            	    {
            	    // InternalPuRSUEML.g:970:6: (otherlv_10= RULE_ID )
            	    // InternalPuRSUEML.g:971:7: otherlv_10= RULE_ID
            	    {

            	    							if (current==null) {
            	    								current = createModelElement(grammarAccess.getStatoRule());
            	    							}
            	    						
            	    otherlv_10=(Token)match(input,RULE_ID,FOLLOW_29); 

            	    							newLeafNode(otherlv_10, grammarAccess.getStatoAccess().getTrue_eventsEventCrossReference_7_1_1_0());
            	    						

            	    }


            	    }


            	    }
            	    break;

            	default :
            	    break loop20;
                }
            } while (true);


            }

            otherlv_11=(Token)match(input,33,FOLLOW_14); 

            			newLeafNode(otherlv_11, grammarAccess.getStatoAccess().getFalse_ifKeyword_8());
            		
            // InternalPuRSUEML.g:988:3: ( ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )* )
            // InternalPuRSUEML.g:989:4: ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )*
            {
            // InternalPuRSUEML.g:989:4: ( (otherlv_12= RULE_ID ) )
            // InternalPuRSUEML.g:990:5: (otherlv_12= RULE_ID )
            {
            // InternalPuRSUEML.g:990:5: (otherlv_12= RULE_ID )
            // InternalPuRSUEML.g:991:6: otherlv_12= RULE_ID
            {

            						if (current==null) {
            							current = createModelElement(grammarAccess.getStatoRule());
            						}
            					
            otherlv_12=(Token)match(input,RULE_ID,FOLLOW_30); 

            						newLeafNode(otherlv_12, grammarAccess.getStatoAccess().getFalse_eventsEventCrossReference_9_0_0());
            					

            }


            }

            // InternalPuRSUEML.g:1002:4: (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )*
            loop21:
            do {
                int alt21=2;
                int LA21_0 = input.LA(1);

                if ( (LA21_0==31) ) {
                    alt21=1;
                }


                switch (alt21) {
            	case 1 :
            	    // InternalPuRSUEML.g:1003:5: otherlv_13= ',' ( (otherlv_14= RULE_ID ) )
            	    {
            	    otherlv_13=(Token)match(input,31,FOLLOW_14); 

            	    					newLeafNode(otherlv_13, grammarAccess.getStatoAccess().getCommaKeyword_9_1_0());
            	    				
            	    // InternalPuRSUEML.g:1007:5: ( (otherlv_14= RULE_ID ) )
            	    // InternalPuRSUEML.g:1008:6: (otherlv_14= RULE_ID )
            	    {
            	    // InternalPuRSUEML.g:1008:6: (otherlv_14= RULE_ID )
            	    // InternalPuRSUEML.g:1009:7: otherlv_14= RULE_ID
            	    {

            	    							if (current==null) {
            	    								current = createModelElement(grammarAccess.getStatoRule());
            	    							}
            	    						
            	    otherlv_14=(Token)match(input,RULE_ID,FOLLOW_30); 

            	    							newLeafNode(otherlv_14, grammarAccess.getStatoAccess().getFalse_eventsEventCrossReference_9_1_1_0());
            	    						

            	    }


            	    }


            	    }
            	    break;

            	default :
            	    break loop21;
                }
            } while (true);


            }


            }


            }


            	leaveRule();

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "ruleStato"


    // $ANTLR start "entryRuleStateDep"
    // InternalPuRSUEML.g:1026:1: entryRuleStateDep returns [EObject current=null] : iv_ruleStateDep= ruleStateDep EOF ;
    public final EObject entryRuleStateDep() throws RecognitionException {
        EObject current = null;

        EObject iv_ruleStateDep = null;


        try {
            // InternalPuRSUEML.g:1026:49: (iv_ruleStateDep= ruleStateDep EOF )
            // InternalPuRSUEML.g:1027:2: iv_ruleStateDep= ruleStateDep EOF
            {
             newCompositeNode(grammarAccess.getStateDepRule()); 
            pushFollow(FOLLOW_1);
            iv_ruleStateDep=ruleStateDep();

            state._fsp--;

             current =iv_ruleStateDep; 
            match(input,EOF,FOLLOW_2); 

            }

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "entryRuleStateDep"


    // $ANTLR start "ruleStateDep"
    // InternalPuRSUEML.g:1033:1: ruleStateDep returns [EObject current=null] : (otherlv_0= 'stateDependency:' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'only_if' ( ( ( (otherlv_3= RULE_ID ) ) ( (lv_tr_4_0= 'is_true' ) ) ) | ( ( (otherlv_5= RULE_ID ) ) ( (lv_fl_6_0= 'is_false' ) ) ) ) ) ;
    public final EObject ruleStateDep() throws RecognitionException {
        EObject current = null;

        Token otherlv_0=null;
        Token otherlv_1=null;
        Token otherlv_2=null;
        Token otherlv_3=null;
        Token lv_tr_4_0=null;
        Token otherlv_5=null;
        Token lv_fl_6_0=null;


        	enterRule();

        try {
            // InternalPuRSUEML.g:1039:2: ( (otherlv_0= 'stateDependency:' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'only_if' ( ( ( (otherlv_3= RULE_ID ) ) ( (lv_tr_4_0= 'is_true' ) ) ) | ( ( (otherlv_5= RULE_ID ) ) ( (lv_fl_6_0= 'is_false' ) ) ) ) ) )
            // InternalPuRSUEML.g:1040:2: (otherlv_0= 'stateDependency:' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'only_if' ( ( ( (otherlv_3= RULE_ID ) ) ( (lv_tr_4_0= 'is_true' ) ) ) | ( ( (otherlv_5= RULE_ID ) ) ( (lv_fl_6_0= 'is_false' ) ) ) ) )
            {
            // InternalPuRSUEML.g:1040:2: (otherlv_0= 'stateDependency:' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'only_if' ( ( ( (otherlv_3= RULE_ID ) ) ( (lv_tr_4_0= 'is_true' ) ) ) | ( ( (otherlv_5= RULE_ID ) ) ( (lv_fl_6_0= 'is_false' ) ) ) ) )
            // InternalPuRSUEML.g:1041:3: otherlv_0= 'stateDependency:' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'only_if' ( ( ( (otherlv_3= RULE_ID ) ) ( (lv_tr_4_0= 'is_true' ) ) ) | ( ( (otherlv_5= RULE_ID ) ) ( (lv_fl_6_0= 'is_false' ) ) ) )
            {
            otherlv_0=(Token)match(input,34,FOLLOW_14); 

            			newLeafNode(otherlv_0, grammarAccess.getStateDepAccess().getStateDependencyKeyword_0());
            		
            // InternalPuRSUEML.g:1045:3: ( (otherlv_1= RULE_ID ) )
            // InternalPuRSUEML.g:1046:4: (otherlv_1= RULE_ID )
            {
            // InternalPuRSUEML.g:1046:4: (otherlv_1= RULE_ID )
            // InternalPuRSUEML.g:1047:5: otherlv_1= RULE_ID
            {

            					if (current==null) {
            						current = createModelElement(grammarAccess.getStateDepRule());
            					}
            				
            otherlv_1=(Token)match(input,RULE_ID,FOLLOW_31); 

            					newLeafNode(otherlv_1, grammarAccess.getStateDepAccess().getEventoEventCrossReference_1_0());
            				

            }


            }

            otherlv_2=(Token)match(input,35,FOLLOW_14); 

            			newLeafNode(otherlv_2, grammarAccess.getStateDepAccess().getOnly_ifKeyword_2());
            		
            // InternalPuRSUEML.g:1062:3: ( ( ( (otherlv_3= RULE_ID ) ) ( (lv_tr_4_0= 'is_true' ) ) ) | ( ( (otherlv_5= RULE_ID ) ) ( (lv_fl_6_0= 'is_false' ) ) ) )
            int alt22=2;
            int LA22_0 = input.LA(1);

            if ( (LA22_0==RULE_ID) ) {
                int LA22_1 = input.LA(2);

                if ( (LA22_1==36) ) {
                    alt22=1;
                }
                else if ( (LA22_1==37) ) {
                    alt22=2;
                }
                else {
                    NoViableAltException nvae =
                        new NoViableAltException("", 22, 1, input);

                    throw nvae;
                }
            }
            else {
                NoViableAltException nvae =
                    new NoViableAltException("", 22, 0, input);

                throw nvae;
            }
            switch (alt22) {
                case 1 :
                    // InternalPuRSUEML.g:1063:4: ( ( (otherlv_3= RULE_ID ) ) ( (lv_tr_4_0= 'is_true' ) ) )
                    {
                    // InternalPuRSUEML.g:1063:4: ( ( (otherlv_3= RULE_ID ) ) ( (lv_tr_4_0= 'is_true' ) ) )
                    // InternalPuRSUEML.g:1064:5: ( (otherlv_3= RULE_ID ) ) ( (lv_tr_4_0= 'is_true' ) )
                    {
                    // InternalPuRSUEML.g:1064:5: ( (otherlv_3= RULE_ID ) )
                    // InternalPuRSUEML.g:1065:6: (otherlv_3= RULE_ID )
                    {
                    // InternalPuRSUEML.g:1065:6: (otherlv_3= RULE_ID )
                    // InternalPuRSUEML.g:1066:7: otherlv_3= RULE_ID
                    {

                    							if (current==null) {
                    								current = createModelElement(grammarAccess.getStateDepRule());
                    							}
                    						
                    otherlv_3=(Token)match(input,RULE_ID,FOLLOW_32); 

                    							newLeafNode(otherlv_3, grammarAccess.getStateDepAccess().getStatStatoCrossReference_3_0_0_0());
                    						

                    }


                    }

                    // InternalPuRSUEML.g:1077:5: ( (lv_tr_4_0= 'is_true' ) )
                    // InternalPuRSUEML.g:1078:6: (lv_tr_4_0= 'is_true' )
                    {
                    // InternalPuRSUEML.g:1078:6: (lv_tr_4_0= 'is_true' )
                    // InternalPuRSUEML.g:1079:7: lv_tr_4_0= 'is_true'
                    {
                    lv_tr_4_0=(Token)match(input,36,FOLLOW_2); 

                    							newLeafNode(lv_tr_4_0, grammarAccess.getStateDepAccess().getTrIs_trueKeyword_3_0_1_0());
                    						

                    							if (current==null) {
                    								current = createModelElement(grammarAccess.getStateDepRule());
                    							}
                    							setWithLastConsumed(current, "tr", true, "is_true");
                    						

                    }


                    }


                    }


                    }
                    break;
                case 2 :
                    // InternalPuRSUEML.g:1093:4: ( ( (otherlv_5= RULE_ID ) ) ( (lv_fl_6_0= 'is_false' ) ) )
                    {
                    // InternalPuRSUEML.g:1093:4: ( ( (otherlv_5= RULE_ID ) ) ( (lv_fl_6_0= 'is_false' ) ) )
                    // InternalPuRSUEML.g:1094:5: ( (otherlv_5= RULE_ID ) ) ( (lv_fl_6_0= 'is_false' ) )
                    {
                    // InternalPuRSUEML.g:1094:5: ( (otherlv_5= RULE_ID ) )
                    // InternalPuRSUEML.g:1095:6: (otherlv_5= RULE_ID )
                    {
                    // InternalPuRSUEML.g:1095:6: (otherlv_5= RULE_ID )
                    // InternalPuRSUEML.g:1096:7: otherlv_5= RULE_ID
                    {

                    							if (current==null) {
                    								current = createModelElement(grammarAccess.getStateDepRule());
                    							}
                    						
                    otherlv_5=(Token)match(input,RULE_ID,FOLLOW_33); 

                    							newLeafNode(otherlv_5, grammarAccess.getStateDepAccess().getStatStatoCrossReference_3_1_0_0());
                    						

                    }


                    }

                    // InternalPuRSUEML.g:1107:5: ( (lv_fl_6_0= 'is_false' ) )
                    // InternalPuRSUEML.g:1108:6: (lv_fl_6_0= 'is_false' )
                    {
                    // InternalPuRSUEML.g:1108:6: (lv_fl_6_0= 'is_false' )
                    // InternalPuRSUEML.g:1109:7: lv_fl_6_0= 'is_false'
                    {
                    lv_fl_6_0=(Token)match(input,37,FOLLOW_2); 

                    							newLeafNode(lv_fl_6_0, grammarAccess.getStateDepAccess().getFlIs_falseKeyword_3_1_1_0());
                    						

                    							if (current==null) {
                    								current = createModelElement(grammarAccess.getStateDepRule());
                    							}
                    							setWithLastConsumed(current, "fl", true, "is_false");
                    						

                    }


                    }


                    }


                    }
                    break;

            }


            }


            }


            	leaveRule();

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "ruleStateDep"


    // $ANTLR start "entryRuleAgent"
    // InternalPuRSUEML.g:1127:1: entryRuleAgent returns [EObject current=null] : iv_ruleAgent= ruleAgent EOF ;
    public final EObject entryRuleAgent() throws RecognitionException {
        EObject current = null;

        EObject iv_ruleAgent = null;


        try {
            // InternalPuRSUEML.g:1127:46: (iv_ruleAgent= ruleAgent EOF )
            // InternalPuRSUEML.g:1128:2: iv_ruleAgent= ruleAgent EOF
            {
             newCompositeNode(grammarAccess.getAgentRule()); 
            pushFollow(FOLLOW_1);
            iv_ruleAgent=ruleAgent();

            state._fsp--;

             current =iv_ruleAgent; 
            match(input,EOF,FOLLOW_2); 

            }

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "entryRuleAgent"


    // $ANTLR start "ruleAgent"
    // InternalPuRSUEML.g:1134:1: ruleAgent returns [EObject current=null] : (otherlv_0= 'agent' ( (lv_name_1_0= RULE_STRING ) ) ( (lv_controllable_2_0= 'controllable' ) )? ( ( (lv_mobile_3_0= 'mobile' ) ) ( (lv_speed_4_0= RULE_INT ) ) )? (otherlv_5= 'location' ( (otherlv_6= RULE_ID ) ) ) (otherlv_7= 'can_do' ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )* )? (otherlv_11= 'reacts_to' ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )* )? ) ;
    public final EObject ruleAgent() throws RecognitionException {
        EObject current = null;

        Token otherlv_0=null;
        Token lv_name_1_0=null;
        Token lv_controllable_2_0=null;
        Token lv_mobile_3_0=null;
        Token lv_speed_4_0=null;
        Token otherlv_5=null;
        Token otherlv_6=null;
        Token otherlv_7=null;
        Token otherlv_8=null;
        Token otherlv_9=null;
        Token otherlv_10=null;
        Token otherlv_11=null;
        Token otherlv_12=null;
        Token otherlv_13=null;
        Token otherlv_14=null;


        	enterRule();

        try {
            // InternalPuRSUEML.g:1140:2: ( (otherlv_0= 'agent' ( (lv_name_1_0= RULE_STRING ) ) ( (lv_controllable_2_0= 'controllable' ) )? ( ( (lv_mobile_3_0= 'mobile' ) ) ( (lv_speed_4_0= RULE_INT ) ) )? (otherlv_5= 'location' ( (otherlv_6= RULE_ID ) ) ) (otherlv_7= 'can_do' ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )* )? (otherlv_11= 'reacts_to' ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )* )? ) )
            // InternalPuRSUEML.g:1141:2: (otherlv_0= 'agent' ( (lv_name_1_0= RULE_STRING ) ) ( (lv_controllable_2_0= 'controllable' ) )? ( ( (lv_mobile_3_0= 'mobile' ) ) ( (lv_speed_4_0= RULE_INT ) ) )? (otherlv_5= 'location' ( (otherlv_6= RULE_ID ) ) ) (otherlv_7= 'can_do' ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )* )? (otherlv_11= 'reacts_to' ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )* )? )
            {
            // InternalPuRSUEML.g:1141:2: (otherlv_0= 'agent' ( (lv_name_1_0= RULE_STRING ) ) ( (lv_controllable_2_0= 'controllable' ) )? ( ( (lv_mobile_3_0= 'mobile' ) ) ( (lv_speed_4_0= RULE_INT ) ) )? (otherlv_5= 'location' ( (otherlv_6= RULE_ID ) ) ) (otherlv_7= 'can_do' ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )* )? (otherlv_11= 'reacts_to' ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )* )? )
            // InternalPuRSUEML.g:1142:3: otherlv_0= 'agent' ( (lv_name_1_0= RULE_STRING ) ) ( (lv_controllable_2_0= 'controllable' ) )? ( ( (lv_mobile_3_0= 'mobile' ) ) ( (lv_speed_4_0= RULE_INT ) ) )? (otherlv_5= 'location' ( (otherlv_6= RULE_ID ) ) ) (otherlv_7= 'can_do' ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )* )? (otherlv_11= 'reacts_to' ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )* )?
            {
            otherlv_0=(Token)match(input,38,FOLLOW_13); 

            			newLeafNode(otherlv_0, grammarAccess.getAgentAccess().getAgentKeyword_0());
            		
            // InternalPuRSUEML.g:1146:3: ( (lv_name_1_0= RULE_STRING ) )
            // InternalPuRSUEML.g:1147:4: (lv_name_1_0= RULE_STRING )
            {
            // InternalPuRSUEML.g:1147:4: (lv_name_1_0= RULE_STRING )
            // InternalPuRSUEML.g:1148:5: lv_name_1_0= RULE_STRING
            {
            lv_name_1_0=(Token)match(input,RULE_STRING,FOLLOW_34); 

            					newLeafNode(lv_name_1_0, grammarAccess.getAgentAccess().getNameSTRINGTerminalRuleCall_1_0());
            				

            					if (current==null) {
            						current = createModelElement(grammarAccess.getAgentRule());
            					}
            					setWithLastConsumed(
            						current,
            						"name",
            						lv_name_1_0,
            						"org.eclipse.xtext.common.Terminals.STRING");
            				

            }


            }

            // InternalPuRSUEML.g:1164:3: ( (lv_controllable_2_0= 'controllable' ) )?
            int alt23=2;
            int LA23_0 = input.LA(1);

            if ( (LA23_0==39) ) {
                alt23=1;
            }
            switch (alt23) {
                case 1 :
                    // InternalPuRSUEML.g:1165:4: (lv_controllable_2_0= 'controllable' )
                    {
                    // InternalPuRSUEML.g:1165:4: (lv_controllable_2_0= 'controllable' )
                    // InternalPuRSUEML.g:1166:5: lv_controllable_2_0= 'controllable'
                    {
                    lv_controllable_2_0=(Token)match(input,39,FOLLOW_35); 

                    					newLeafNode(lv_controllable_2_0, grammarAccess.getAgentAccess().getControllableControllableKeyword_2_0());
                    				

                    					if (current==null) {
                    						current = createModelElement(grammarAccess.getAgentRule());
                    					}
                    					setWithLastConsumed(current, "controllable", true, "controllable");
                    				

                    }


                    }
                    break;

            }

            // InternalPuRSUEML.g:1178:3: ( ( (lv_mobile_3_0= 'mobile' ) ) ( (lv_speed_4_0= RULE_INT ) ) )?
            int alt24=2;
            int LA24_0 = input.LA(1);

            if ( (LA24_0==40) ) {
                alt24=1;
            }
            switch (alt24) {
                case 1 :
                    // InternalPuRSUEML.g:1179:4: ( (lv_mobile_3_0= 'mobile' ) ) ( (lv_speed_4_0= RULE_INT ) )
                    {
                    // InternalPuRSUEML.g:1179:4: ( (lv_mobile_3_0= 'mobile' ) )
                    // InternalPuRSUEML.g:1180:5: (lv_mobile_3_0= 'mobile' )
                    {
                    // InternalPuRSUEML.g:1180:5: (lv_mobile_3_0= 'mobile' )
                    // InternalPuRSUEML.g:1181:6: lv_mobile_3_0= 'mobile'
                    {
                    lv_mobile_3_0=(Token)match(input,40,FOLLOW_17); 

                    						newLeafNode(lv_mobile_3_0, grammarAccess.getAgentAccess().getMobileMobileKeyword_3_0_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getAgentRule());
                    						}
                    						setWithLastConsumed(current, "mobile", true, "mobile");
                    					

                    }


                    }

                    // InternalPuRSUEML.g:1193:4: ( (lv_speed_4_0= RULE_INT ) )
                    // InternalPuRSUEML.g:1194:5: (lv_speed_4_0= RULE_INT )
                    {
                    // InternalPuRSUEML.g:1194:5: (lv_speed_4_0= RULE_INT )
                    // InternalPuRSUEML.g:1195:6: lv_speed_4_0= RULE_INT
                    {
                    lv_speed_4_0=(Token)match(input,RULE_INT,FOLLOW_36); 

                    						newLeafNode(lv_speed_4_0, grammarAccess.getAgentAccess().getSpeedINTTerminalRuleCall_3_1_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getAgentRule());
                    						}
                    						setWithLastConsumed(
                    							current,
                    							"speed",
                    							lv_speed_4_0,
                    							"org.eclipse.xtext.common.Terminals.INT");
                    					

                    }


                    }


                    }
                    break;

            }

            // InternalPuRSUEML.g:1212:3: (otherlv_5= 'location' ( (otherlv_6= RULE_ID ) ) )
            // InternalPuRSUEML.g:1213:4: otherlv_5= 'location' ( (otherlv_6= RULE_ID ) )
            {
            otherlv_5=(Token)match(input,19,FOLLOW_14); 

            				newLeafNode(otherlv_5, grammarAccess.getAgentAccess().getLocationKeyword_4_0());
            			
            // InternalPuRSUEML.g:1217:4: ( (otherlv_6= RULE_ID ) )
            // InternalPuRSUEML.g:1218:5: (otherlv_6= RULE_ID )
            {
            // InternalPuRSUEML.g:1218:5: (otherlv_6= RULE_ID )
            // InternalPuRSUEML.g:1219:6: otherlv_6= RULE_ID
            {

            						if (current==null) {
            							current = createModelElement(grammarAccess.getAgentRule());
            						}
            					
            otherlv_6=(Token)match(input,RULE_ID,FOLLOW_37); 

            						newLeafNode(otherlv_6, grammarAccess.getAgentAccess().getInitial_locationPdiCrossReference_4_1_0());
            					

            }


            }


            }

            // InternalPuRSUEML.g:1231:3: (otherlv_7= 'can_do' ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )* )?
            int alt26=2;
            int LA26_0 = input.LA(1);

            if ( (LA26_0==41) ) {
                alt26=1;
            }
            switch (alt26) {
                case 1 :
                    // InternalPuRSUEML.g:1232:4: otherlv_7= 'can_do' ( (otherlv_8= RULE_ID ) ) (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )*
                    {
                    otherlv_7=(Token)match(input,41,FOLLOW_14); 

                    				newLeafNode(otherlv_7, grammarAccess.getAgentAccess().getCan_doKeyword_5_0());
                    			
                    // InternalPuRSUEML.g:1236:4: ( (otherlv_8= RULE_ID ) )
                    // InternalPuRSUEML.g:1237:5: (otherlv_8= RULE_ID )
                    {
                    // InternalPuRSUEML.g:1237:5: (otherlv_8= RULE_ID )
                    // InternalPuRSUEML.g:1238:6: otherlv_8= RULE_ID
                    {

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getAgentRule());
                    						}
                    					
                    otherlv_8=(Token)match(input,RULE_ID,FOLLOW_38); 

                    						newLeafNode(otherlv_8, grammarAccess.getAgentAccess().getActionsEventCrossReference_5_1_0());
                    					

                    }


                    }

                    // InternalPuRSUEML.g:1249:4: (otherlv_9= ',' ( (otherlv_10= RULE_ID ) ) )*
                    loop25:
                    do {
                        int alt25=2;
                        int LA25_0 = input.LA(1);

                        if ( (LA25_0==31) ) {
                            alt25=1;
                        }


                        switch (alt25) {
                    	case 1 :
                    	    // InternalPuRSUEML.g:1250:5: otherlv_9= ',' ( (otherlv_10= RULE_ID ) )
                    	    {
                    	    otherlv_9=(Token)match(input,31,FOLLOW_14); 

                    	    					newLeafNode(otherlv_9, grammarAccess.getAgentAccess().getCommaKeyword_5_2_0());
                    	    				
                    	    // InternalPuRSUEML.g:1254:5: ( (otherlv_10= RULE_ID ) )
                    	    // InternalPuRSUEML.g:1255:6: (otherlv_10= RULE_ID )
                    	    {
                    	    // InternalPuRSUEML.g:1255:6: (otherlv_10= RULE_ID )
                    	    // InternalPuRSUEML.g:1256:7: otherlv_10= RULE_ID
                    	    {

                    	    							if (current==null) {
                    	    								current = createModelElement(grammarAccess.getAgentRule());
                    	    							}
                    	    						
                    	    otherlv_10=(Token)match(input,RULE_ID,FOLLOW_38); 

                    	    							newLeafNode(otherlv_10, grammarAccess.getAgentAccess().getActionsEventCrossReference_5_2_1_0());
                    	    						

                    	    }


                    	    }


                    	    }
                    	    break;

                    	default :
                    	    break loop25;
                        }
                    } while (true);


                    }
                    break;

            }

            // InternalPuRSUEML.g:1269:3: (otherlv_11= 'reacts_to' ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )* )?
            int alt28=2;
            int LA28_0 = input.LA(1);

            if ( (LA28_0==42) ) {
                alt28=1;
            }
            switch (alt28) {
                case 1 :
                    // InternalPuRSUEML.g:1270:4: otherlv_11= 'reacts_to' ( (otherlv_12= RULE_ID ) ) (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )*
                    {
                    otherlv_11=(Token)match(input,42,FOLLOW_14); 

                    				newLeafNode(otherlv_11, grammarAccess.getAgentAccess().getReacts_toKeyword_6_0());
                    			
                    // InternalPuRSUEML.g:1274:4: ( (otherlv_12= RULE_ID ) )
                    // InternalPuRSUEML.g:1275:5: (otherlv_12= RULE_ID )
                    {
                    // InternalPuRSUEML.g:1275:5: (otherlv_12= RULE_ID )
                    // InternalPuRSUEML.g:1276:6: otherlv_12= RULE_ID
                    {

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getAgentRule());
                    						}
                    					
                    otherlv_12=(Token)match(input,RULE_ID,FOLLOW_30); 

                    						newLeafNode(otherlv_12, grammarAccess.getAgentAccess().getReactionsEventCrossReference_6_1_0());
                    					

                    }


                    }

                    // InternalPuRSUEML.g:1287:4: (otherlv_13= ',' ( (otherlv_14= RULE_ID ) ) )*
                    loop27:
                    do {
                        int alt27=2;
                        int LA27_0 = input.LA(1);

                        if ( (LA27_0==31) ) {
                            alt27=1;
                        }


                        switch (alt27) {
                    	case 1 :
                    	    // InternalPuRSUEML.g:1288:5: otherlv_13= ',' ( (otherlv_14= RULE_ID ) )
                    	    {
                    	    otherlv_13=(Token)match(input,31,FOLLOW_14); 

                    	    					newLeafNode(otherlv_13, grammarAccess.getAgentAccess().getCommaKeyword_6_2_0());
                    	    				
                    	    // InternalPuRSUEML.g:1292:5: ( (otherlv_14= RULE_ID ) )
                    	    // InternalPuRSUEML.g:1293:6: (otherlv_14= RULE_ID )
                    	    {
                    	    // InternalPuRSUEML.g:1293:6: (otherlv_14= RULE_ID )
                    	    // InternalPuRSUEML.g:1294:7: otherlv_14= RULE_ID
                    	    {

                    	    							if (current==null) {
                    	    								current = createModelElement(grammarAccess.getAgentRule());
                    	    							}
                    	    						
                    	    otherlv_14=(Token)match(input,RULE_ID,FOLLOW_30); 

                    	    							newLeafNode(otherlv_14, grammarAccess.getAgentAccess().getReactionsEventCrossReference_6_2_1_0());
                    	    						

                    	    }


                    	    }


                    	    }
                    	    break;

                    	default :
                    	    break loop27;
                        }
                    } while (true);


                    }
                    break;

            }


            }


            }


            	leaveRule();

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "ruleAgent"


    // $ANTLR start "entryRuleObjective"
    // InternalPuRSUEML.g:1311:1: entryRuleObjective returns [EObject current=null] : iv_ruleObjective= ruleObjective EOF ;
    public final EObject entryRuleObjective() throws RecognitionException {
        EObject current = null;

        EObject iv_ruleObjective = null;


        try {
            // InternalPuRSUEML.g:1311:50: (iv_ruleObjective= ruleObjective EOF )
            // InternalPuRSUEML.g:1312:2: iv_ruleObjective= ruleObjective EOF
            {
             newCompositeNode(grammarAccess.getObjectiveRule()); 
            pushFollow(FOLLOW_1);
            iv_ruleObjective=ruleObjective();

            state._fsp--;

             current =iv_ruleObjective; 
            match(input,EOF,FOLLOW_2); 

            }

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "entryRuleObjective"


    // $ANTLR start "ruleObjective"
    // InternalPuRSUEML.g:1318:1: ruleObjective returns [EObject current=null] : ( ( ( (lv_is_if_0_0= 'if' ) ) ( (otherlv_1= RULE_ID ) ) otherlv_2= 'then' ( (otherlv_3= RULE_ID ) ) otherlv_4= 'within' ( (lv_time_5_0= RULE_INT ) ) ) | ( ( (lv_is_avoid_6_0= 'avoid' ) ) ( (otherlv_7= RULE_ID ) ) ) ) ;
    public final EObject ruleObjective() throws RecognitionException {
        EObject current = null;

        Token lv_is_if_0_0=null;
        Token otherlv_1=null;
        Token otherlv_2=null;
        Token otherlv_3=null;
        Token otherlv_4=null;
        Token lv_time_5_0=null;
        Token lv_is_avoid_6_0=null;
        Token otherlv_7=null;


        	enterRule();

        try {
            // InternalPuRSUEML.g:1324:2: ( ( ( ( (lv_is_if_0_0= 'if' ) ) ( (otherlv_1= RULE_ID ) ) otherlv_2= 'then' ( (otherlv_3= RULE_ID ) ) otherlv_4= 'within' ( (lv_time_5_0= RULE_INT ) ) ) | ( ( (lv_is_avoid_6_0= 'avoid' ) ) ( (otherlv_7= RULE_ID ) ) ) ) )
            // InternalPuRSUEML.g:1325:2: ( ( ( (lv_is_if_0_0= 'if' ) ) ( (otherlv_1= RULE_ID ) ) otherlv_2= 'then' ( (otherlv_3= RULE_ID ) ) otherlv_4= 'within' ( (lv_time_5_0= RULE_INT ) ) ) | ( ( (lv_is_avoid_6_0= 'avoid' ) ) ( (otherlv_7= RULE_ID ) ) ) )
            {
            // InternalPuRSUEML.g:1325:2: ( ( ( (lv_is_if_0_0= 'if' ) ) ( (otherlv_1= RULE_ID ) ) otherlv_2= 'then' ( (otherlv_3= RULE_ID ) ) otherlv_4= 'within' ( (lv_time_5_0= RULE_INT ) ) ) | ( ( (lv_is_avoid_6_0= 'avoid' ) ) ( (otherlv_7= RULE_ID ) ) ) )
            int alt29=2;
            int LA29_0 = input.LA(1);

            if ( (LA29_0==43) ) {
                alt29=1;
            }
            else if ( (LA29_0==46) ) {
                alt29=2;
            }
            else {
                NoViableAltException nvae =
                    new NoViableAltException("", 29, 0, input);

                throw nvae;
            }
            switch (alt29) {
                case 1 :
                    // InternalPuRSUEML.g:1326:3: ( ( (lv_is_if_0_0= 'if' ) ) ( (otherlv_1= RULE_ID ) ) otherlv_2= 'then' ( (otherlv_3= RULE_ID ) ) otherlv_4= 'within' ( (lv_time_5_0= RULE_INT ) ) )
                    {
                    // InternalPuRSUEML.g:1326:3: ( ( (lv_is_if_0_0= 'if' ) ) ( (otherlv_1= RULE_ID ) ) otherlv_2= 'then' ( (otherlv_3= RULE_ID ) ) otherlv_4= 'within' ( (lv_time_5_0= RULE_INT ) ) )
                    // InternalPuRSUEML.g:1327:4: ( (lv_is_if_0_0= 'if' ) ) ( (otherlv_1= RULE_ID ) ) otherlv_2= 'then' ( (otherlv_3= RULE_ID ) ) otherlv_4= 'within' ( (lv_time_5_0= RULE_INT ) )
                    {
                    // InternalPuRSUEML.g:1327:4: ( (lv_is_if_0_0= 'if' ) )
                    // InternalPuRSUEML.g:1328:5: (lv_is_if_0_0= 'if' )
                    {
                    // InternalPuRSUEML.g:1328:5: (lv_is_if_0_0= 'if' )
                    // InternalPuRSUEML.g:1329:6: lv_is_if_0_0= 'if'
                    {
                    lv_is_if_0_0=(Token)match(input,43,FOLLOW_14); 

                    						newLeafNode(lv_is_if_0_0, grammarAccess.getObjectiveAccess().getIs_ifIfKeyword_0_0_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getObjectiveRule());
                    						}
                    						setWithLastConsumed(current, "is_if", true, "if");
                    					

                    }


                    }

                    // InternalPuRSUEML.g:1341:4: ( (otherlv_1= RULE_ID ) )
                    // InternalPuRSUEML.g:1342:5: (otherlv_1= RULE_ID )
                    {
                    // InternalPuRSUEML.g:1342:5: (otherlv_1= RULE_ID )
                    // InternalPuRSUEML.g:1343:6: otherlv_1= RULE_ID
                    {

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getObjectiveRule());
                    						}
                    					
                    otherlv_1=(Token)match(input,RULE_ID,FOLLOW_39); 

                    						newLeafNode(otherlv_1, grammarAccess.getObjectiveAccess().getCauseEventCrossReference_0_1_0());
                    					

                    }


                    }

                    otherlv_2=(Token)match(input,44,FOLLOW_14); 

                    				newLeafNode(otherlv_2, grammarAccess.getObjectiveAccess().getThenKeyword_0_2());
                    			
                    // InternalPuRSUEML.g:1358:4: ( (otherlv_3= RULE_ID ) )
                    // InternalPuRSUEML.g:1359:5: (otherlv_3= RULE_ID )
                    {
                    // InternalPuRSUEML.g:1359:5: (otherlv_3= RULE_ID )
                    // InternalPuRSUEML.g:1360:6: otherlv_3= RULE_ID
                    {

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getObjectiveRule());
                    						}
                    					
                    otherlv_3=(Token)match(input,RULE_ID,FOLLOW_40); 

                    						newLeafNode(otherlv_3, grammarAccess.getObjectiveAccess().getReactionEventCrossReference_0_3_0());
                    					

                    }


                    }

                    otherlv_4=(Token)match(input,45,FOLLOW_17); 

                    				newLeafNode(otherlv_4, grammarAccess.getObjectiveAccess().getWithinKeyword_0_4());
                    			
                    // InternalPuRSUEML.g:1375:4: ( (lv_time_5_0= RULE_INT ) )
                    // InternalPuRSUEML.g:1376:5: (lv_time_5_0= RULE_INT )
                    {
                    // InternalPuRSUEML.g:1376:5: (lv_time_5_0= RULE_INT )
                    // InternalPuRSUEML.g:1377:6: lv_time_5_0= RULE_INT
                    {
                    lv_time_5_0=(Token)match(input,RULE_INT,FOLLOW_2); 

                    						newLeafNode(lv_time_5_0, grammarAccess.getObjectiveAccess().getTimeINTTerminalRuleCall_0_5_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getObjectiveRule());
                    						}
                    						setWithLastConsumed(
                    							current,
                    							"time",
                    							lv_time_5_0,
                    							"org.eclipse.xtext.common.Terminals.INT");
                    					

                    }


                    }


                    }


                    }
                    break;
                case 2 :
                    // InternalPuRSUEML.g:1395:3: ( ( (lv_is_avoid_6_0= 'avoid' ) ) ( (otherlv_7= RULE_ID ) ) )
                    {
                    // InternalPuRSUEML.g:1395:3: ( ( (lv_is_avoid_6_0= 'avoid' ) ) ( (otherlv_7= RULE_ID ) ) )
                    // InternalPuRSUEML.g:1396:4: ( (lv_is_avoid_6_0= 'avoid' ) ) ( (otherlv_7= RULE_ID ) )
                    {
                    // InternalPuRSUEML.g:1396:4: ( (lv_is_avoid_6_0= 'avoid' ) )
                    // InternalPuRSUEML.g:1397:5: (lv_is_avoid_6_0= 'avoid' )
                    {
                    // InternalPuRSUEML.g:1397:5: (lv_is_avoid_6_0= 'avoid' )
                    // InternalPuRSUEML.g:1398:6: lv_is_avoid_6_0= 'avoid'
                    {
                    lv_is_avoid_6_0=(Token)match(input,46,FOLLOW_14); 

                    						newLeafNode(lv_is_avoid_6_0, grammarAccess.getObjectiveAccess().getIs_avoidAvoidKeyword_1_0_0());
                    					

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getObjectiveRule());
                    						}
                    						setWithLastConsumed(current, "is_avoid", true, "avoid");
                    					

                    }


                    }

                    // InternalPuRSUEML.g:1410:4: ( (otherlv_7= RULE_ID ) )
                    // InternalPuRSUEML.g:1411:5: (otherlv_7= RULE_ID )
                    {
                    // InternalPuRSUEML.g:1411:5: (otherlv_7= RULE_ID )
                    // InternalPuRSUEML.g:1412:6: otherlv_7= RULE_ID
                    {

                    						if (current==null) {
                    							current = createModelElement(grammarAccess.getObjectiveRule());
                    						}
                    					
                    otherlv_7=(Token)match(input,RULE_ID,FOLLOW_2); 

                    						newLeafNode(otherlv_7, grammarAccess.getObjectiveAccess().getLoseEventCrossReference_1_1_0());
                    					

                    }


                    }


                    }


                    }
                    break;

            }


            }


            	leaveRule();

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "ruleObjective"


    // $ANTLR start "entryRuleReachObjective"
    // InternalPuRSUEML.g:1428:1: entryRuleReachObjective returns [EObject current=null] : iv_ruleReachObjective= ruleReachObjective EOF ;
    public final EObject entryRuleReachObjective() throws RecognitionException {
        EObject current = null;

        EObject iv_ruleReachObjective = null;


        try {
            // InternalPuRSUEML.g:1428:55: (iv_ruleReachObjective= ruleReachObjective EOF )
            // InternalPuRSUEML.g:1429:2: iv_ruleReachObjective= ruleReachObjective EOF
            {
             newCompositeNode(grammarAccess.getReachObjectiveRule()); 
            pushFollow(FOLLOW_1);
            iv_ruleReachObjective=ruleReachObjective();

            state._fsp--;

             current =iv_ruleReachObjective; 
            match(input,EOF,FOLLOW_2); 

            }

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "entryRuleReachObjective"


    // $ANTLR start "ruleReachObjective"
    // InternalPuRSUEML.g:1435:1: ruleReachObjective returns [EObject current=null] : (otherlv_0= 'do' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'after' ( (lv_life_span_3_0= RULE_INT ) ) ) ;
    public final EObject ruleReachObjective() throws RecognitionException {
        EObject current = null;

        Token otherlv_0=null;
        Token otherlv_1=null;
        Token otherlv_2=null;
        Token lv_life_span_3_0=null;


        	enterRule();

        try {
            // InternalPuRSUEML.g:1441:2: ( (otherlv_0= 'do' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'after' ( (lv_life_span_3_0= RULE_INT ) ) ) )
            // InternalPuRSUEML.g:1442:2: (otherlv_0= 'do' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'after' ( (lv_life_span_3_0= RULE_INT ) ) )
            {
            // InternalPuRSUEML.g:1442:2: (otherlv_0= 'do' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'after' ( (lv_life_span_3_0= RULE_INT ) ) )
            // InternalPuRSUEML.g:1443:3: otherlv_0= 'do' ( (otherlv_1= RULE_ID ) ) otherlv_2= 'after' ( (lv_life_span_3_0= RULE_INT ) )
            {
            otherlv_0=(Token)match(input,47,FOLLOW_14); 

            			newLeafNode(otherlv_0, grammarAccess.getReachObjectiveAccess().getDoKeyword_0());
            		
            // InternalPuRSUEML.g:1447:3: ( (otherlv_1= RULE_ID ) )
            // InternalPuRSUEML.g:1448:4: (otherlv_1= RULE_ID )
            {
            // InternalPuRSUEML.g:1448:4: (otherlv_1= RULE_ID )
            // InternalPuRSUEML.g:1449:5: otherlv_1= RULE_ID
            {

            					if (current==null) {
            						current = createModelElement(grammarAccess.getReachObjectiveRule());
            					}
            				
            otherlv_1=(Token)match(input,RULE_ID,FOLLOW_41); 

            					newLeafNode(otherlv_1, grammarAccess.getReachObjectiveAccess().getGoalEventCrossReference_1_0());
            				

            }


            }

            otherlv_2=(Token)match(input,48,FOLLOW_17); 

            			newLeafNode(otherlv_2, grammarAccess.getReachObjectiveAccess().getAfterKeyword_2());
            		
            // InternalPuRSUEML.g:1464:3: ( (lv_life_span_3_0= RULE_INT ) )
            // InternalPuRSUEML.g:1465:4: (lv_life_span_3_0= RULE_INT )
            {
            // InternalPuRSUEML.g:1465:4: (lv_life_span_3_0= RULE_INT )
            // InternalPuRSUEML.g:1466:5: lv_life_span_3_0= RULE_INT
            {
            lv_life_span_3_0=(Token)match(input,RULE_INT,FOLLOW_2); 

            					newLeafNode(lv_life_span_3_0, grammarAccess.getReachObjectiveAccess().getLife_spanINTTerminalRuleCall_3_0());
            				

            					if (current==null) {
            						current = createModelElement(grammarAccess.getReachObjectiveRule());
            					}
            					setWithLastConsumed(
            						current,
            						"life_span",
            						lv_life_span_3_0,
            						"org.eclipse.xtext.common.Terminals.INT");
            				

            }


            }


            }


            }


            	leaveRule();

        }

            catch (RecognitionException re) {
                recover(input,re);
                appendSkippedTokens();
            }
        finally {
        }
        return current;
    }
    // $ANTLR end "ruleReachObjective"

    // Delegated rules


 

    public static final BitSet FOLLOW_1 = new BitSet(new long[]{0x0000000000000000L});
    public static final BitSet FOLLOW_2 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_3 = new BitSet(new long[]{0x0000004408227802L});
    public static final BitSet FOLLOW_4 = new BitSet(new long[]{0x0000004408225802L});
    public static final BitSet FOLLOW_5 = new BitSet(new long[]{0x0000004408221802L});
    public static final BitSet FOLLOW_6 = new BitSet(new long[]{0x0000004408201802L});
    public static final BitSet FOLLOW_7 = new BitSet(new long[]{0x0000004408001802L});
    public static final BitSet FOLLOW_8 = new BitSet(new long[]{0x0000004400001802L});
    public static final BitSet FOLLOW_9 = new BitSet(new long[]{0x0000004000001802L});
    public static final BitSet FOLLOW_10 = new BitSet(new long[]{0x0000480000000000L});
    public static final BitSet FOLLOW_11 = new BitSet(new long[]{0x0000000000001002L});
    public static final BitSet FOLLOW_12 = new BitSet(new long[]{0x0000800000000000L});
    public static final BitSet FOLLOW_13 = new BitSet(new long[]{0x0000000000000010L});
    public static final BitSet FOLLOW_14 = new BitSet(new long[]{0x0000000000000020L});
    public static final BitSet FOLLOW_15 = new BitSet(new long[]{0x0000000000008000L});
    public static final BitSet FOLLOW_16 = new BitSet(new long[]{0x0000000000010000L});
    public static final BitSet FOLLOW_17 = new BitSet(new long[]{0x0000000000000040L});
    public static final BitSet FOLLOW_18 = new BitSet(new long[]{0x00000000001C0002L});
    public static final BitSet FOLLOW_19 = new BitSet(new long[]{0x0000000000180002L});
    public static final BitSet FOLLOW_20 = new BitSet(new long[]{0x0000000000100002L});
    public static final BitSet FOLLOW_21 = new BitSet(new long[]{0x0000000000400000L});
    public static final BitSet FOLLOW_22 = new BitSet(new long[]{0x0000000000800020L});
    public static final BitSet FOLLOW_23 = new BitSet(new long[]{0x0000000006000000L});
    public static final BitSet FOLLOW_24 = new BitSet(new long[]{0x0000000001000000L});
    public static final BitSet FOLLOW_25 = new BitSet(new long[]{0x0000000010000000L});
    public static final BitSet FOLLOW_26 = new BitSet(new long[]{0x0000000060000000L});
    public static final BitSet FOLLOW_27 = new BitSet(new long[]{0x0000000080000000L});
    public static final BitSet FOLLOW_28 = new BitSet(new long[]{0x0000000100000000L});
    public static final BitSet FOLLOW_29 = new BitSet(new long[]{0x0000000280000000L});
    public static final BitSet FOLLOW_30 = new BitSet(new long[]{0x0000000080000002L});
    public static final BitSet FOLLOW_31 = new BitSet(new long[]{0x0000000800000000L});
    public static final BitSet FOLLOW_32 = new BitSet(new long[]{0x0000001000000000L});
    public static final BitSet FOLLOW_33 = new BitSet(new long[]{0x0000002000000000L});
    public static final BitSet FOLLOW_34 = new BitSet(new long[]{0x0000018000080000L});
    public static final BitSet FOLLOW_35 = new BitSet(new long[]{0x0000010000080000L});
    public static final BitSet FOLLOW_36 = new BitSet(new long[]{0x0000000000080000L});
    public static final BitSet FOLLOW_37 = new BitSet(new long[]{0x0000060000000002L});
    public static final BitSet FOLLOW_38 = new BitSet(new long[]{0x0000040080000002L});
    public static final BitSet FOLLOW_39 = new BitSet(new long[]{0x0000100000000000L});
    public static final BitSet FOLLOW_40 = new BitSet(new long[]{0x0000200000000000L});
    public static final BitSet FOLLOW_41 = new BitSet(new long[]{0x0001000000000000L});

}