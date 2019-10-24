// Generated from UP2CO.g4 by ANTLR 4.7.1

   package se.cth.pursue;
   import java.util.Set;
   import java.util.HashSet;

import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link UP2COParser}.
 */
public interface UP2COListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link UP2COParser#controller}.
	 * @param ctx the parse tree
	 */
	void enterController(UP2COParser.ControllerContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#controller}.
	 * @param ctx the parse tree
	 */
	void exitController(UP2COParser.ControllerContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#state_block}.
	 * @param ctx the parse tree
	 */
	void enterState_block(UP2COParser.State_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#state_block}.
	 * @param ctx the parse tree
	 */
	void exitState_block(UP2COParser.State_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#state_if}.
	 * @param ctx the parse tree
	 */
	void enterState_if(UP2COParser.State_ifContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#state_if}.
	 * @param ctx the parse tree
	 */
	void exitState_if(UP2COParser.State_ifContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#while_block}.
	 * @param ctx the parse tree
	 */
	void enterWhile_block(UP2COParser.While_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#while_block}.
	 * @param ctx the parse tree
	 */
	void exitWhile_block(UP2COParser.While_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#when_block}.
	 * @param ctx the parse tree
	 */
	void enterWhen_block(UP2COParser.When_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#when_block}.
	 * @param ctx the parse tree
	 */
	void exitWhen_block(UP2COParser.When_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#clock_conditions_set}.
	 * @param ctx the parse tree
	 */
	void enterClock_conditions_set(UP2COParser.Clock_conditions_setContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#clock_conditions_set}.
	 * @param ctx the parse tree
	 */
	void exitClock_conditions_set(UP2COParser.Clock_conditions_setContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#clock_condition}.
	 * @param ctx the parse tree
	 */
	void enterClock_condition(UP2COParser.Clock_conditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#clock_condition}.
	 * @param ctx the parse tree
	 */
	void exitClock_condition(UP2COParser.Clock_conditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#clock_higher_strong}.
	 * @param ctx the parse tree
	 */
	void enterClock_higher_strong(UP2COParser.Clock_higher_strongContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#clock_higher_strong}.
	 * @param ctx the parse tree
	 */
	void exitClock_higher_strong(UP2COParser.Clock_higher_strongContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#clock_higher_weak}.
	 * @param ctx the parse tree
	 */
	void enterClock_higher_weak(UP2COParser.Clock_higher_weakContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#clock_higher_weak}.
	 * @param ctx the parse tree
	 */
	void exitClock_higher_weak(UP2COParser.Clock_higher_weakContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#clock_lower_strong}.
	 * @param ctx the parse tree
	 */
	void enterClock_lower_strong(UP2COParser.Clock_lower_strongContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#clock_lower_strong}.
	 * @param ctx the parse tree
	 */
	void exitClock_lower_strong(UP2COParser.Clock_lower_strongContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#clock_lower_weak}.
	 * @param ctx the parse tree
	 */
	void enterClock_lower_weak(UP2COParser.Clock_lower_weakContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#clock_lower_weak}.
	 * @param ctx the parse tree
	 */
	void exitClock_lower_weak(UP2COParser.Clock_lower_weakContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#clock_equal}.
	 * @param ctx the parse tree
	 */
	void enterClock_equal(UP2COParser.Clock_equalContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#clock_equal}.
	 * @param ctx the parse tree
	 */
	void exitClock_equal(UP2COParser.Clock_equalContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#clock_constant_condition_equality}.
	 * @param ctx the parse tree
	 */
	void enterClock_constant_condition_equality(UP2COParser.Clock_constant_condition_equalityContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#clock_constant_condition_equality}.
	 * @param ctx the parse tree
	 */
	void exitClock_constant_condition_equality(UP2COParser.Clock_constant_condition_equalityContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#clock_constant_condition_1_equality}.
	 * @param ctx the parse tree
	 */
	void enterClock_constant_condition_1_equality(UP2COParser.Clock_constant_condition_1_equalityContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#clock_constant_condition_1_equality}.
	 * @param ctx the parse tree
	 */
	void exitClock_constant_condition_1_equality(UP2COParser.Clock_constant_condition_1_equalityContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#clock_constant_condition_1_strong}.
	 * @param ctx the parse tree
	 */
	void enterClock_constant_condition_1_strong(UP2COParser.Clock_constant_condition_1_strongContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#clock_constant_condition_1_strong}.
	 * @param ctx the parse tree
	 */
	void exitClock_constant_condition_1_strong(UP2COParser.Clock_constant_condition_1_strongContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#clock_constant_condition_1_weak}.
	 * @param ctx the parse tree
	 */
	void enterClock_constant_condition_1_weak(UP2COParser.Clock_constant_condition_1_weakContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#clock_constant_condition_1_weak}.
	 * @param ctx the parse tree
	 */
	void exitClock_constant_condition_1_weak(UP2COParser.Clock_constant_condition_1_weakContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#clock_constant_condition_2_strong}.
	 * @param ctx the parse tree
	 */
	void enterClock_constant_condition_2_strong(UP2COParser.Clock_constant_condition_2_strongContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#clock_constant_condition_2_strong}.
	 * @param ctx the parse tree
	 */
	void exitClock_constant_condition_2_strong(UP2COParser.Clock_constant_condition_2_strongContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#clock_constant_condition_2_weak}.
	 * @param ctx the parse tree
	 */
	void enterClock_constant_condition_2_weak(UP2COParser.Clock_constant_condition_2_weakContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#clock_constant_condition_2_weak}.
	 * @param ctx the parse tree
	 */
	void exitClock_constant_condition_2_weak(UP2COParser.Clock_constant_condition_2_weakContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#transition}.
	 * @param ctx the parse tree
	 */
	void enterTransition(UP2COParser.TransitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#transition}.
	 * @param ctx the parse tree
	 */
	void exitTransition(UP2COParser.TransitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#preconditions}.
	 * @param ctx the parse tree
	 */
	void enterPreconditions(UP2COParser.PreconditionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#preconditions}.
	 * @param ctx the parse tree
	 */
	void exitPreconditions(UP2COParser.PreconditionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#automa_state}.
	 * @param ctx the parse tree
	 */
	void enterAutoma_state(UP2COParser.Automa_stateContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#automa_state}.
	 * @param ctx the parse tree
	 */
	void exitAutoma_state(UP2COParser.Automa_stateContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2COParser#state_variable}.
	 * @param ctx the parse tree
	 */
	void enterState_variable(UP2COParser.State_variableContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2COParser#state_variable}.
	 * @param ctx the parse tree
	 */
	void exitState_variable(UP2COParser.State_variableContext ctx);
}